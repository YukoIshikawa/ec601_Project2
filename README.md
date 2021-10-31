# ec601 Project2

## Phase 1 (a): Twitter APIs 
- Goal: write test programs to exercise different twitter APIs. For example, retrieving tweets, searching per time, hashtags, etc.
- Due: 9/26/2021 [Done](https://github.com/YukoIshikawa/ec601_Project2/blob/main/twitter_api.py)       
- Output is stored into csv file

## Phase 1 (b): Google NLP
- Goal: write test programs to exercise different Google NLP APIs.  Focus on Sentiment analysis.
- Due: 9/29/2021 [Done](https://github.com/YukoIshikawa/ec601_Project2/blob/main/analyze_nlp.py)      
- Example input and output   
Input: ```The most interesting course at BU is EC601.```      
Output: ```"sentiment_score": 0.699999988079071, "sentiment_magnitude": 0.699999988079071, "sentiment": "positive"}```

## Phase 2 (a): Build your own social media analyzer - User Stories
- Due date: 10/3/2021
- You can see it from here: [User Story](https://github.com/YukoIshikawa/ec601_Project2/blob/main/UserStory.md)   

## Phase 2 (b): Build your own social media analyzer - Completion
- Due date: 10/10/2021
- You can see it from here: [quotetweet_reply_analyzer.py](https://github.com/YukoIshikawa/ec601_Project2/blob/main/quotetweet_reply_analyzer.py)     
- How to run the code 
  -  ``` git clone  https://github.com/YukoIshikawa/ec601_Project2.git```
  - Enter your Twitter API and Google Cloud API credentials on quotetweet_reply_analyzer.py file
  - ``` python quotetweet_reply_analyzer.py```     
- Example input and output     
TweetID: 1451354572933550081   
```
The result of sentiment analysis of replies and quote tweets for the tweet
positive🙂:  28 %
negative🙁:  0 %
neutral😐:  71 %
```
## Phase 3 (a): Write Unit tests for Projectt 2
- Due date: 10/29/2021
- You can see it here: [quotetweet_reply_analyzer_test.py](https://github.com/YukoIshikawa/ec601_Project2/blob/main/quotetweet_reply_analyzer_test.py)
- Note: my code passed the unit test with google cloud and twitter API credentials [You can see it here](https://github.com/YukoIshikawa/ec601_Project2/actions/runs/1397717822), but it has errors now since I deleted credentials 

## Phase 3 (b): Code Review
- Due Date: 11/1/2021
- You can see it here: [code review](https://github.com/hn957/EC601_project2/issues/1)

