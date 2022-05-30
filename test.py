import tweepy
from pprint import pprint
import json
import TweetMsgManager
from time import sleep
import logging


def getAccessInfo(infoFile):
    file = open(infoFile, "r")
    info = json.load(file)
    return info


def API(info):

    auth = tweepy.OAuth1UserHandler(
        consumer_key=info["API_KEY"], consumer_secret=info["API_SECRET"])
    auth.set_access_token(
        access_token=info["ACCESS_TOKEN"], access_token_secret=info["ACCESS_TOKEN_SECRET"])

    api = tweepy.API(auth)

    client = tweepy.Client(bearer_token=info["BEARER_TOKEN"],
                           consumer_key=info["API_KEY"],
                           consumer_secret=info["API_SECRET"],
                           access_token=info["ACCESS_TOKEN"],
                           access_token_secret=info["ACCESS_TOKEN_SECRET"])
    return client


def main():
    pass


if __name__ == "__main__":
    main()
