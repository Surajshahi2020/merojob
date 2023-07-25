from django.shortcuts import render, redirect
from .models import ShortenedURLStore
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta, timezone
from common.func import shorten_url, find_url

def shorten_url_view(request):
    if request.method == "POST":
        input_url = request.POST.get("input_url")
        custom_url = request.POST.get("custom_url")
        existing_shortened_url = ShortenedURLStore.objects.filter(original_url=input_url).first()
        if existing_shortened_url:
            error_message = f"The original URL '{input_url}' already exists in the database with the shortened URL '{existing_shortened_url.custom_url}'"
            return render(request, "index.html", {"error_message": error_message})
        shortened_url = shorten_url(input_url, custom_url)
        if shortened_url:
            ShortenedURLStore.objects.create(original_url=input_url, custom_url=shortened_url)
            return render(request, "result.html", {"shortened_url": shortened_url})
    return render(request, "index.html")

def find_url_view(request):
    if request.method == "POST":
        tiny_url = request.POST.get("tiny_url")
        original_url = find_url(tiny_url)
        if original_url:
            org_url = ShortenedURLStore.objects.get(original_url=original_url)
            now_utc = datetime.now(timezone.utc)
            if now_utc > org_url.created_at + timedelta(minutes=1):
                return render(request, "find.html", {"error_message": "The tiny URL has expired."})
            return HttpResponseRedirect(original_url)
        else:
            raise Http404("Original URL not found")

    return render(request, "find.html")

def list_view(request):
    shortened_urls = ShortenedURLStore.objects.all()
    return render(request, "list.html", {"shortened_urls": shortened_urls})

def find_short_view(request):
    short_param = request.GET.get('short')
    if not short_param:
        return HttpResponse("Missing 'short' parameter in the URL.", status=400)
    try:
        shortened_url = ShortenedURLStore.objects.filter(custom_url=short_param)
        if shortened_url.exists():
            shortened_url = shortened_url.first()
            return HttpResponseRedirect(shortened_url.original_url)
    except ObjectDoesNotExist:
        return HttpResponse("Short URL does not exist.", status=404)