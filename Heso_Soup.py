import tweepy
from pprint import pprint
import json
import TweetMsgManager
from time import sleep


def getAccessInfo(infoFile):
    file = open(infoFile, "r")
    info = json.load(file)
    return info


def ClientInfo(info):
    client = tweepy.Client(bearer_token=info["BEARER_TOKEN"],
                           consumer_key=info["API_KEY"],
                           consumer_secret=info["API_SECRET"],
                           access_token=info["ACCESS_TOKEN"],
                           access_token_secret=info["ACCESS_TOKEN_SECRET"])

    return client


def CreateTweet(message, infoinfo):
    return ClientInfo(infoinfo).create_tweet(text=message)


def main():
    infoFile = "info.json"
    info = getAccessInfo(infoFile)
    msgManager = TweetMsgManager.CTweetMessageManager()
    while True:
        message = msgManager.createMsg()
        pprint(CreateTweet(message, info))
        # 暫定1時間Sleep
        sleep(360)


if __name__ == "__main__":
    main()
