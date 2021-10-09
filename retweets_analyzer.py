import tweepy
from google.cloud import language_v1
import os
import io
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ec601-327921-163f4aceceb9.json'

# Twitter API credentials 
consumer_key = "OWPfglqeVOT5fBAYOj0bsSOW6"
consumer_secret = "I1HlsVm4go9gU6yr50QWdES78G6APx6CvJowASJmI5HuIMByoV"
access_key = "1347722066-3n86zjubxeJjsrUDCtPSFlvxeBkEGcI8YeiUc3V"
access_secret = "bvllPUsptqA7pztYstBM1VlONDAbjL8dCDdi6YPd0Qj5P"

num_tweets = 200 # num of tweets: max 200
NUM_RETWEETS = 200 # retweeted min number  

def get_retweets(tweetID):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    retweets_list = api.retweets(tweetID)
    return retweets_list

def get_tweet(username):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    tweets_list = api.user_timeline(screen_name=username,count=num_tweets)
    return tweets_list

def print_tweetIDs(username):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    tweets_list = get_tweet(username)    
    for tweet in tweets_list:
        status = api.get_status(tweet.id)
        if ((status.retweet_count > NUM_RETWEETS) and ('RT @' not in tweet.text)): ## exclude retweets 
            print("[ID] ", tweet.id, "[COUNT]", status.retweet_count, " [TEXT] ", tweet.text) ## print tweet ID, number of retweets and tweet text 

def get_sentiment_of_retweets(tweetID):
    retweets_list = get_retweets(tweetID)
    num_positive = 0
    num_negative = 0
    num_neutral = 0
    for retweet in retweets_list:
        sentiment_score = analyze_nlp(retweet.text)
        if (sentiment_score > 0):
            num_positive += 1
        elif (sentiment_score < 0):
            num_negative += 1
        else: 
            num_neutral += 1

    return num_positive, num_negative, num_neutral

def print_result_sentiment_of_retweets(tweetID):
    num_positive, num_negative, num_neutral = get_sentiment_of_retweets(tweetID)
    print("positive: ", num_positive, "negative: ", num_negative, "neutral: ", num_neutral)

def analyze_nlp(text_content):
    client = language_v1.LanguageServiceClient()
    type_ = language_v1.Document.Type.PLAIN_TEXT
    language = "ja"
    document = {"content": text_content, "type_": type_, "language": language}
    encoding_type = language_v1.EncodingType.UTF8
    response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    return response.document_sentiment.score

def main():
    print("========================================")
    print("Enter your Twitter user name: ")
    username = input()
    print_tweetIDs(username) ## print tweet ID and tweet text to choose which tweet to analyze it retweets
    print("Enter tweet ID you want to analyze: ") 
    tweetID = input()
    print_result_sentiment_of_retweets(tweetID) ## print the result 

if __name__ == '__main__':
    main()
