from pydoc import cli
from ssl import ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY
import tweepy
from pprint import pprint
import schedule
from time import sleep
import json
import os

# アクセストークン読み込み
file = open("info.json", "r")
info = json.load(file)


def ClientInfo():
    client = tweepy.Client(bearer_token=info["BEARER_TOKEN"],
                           consumer_key=info["API_KEY"],
                           consumer_secret=info["API_SECRET"],
                           access_token=info["ACCESS_TOKEN"],
                           access_token_secret=info["ACCESS_TOKEN_SECRET"])

    return client


message = "ﾌﾟｼﾟｼｯﾌﾟｼﾟｼｯﾌﾟｼｯﾌﾟｼｯﾌﾟｼｯﾌﾟｼｯﾌﾟｼｯﾌﾟｼｯﾌﾟｼｯ"


def CreateTweet(message):
    tweet = ClientInfo().create_tweet(text=message)
    return tweet


pprint(CreateTweet(message))
