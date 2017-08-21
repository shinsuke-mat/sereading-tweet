#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Tweepyライブラリをインポート
import tweepy

# 各種キーをセット
CONSUMER_KEY = 
CONSUMER_SECRET = 
ACCESS_TOKEN = 
ACCESS_SECRET = 

FILE_ASSIGNMENT = '/Users/kyoheif/Documents/work/sereading/assignment.csv'
FILE_PAPER = '/Users/kyoheif/Documents/work/sereading/paper.csv'

# create api instance
def create_api():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    #APIインスタンスを作成
    return tweepy.API(auth)

# get tweet list
def get_tweet_list():
    import re
    api = create_api()
    tweets = api.user_timeline(id='sereading_jp', count=200)
    data = []
    for tweet in tweets:
        m = re.match("\d?\d-\d", tweet.text)
        if m:
            data.append([m.group(), tweet.favorite_count, tweet.retweet_count])
    return data

# ranking
def get_ranking_dataframe():
    import pandas as pd
    df = pd.DataFrame(get_tweet_list())
    df.columns = ["pid", "likes", "RTs"]
    df["sum"] = df[["likes", "RTs"]].sum(axis=1)
    df = df.sort("sum", ascending=False)
    return df

# tweet session
def tweet_session_name(sid):
    import pandas as pd
    a = pd.read_csv(FILE_ASSIGNMENT,index_col='sid')
    text = str(sid) + ". " + a["title"][sid] + " (" + a["name"][sid] + ') #sereading'
    api = create_api()
    api.update_status(status=text)

# tweet paper
def tweet_paper_name(pid):
    import pandas as pd
    p = pd.read_csv(FILE_PAPER,index_col='pid')
    text = pid + ": " + p["ptitle"][pid]
    if len(text)>129:
        text = text[0:126] + "..."
    text = text + " #sereading"
    api = create_api()
    api.update_status(status=text)

# これだけで、Twitter APIをPythonから操作するための準備は完了。
print('Done!')

