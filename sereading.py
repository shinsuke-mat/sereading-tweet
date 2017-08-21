#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Tweepyライブラリをインポート
import tweepy
import ConfigParser

ini = ConfigParser.SafeConfigParser()
ini.read('config.ini')

# create api instance
def create_api():
    auth = tweepy.OAuthHandler(ini.get('token', 'consumer_key'), ini.get('token', 'consumer_secret'))
    auth.set_access_token(ini.get('token', 'access_token'), ini.get('token', 'access_secret'))
    #APIインスタンスを作成
    return tweepy.API(auth)

# get tweet list
def get_tweet_list():
    import re
    import datetime
    api = create_api()
    #tweets = api.user_timeline(id='sereading_jp', count=200)
    tweets = api.user_timeline(id=ini.get('general', 'twitter_id'), count=200)
    data = []
    for tweet in tweets:
        p = tweet.created_at
        if p < datetime.datetime(int(ini.get('general', 'tweet_year_from')),1,1): continue
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
    df = df.sort_values("sum", ascending=False)
    return df

# tweet session
def tweet_session_name(sid):
    import pandas as pd
    a = pd.read_csv(ini.get('file', 'assignment'), index_col='sid')
    text = str(sid) + ". " + a["title"][sid] + " (" + a["name"][sid] + ') #sereading'
    api = create_api()
    api.update_status(status=text)

# tweet paper
def tweet_paper_name(pid):
    import pandas as pd
    p = pd.read_csv(ini.get('file', 'paper'), index_col='pid')
    text = pid + ": " + p["ptitle"][pid]
    if len(text)>129:
        text = text[0:126] + "..."
    text = text + " #sereading"
    api = create_api()
    api.update_status(status=text)

# これだけで、Twitter APIをPythonから操作するための準備は完了。
print('Done!')

