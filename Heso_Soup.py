import tweepy
from pprint import pprint
import json
import TweetMsgManager
from time import sleep
import logging

LOGGING_TIME = 60
TWEET_TIME = 3600


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

# def getDuplicateList(message, info):
#    tweetList = []
#    tweets = ClientInfo(info).get_users_tweets("HesoSoup")
#   # if(tweets.data != None):
#   #     for t in tweets.data:
#   #         tweetList.append(t.text)
#   # else:
#   #     tweetList.append("")
#
#    return tweetList


def main():
    infoFile = "info.json"
    info = getAccessInfo(infoFile)
    msgManager = TweetMsgManager.CTweetMessageManager()
    timeCount = 0
    formatter = '%(asctime)s : %(levelname)s : %(message)s'
    logging.basicConfig(filename='Push.log',
                        format=formatter, level=logging.INFO)

    # 起動時に一度ツイート
    message = msgManager.createMsg()
    logging.info(CreateTweet(message, info))
    # 1時間毎にツイートする
    try:
        while True:
            message = msgManager.createMsg()

            if((timeCount % LOGGING_TIME) == 0):
                logging.info("ﾌﾟｼｭ...")

            if(timeCount == TWEET_TIME):
                message = msgManager.createMsg()
                # pprint(CreateTweet(message, info))  # Tweet実行
                logging.info(CreateTweet(message, info))
                timeCount = 0

            sleep(1)
            timeCount += 1

    except KeyboardInterrupt:
        print("ﾌﾟｼュｳｳｳｳｳ…")
        logging.info("正常")
    except tweepy.TweepyException as e:
        print("tweepyエラーﾌﾟｼｭ...", e)
        logging.info(e)
    except Exception as e:
        print("エラーﾌﾟｼｭ...")
        logging.info(e)


if __name__ == "__main__":
    main()
