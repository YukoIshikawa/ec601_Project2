import tweepy 
import json

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""
num_tweet = 10

def get_tweets_from_user(screen_name):
    
    alltweets = []    
    new_tweets = api.user_timeline(screen_name = screen_name,count=10)
    
    alltweets.extend(new_tweets)
    
    oldest = alltweets[-1].id - 1
    
    while len(new_tweets) > 0:
        
        new_tweets = api.user_timeline(screen_name = screen_name,count=10,max_id=oldest)
        
        alltweets.extend(new_tweets)

        oldest = alltweets[-1].id - 1
        if(len(alltweets) > 15):
            break
       
    file = open('tweets_from_user.json', 'w') 
    for status in alltweets:
        json.dump(status._json,file,sort_keys = True,indent = 4)
    file.close()

def get_tweets_from_hashtag(words, date_since, numtweet):
    
    tweets = tweepy.Cursor(api.search, q=words, lang="en", since=date_since, tweet_mode='extended').items(numtweet)
     
    list_tweets = [tweet for tweet in tweets]
      
    i = 1  

    for tweet in list_tweets:
        username = tweet.user.screen_name
        description = tweet.user.description
        location = tweet.user.location
        following = tweet.user.friends_count
        followers = tweet.user.followers_count
        totaltweets = tweet.user.statuses_count
        retweetcount = tweet.retweet_count
        hashtags = tweet.entities['hashtags']
          
        try:
            text = tweet.retweeted_status.full_text
        except AttributeError:
            text = tweet.full_text
        hashtext = list()
        for j in range(0, len(hashtags)):
            hashtext.append(hashtags[j]['text'])
          
        ith_tweet = [username, description, location, following,
                     followers, totaltweets, retweetcount, text, hashtext]
          
        file = open('tweets_from_hashtag.json', 'w') 
        for status in ith_tweet:
            json.dump(status._json,file,sort_keys = True,indent = 4)
        file.close()

if __name__ == '__main__':

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    print("Username that you want to search for: ")
    user = input()
    get_tweets_from_user(user)

    print("Twitter HashTag that you want to search for: ")
    words = input()
    print("Date ex) yyyy-mm--dd: ")
    date_since = input()
    get_tweets_from_hashtag(words, date_since, num_tweet)
