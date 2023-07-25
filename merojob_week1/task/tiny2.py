import hashlib
import webbrowser

url_mapping = {}

def generate_url(url, custom_url=None):
    if custom_url:
        custom_url = "https://short.url/" + custom_url
        return custom_url
    else:
        md5_hash = hashlib.md5(url.encode()).hexdigest()
        short_url = "https://short.url/" + md5_hash[:5]
        return short_url

def shorten_url(input_url, custom_url):
    if input_url:
        if custom_url and custom_url not in url_mapping:
            shortened_url = generate_url(input_url, custom_url)
            url_mapping[shortened_url] = input_url
        else:
            shortened_url = generate_url(input_url)
            url_mapping[shortened_url] = input_url
        print("Tiny url is:", shortened_url)
    else:
        return f"Please provide a valid URL."

def find_url(tiny_url):
    if tiny_url in url_mapping:
        original = url_mapping[tiny_url]
        print("Original URL is:", original)
        return original
    else:
        return None

def redirect_to_original(tiny_url):
    original_url = find_url(tiny_url)
    if original_url:
        webbrowser.open(original_url)
    else:
        print("Short URL not found.")

input_url = input("Enter the URL to be shortened:")
custom_url = input("Enter the custom URL:")
shorten_url(input_url, custom_url)

tiny_url = input("Enter the tiny URL:")
redirect_to_original(tiny_url)
