# news.py
import tweepy

def get_temple_news(bearer_token, username="TempleAlert", limit=5):
    """
    Fetches the latest tweets from @TempleAlert using Twitter API v2.
    """
    client = tweepy.Client(bearer_token=bearer_token)

    # Get user ID
    user = client.get_user(username=username)
    user_id = user.data.id

    # Get their latest tweets
    tweets = client.get_users_tweets(
        id=user_id,
        max_results=limit,
        tweet_fields=["created_at", "text"]
    )

    news_list = []
    for t in tweets.data:
        news_list.append({
            "time": t.created_at,
            "text": t.text,
            "url": f"https://twitter.com/{username}/status/{t.id}"
        })

    return news_list
