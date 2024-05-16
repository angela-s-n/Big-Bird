pip install snscrape

import snscrape.modules.twitter as sntwitter

# Function to get tweet timestamps
def get_tweet_timestamps(username, count=1000):
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterUserScraper(username).get_items()):
        if i >= count:
            break
        tweets.append((tweet.id, tweet.date))
    return tweets

# Example usage
username = '0xBalloonLover'
tweet_timestamps = get_tweet_timestamps(username, count=1000)
for tweet_id, timestamp in tweet_timestamps:
    print(f'Tweet ID: {tweet_id}, Timestamp: {timestamp}')
