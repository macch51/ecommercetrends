import tweepy
import pandas as pd
from dotenv import load_dotenv
import os
import warnings
from urllib3.exceptions import NotOpenSSLWarning

warnings.filterwarnings("ignore", category=NotOpenSSLWarning)

load_dotenv()

# Twitter API credentials (replace with your own keys)
API_KEY = os.getenv('X_API_KEY')
API_SECRET_KEY = os.getenv('X_API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('X_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('X_ACCESS_TOKEN_SECRET')

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def scrape_tweets(username, count=20):
    try:
        tweets = api.user_timeline(screen_name=username, count=count, tweet_mode='extended')
        tweets_data = [[tweet.created_at, tweet.id_str, tweet.full_text] for tweet in tweets]
        return pd.DataFrame(tweets_data, columns=['Date', 'ID', 'Content'])
    except Exception as e:
        print(f"Error: {e}")

# Example usage
tweets_df = scrape_tweets('Alhadath_Brk', 20)
print(tweets_df)