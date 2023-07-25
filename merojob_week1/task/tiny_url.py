import hashlib
from django.shortcuts import redirect
import json

url_mapping = {}

def generate_url(url, custom_url=None):
    if custom_url:
        custom_url = "https://short.url/" + custom_url
        return custom_url
    else: 
        md5_hash = hashlib.md5(url.encode()).hexdigest()
        short_url = "https://short.url/" + md5_hash[:5]
        return short_url

def shorten_url(input_url,custom_url):
    if input_url:
        if custom_url and custom_url not in url_mapping:
            shortened_url = generate_url(input_url, custom_url)
            url_mapping[shortened_url] = input_url
        else:
            shortened_url = generate_url(input_url)
            url_mapping[shortened_url] = input_url
        print("Tiny url is:",shortened_url)    
    else:
        return f"Please provide a valid URL."
input_url = input("Enter the url to be shorten:")
custom_url = input("Enter the custom url:")    
shorten_url(input_url,custom_url)    


def find_url(tiny_url):
    if tiny_url in url_mapping:
        original = url_mapping[tiny_url]
        print("Original URL is:",original)
    else:
        return f"Short URL not found."
    
tiny_url = input("Enter the tiny url:")    
find_url(tiny_url)   