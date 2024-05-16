import tweepy

# Replace these values with your credentials
consumer_key = 'LXl6Xix0TXH8K7hMayjTe6zpG'
consumer_secret = 'YAIWZak0QjP1O6R1g2TMhPJf9fRC8rNUjII1Uiyfc3DY2drF7Y'
access_token = '1589963824110735360-ixoBa6fMKRftkxa9GZgjupkLAs0Yyz'
access_token_secret = 'fOrHaNXgFVax1mo4NPUKAnFE1V4Chp3FeeOWDAjE1Bg1s'

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Function to get tweet timestamps
def get_tweet_timestamps(username, count=10):
    tweets = api.user_timeline(screen_name=username, count=count, tweet_mode='extended')
    timestamps = [(tweet.id_str, tweet.created_at) for tweet in tweets]
    return timestamps

# Example usage
username = 'angela_sun__'
tweet_timestamps = get_tweet_timestamps(username)
for tweet_id, timestamp in tweet_timestamps:
    print(f'Tweet ID: {tweet_id}, Timestamp: {timestamp}')
