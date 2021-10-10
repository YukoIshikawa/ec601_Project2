# ec601 Project2

## Phase 1 (a): Twitter APIs 
- Goal: write test programs to exercise different twitter APIs. For example, retrieving tweets, searching per time, hashtags, etc.
- Due: 9/26/2021 [Done](https://github.com/YukoIshikawa/ec601_Project2/blob/main/twitter_api.py)   
Ex)   
Input: ```@JoeBiden```        
Output:       
``` 
{
 "created_at": "2021-10-08 21:59:53",
 "location": "Washington, DC"
 "text": "We’re making real progress for the American people.",
}
```
etc.,     

## Phase 1 (b): Google NLP
- Goal: write test programs to exercise different Google NLP APIs.  Focus on Sentiment analysis.
- Due: 9/29/2021 [Done](https://github.com/YukoIshikawa/ec601_Project2/blob/main/analyze_nlp.py)      
Ex)   
Input: ```The most interesting course at BU is EC601.```      
Output: ```"sentiment_score": 0.699999988079071, "sentiment_magnitude": 0.699999988079071, "sentiment": "positive"}```

## Phase 2 (a): Build your own social media analyzer - User Stories
- Due date: 10/3/2021[Done](https://github.com/YukoIshikawa/ec601_Project2/blob/main/UserStory.md)   

## Phase 2 (b): Build your own social media analyzer - Completion
- Due date: 10/10/2021[Done](https://github.com/YukoIshikawa/ec601_Project2/blob/main/twitter_nlp_analyzer.py)     
- How to run the code 
  -  ``` git clone  https://github.com/YukoIshikawa/ec601_Project2.git```
  - Enter your Twitter API and Google Cloud API credentials on retweets_analyzer.py file
  - ``` python retweets_analyzer.py```     
- Example input and output     
Retweeted by 285 users but mainly negative responses    
```
User ID: @BlauerSeelowe
Tweet ID: 1446437990243258368
Result: positive:  0 negative:  20 neutral:  0
```

