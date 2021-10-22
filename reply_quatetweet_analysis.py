import tweepy
import re
from google.cloud import language_v1
import os
import io
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = ''

# Twitter API credentials 
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

# Tweepy authoritation
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# exclude unnecessary words such @screen_name and URL included during searching
def format_text(text):
    text=re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)
    text=re.sub('\n', " ", text)
    text=re.sub(r'@?[!-~]+', "", text)
    return text

# extract replies and quote retweets with tweetID
def get_replies_and_quotetweets(tweetID):
    status = api.get_status(tweetID)
    row = []
    # query for reply
    query_reply = '@' + status._json['user']['screen_name'] + ' exclude:retweets'
    # extract replies 
    for status_reply in api.search(q=query_reply, lang='ja', count=100):
        if status_reply._json['in_reply_to_status_id'] == status._json['id']:
            row.append(format_text(status_reply._json['text']))
        else:
            continue
    # query for quote tweets 
    query_quote = status._json['id_str'] + ' exclude:retweets'
    # extract quote tweets 
    for status_quote in api.search(q=query_quote, lang='ja', count=100):
        if status_quote._json['id_str'] == status._json['id_str']:
            continue
        else:
            row.append(format_text(status_quote._json['text']))
    
    return row

# take text and return sentiment score 
def analyze_nlp(text_content):
    client = language_v1.LanguageServiceClient()
    type_ = language_v1.Document.Type.PLAIN_TEXT
    language = "ja"
    document = {"content": text_content, "type_": type_, "language": language}
    encoding_type = language_v1.EncodingType.UTF8
    response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    return response.document_sentiment.score

# take tweetID and return the percentage of positive, negative and neutral replies and quote tweets 
def get_sentiment_of_retweets(tweetID):
    row = get_replies_and_quotetweets(tweetID)
    num_positive = 0
    num_negative = 0
    num_neutral = 0
    for retweet in row:
        sentiment_score = analyze_nlp(retweet)
        if (sentiment_score > 0):
            num_positive += 1
        elif (sentiment_score < 0):
            num_negative += 1
        else: 
            num_neutral += 1
    length = len(row)
    return int((num_positive/length)*100), int((num_negative/length)*100), int((num_neutral/length)*100)

# take text and return sentiment score 
def analyze_nlp(text_content):
    client = language_v1.LanguageServiceClient()
    type_ = language_v1.Document.Type.PLAIN_TEXT
    language = "ja"
    document = {"content": text_content, "type_": type_, "language": language}
    encoding_type = language_v1.EncodingType.UTF8
    response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    return response.document_sentiment.score

def print_result_sentiment(tweetID):
    num_positive, num_negative, num_neutral = get_sentiment_of_retweets(tweetID)
    print("The result of sentiment analysis of replies and quote tweets for the tweet")
    print("positive🙂: ", num_positive, "%")
    print("negative🙁: ", num_negative, "%")
    print("neutral😐: ", num_neutral, "%")

if __name__ == '__main__':
    print("Enter tweet ID you want to analyze: ") 
    tweetID = input()
    # print the result of sentiment analysis
    print_result_sentiment(tweetID) 
