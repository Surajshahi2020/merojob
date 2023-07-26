from django.urls import path
from tinyapp.views import shorten_url_view, list_view,find_url_view,find_short_view
urlpatterns = [
    path('create/',shorten_url_view,name="create"),
    path('find/',find_url_view,name="find"),
    path('list/',list_view,name="list"),
    path("<str:url>",find_short_view,name="find in url")

]