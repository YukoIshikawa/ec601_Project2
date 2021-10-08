import urllib
from requests_oauthlib import OAuth1Session, OAuth1
import requests
import sys
import tweepy
from google.cloud import language_v1
import os
import io
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = ''

# API token
CK = ""
CKS = ""
AT = ""
ATS = ""

def check_reply_positivity():
    # user and tweet ID
    print("Enter the twitter username you want to analyze: ")
    user_id = input()
    print("Enter the twitter id you want to analyze: ")
    tweet_id = input()
    # parameter 
    count = 100 # max number of tweets that can be searched for one time (default: 15)
    count_range = 100 
    # extract tweet and reply
    tweets = search_tweets(CK, CKS, AT, ATS, user_id, tweet_id, count, count_range)
    # display the result
    positive = 0
    negative = 0
    neutral = 0
    for i in range(len(tweets)):
        result = analyze_nlp(tweets[i])
        if (result == "positive"):
            positive += 1
        elif (result == "negative"):
            negative += 1
        elif (result == "neutral"):
            neutral += 1
    
    print("positive: ", positive, "negative: ", negative, "neutral: ", neutral)

def search_tweets(CK, CKS, AT, ATS, user_id, tweet_id, count, count_range):
    # set up
    user_id += ' exclude:retweets' # exclude retweet 
    user_id = urllib.parse.quote_plus(user_id)
    # request
    url = "https://api.twitter.com/1.1/search/tweets.json?lang=ja&q="+user_id+"&count="+str(count)
    auth = OAuth1(CK, CKS, AT, ATS)
    response = requests.get(url, auth=auth)
    data = response.json()['statuses']
    # request after two times 
    cnt = 0
    reply_cnt = 0
    tweets = []
    while True:
        if len(data) == 0:
            break
        cnt += 1
        if cnt > count_range:
            break
        for tweet in data:
            if tweet['in_reply_to_status_id_str'] == tweet_id: # extract tweets which corresponds to ID
                tweets.append(tweet['text'])  # twetter text 
                reply_cnt += 1
            maxid = int(tweet["id"]) - 1
        url = "https://api.twitter.com/1.1/search/tweets.json?lang=ja&q="+user_id+"&count="+str(count)+"&max_id="+str(maxid)
        response = requests.get(url, auth=auth)
        try:
            data = response.json()['statuses']
        except KeyError: # print error when it reaches the limit
            print('reaches the limit')
            break
    print('number of searches :', cnt)
    print('number of replies :', reply_cnt)
    return tweets

def analyze_nlp(text_content):

    client = language_v1.LanguageServiceClient()
    
    type_ = language_v1.Document.Type.PLAIN_TEXT
    
    language = "en"
    
    document = {"content": text_content, "type_": type_, "language": language}
    
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})

    if response.document_sentiment.score < 0:
        result = "negative"
    elif response.document_sentiment.score > 0:
        result = "positive"
    else:
        retuslt = "neutral"

    return result

if __name__ == '__main__':
    check_reply_positivity()
