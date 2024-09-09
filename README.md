# Summary

This codes scrapes X (Twitter) for tweets associated with a list of stock tickers and computes an average polarity measure capturing the average sentiment of the tweets for each stock. It then feeds this information along with information about the sector of the company and the time it took to go public into a linear regression algorithm to predict the return by the end of the day of the stock’s ipo. This code could be easily modified to utilize alternative supervised learning algorithms or to account for other features that may be related to first day ipo returns. 

The ipoReturnsFunctions document contains the relevant function related to scraping the tweets from Twitter and computing the average polarity for a given stock. The package used for fetching the tweets from Twitter is called Tweepy and the code also needs TextBlob for parsing the text data.

The ipoReturns document exports the polarity results of the sentiment analysis to an excel document (attached) and runs the regression algorithm on that data as well as the data on the sector and time to ipo which is already written into the document. 

The xCredentials document contains the API key and secret key needed to pull tweets from X. Note that as of May 2023 the features of the Twitter API used in this code requires a basic membership. TextBlob also requires the download of python -m textblob.download_corpora.
