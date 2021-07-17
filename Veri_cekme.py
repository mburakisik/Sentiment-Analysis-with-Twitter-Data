# Gerekli kütüphanelerin içe aktarılması
import tweepy
import pandas as pd

# API bağlantısı
auth = tweepy.OAuthHandler("xxx", "xxx")
auth.set_access_token("xxx", "xxx")

api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

tweet_icerik = []

df = pd.DataFrame()

# Tweetleri toplanması ve liste olarak kaydedilmesi
for counter,tweet in enumerate(tweepy.Cursor(api.search, q="futbol -RT",  lang= 'tr', tweet_mode = "extended").items(2000)):

    tweet_icerik.append(tweet.full_text)

df["tweet"] = tweet_icerik

df.to_excel("ham_data.xlsx")
