# testnews.py
from news import get_temple_news

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAIP74wEAAAAARijYh30vnDEJI8QjzH2WpR6OMts%3D3gaeXtY5itWqlxfDT3Ckyez8g4fQxuM3YxzjV9bAMxcrAdH71m"

news = get_temple_news(BEARER_TOKEN, "TempleAlert")

for item in news:
    print(f"{item['time']} → {item['text']}\n{item['url']}\n")
