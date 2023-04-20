import requests



r = requests.get(' https://hacker-news.firebaseio.com/v0/item/8863.json?print=pretty')
website_content = r.json()
print(website_content)