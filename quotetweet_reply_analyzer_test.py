from quotetweet_reply_analyzer import *
import pytest

def test_format_text():
    assert format_text("@Yuko") == ""
  
def test_get_replies_and_quotetweets():
    assert get_replies_and_quotetweets(1448674345027399681) == []

def test_calc_percentage():
    assert calc_percentage(30, 100) == 30
    assert calc_percentage(20, 0) == 0

def test_get_sentiment_of_retweets():
    assert get_sentiment_of_retweets(1448674345027399681) == (0, 0, 0)

def test_analyze_nlp():
    assert analyze_nlp("Today is beautiful") == 0.8999999761581421
    assert analyze_nlp("I hate boston") == -0.8999999761581421
