import tweepy
import os
from dotenv import load_dotenv
load_dotenv()

# Access credentials within .env
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

tweets = api.search_tweets(q="python", lang="en")
for tweet in tweets:
    print(f"Found tweet number:\n {tweet.id}\n")
    print(f"Tweeted by:\n {tweet.author.screen_name}\n")
    print(f"With the info:\n {tweet.text}\n")
    api.create_favorite(tweet.id)
    api.retweet(tweet.id)