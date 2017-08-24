# sereading-tweet
- [sereading](https://sites.google.com/site/sereadings)用の[twitterアカウント](https://twitter.com/sereading_jp)管理スクリプト
- セッション番号とペーパーIDをつぶやく


## 準備
### assignment.csvとpaper.csvを更新
- [sereading管理スプレッドシート](http://bit.ly/sereading-icse17-s)からコピペ推奨

### config.iniを更新
- twitterのapi tokenの追加
- tweet-year-fromを更新（ランキング算出時に過去のツイートをカウントしないように年度を定義）

## 使い方
```python
# セッション番号をつぶやく
tweet_session_name(1)

# ペーパーIDをつぶやく
tweet_paper_name('1-1')

# ランキングの収集
get_ranking_dataframe()
```
