from urllib.parse import MAX_CACHE_SIZE
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


def checkDuplicate(message, info):
    tweetList = []
    tweets = ClientInfo(info).search_recent_tweets(
        query=message, max_results=10)
    if(tweets.data != None):
        for t in tweets.data:
            tweetList.append(t.text)
    else:
        tweetList.append("")

    return tweetList


def main():
    infoFile = "info.json"
    info = getAccessInfo(infoFile)
    msgManager = TweetMsgManager.CTweetMessageManager()
    try:
        while True:
            message = msgManager.createMsg()
            duplicateList = checkDuplicate(message, info)
            while(duplicateList.count(message) > 0):
                message = msgManager.createMsg()
                duplicateList = checkDuplicate(message, info)

            pprint(CreateTweet(message, info))
            # 暫定1時間Sleep
            # sleep(60)
    except KeyboardInterrupt:
        print("ﾌﾟｼｭ…")


if __name__ == "__main__":
    main()
