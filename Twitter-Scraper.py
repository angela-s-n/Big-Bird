import tweepy

# Replace these values with your credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Function to get tweet timestamps
def get_tweet_timestamps(username, count=10):
    tweets = api.user_timeline(screen_name=username, count=count, tweet_mode='extended')
    timestamps = [(tweet.id_str, tweet.created_at) for tweet in tweets]
    return timestamps

# Example usage
username = 'twitter_username'
tweet_timestamps = get_tweet_timestamps(username)
for tweet_id, timestamp in tweet_timestamps:
    print(f'Tweet ID: {tweet_id}, Timestamp: {timestamp}')
