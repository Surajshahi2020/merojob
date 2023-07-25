import hashlib
from django.shortcuts import redirect

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
            url_mapping[custom_url] = input_url
            print(url_mapping)
            return url_mapping
        
        else:
            shortened_url = generate_url(input_url)
            url_mapping[shortened_url] = input_url
            return url_mapping

    else:
        return f"Please provide a valid URL."
input_url = input("Enter the url to be shorten:")
custom_url = input("Enter the custom url:")    
shorten_url(input_url,custom_url)    
print("Your shortened url is:",url_mapping)

def find_url(short_url):
    if short_url in url_mapping:
        return url_mapping[short_url]
    else:
        return f"Short URL not found."
short_url = input("Enter the short url:")    
find_url(short_url)    
print("Your URL is:",url_mapping)
