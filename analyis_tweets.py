import tweepy
import pandas as pd

consumer_key = "TxuJiEViKV6hUCqbBz4KUBmTm"  # Your API/Consumer key
consumer_secret = "GFJUvE4XyiNoDTxs4SH0i5LCeQ1ttAK0Uor9eu1dPug00UboBn"  # Your API/Consumer Secret Key
access_token = "1699391442198929408-spM9t40KkQ0MIYPZ3VZVxvYuSA30eB"    # Your Access token key
access_token_secret = "vuEgVz8Xd76DNSF7Uo56MK6Zvz8iAV8rWLWd4o9IcZCDr"  # Your Access token Secret key

# Pass in our twitter API authentication key
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)

# Instantiate the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)

search_query = "james charles"
no_of_tweets = 2

try:
    # The number of tweets we want to retrieved from the search
    tweets = api.search_tweets(q=search_query, lang="en", count=no_of_tweets, tweet_mode='extended')

    # Pulling Some attributes from the tweet
    attributes_container = [[tweet.user.name, tweet.created_at, tweet.favorite_count, tweet.source, tweet.full_text] for
                            tweet in tweets]

    # Creation of column list to rename the columns in the dataframe
    columns = ["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"]

    # Creation of Dataframe
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
except BaseException as e:
    print('Status Failed On,', str(e))