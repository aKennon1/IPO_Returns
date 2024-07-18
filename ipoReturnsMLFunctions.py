############################################################################
#
# ipoReturnsMLFunctions 
#
############################################################################

import re
import tweepy
import statistics
from tweepy import OAuthHandler
from textblob import TextBlob
from xCredentials import * # Credentials for logging into Twitter dev console

############################################################################
############################################################################
 
class TwitterClient: 

    def __init__(self):
        
    # Needed below is information from the Twitter dev console
        
        client_key = clientID
        client_secret = clientSecret
        access_token = accessToken
        access_token_secret = accessSecret
 
        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")
 
############################################################################

    def cleanTweet(self, tweet): 
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

############################################################################
 
    def getSentiment(self, tweet): 
        analysis = TextBlob(self.cleanTweet(tweet))
        return analysis.sentiment.polarity # returns a number corresponding to the strength of the tweet sentiment

############################################################################
 
    def getTweets(self, query, number):
        
        tweets = []
 
        try:
            fetched_tweets = self.api.search(q = query, count = number)
 
            for tweet in fetched_tweets:
                parsed_tweet = {}
                parsed_tweet['text'] = tweet.text # This just returns the unprocessed text which is not used later
                parsed_tweet['sentiment'] = self.getSentiment(tweet.text) # This returns the sentiment of the processed text
 
                if tweet.retweet_count > 0:
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)
 
            return tweets
 
        except tweepy.TweepError as e:
            print("Error : " + str(e))
        
############################################################################
 
def avgPolarity(ticker, number): # The Twitter search is for the stock ticker 
    api = TwitterClient()
    tweets = api.getTweets(ticker, number) # This is a list of dictionaries corresponding to each tweet
    polarityListTweets = []
    for tweet in tweets:
        polarityListTweets.append(tweet['sentiment']) 
    return statistics.mean(polarityListTweets) # Returns the average sentiment for all of the tweets corresponding to a given stock ticker
 

