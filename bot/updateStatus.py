#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
from datetime import datetime
import sys
import os
from bot import tweetText
import traceback


def updateStatus(api, idFile, tweetArray, index):
    print("update status")
    response = api.update_status(tweetArray[index])
    print(str(response))
    writeToFile(idFile, str(response.id))
    return str(response.id)


def checkIfTweetShouldBeDeleted(api, tweetId):
    print("check if tweet should be deleted")
    status = api.get_status(tweetId)
    print(status)
    if status.favorite_count > 0 or status.retweet_count > 0:
        return False
    else:
        return True


def deleteStatus(api, tweetId, idFile):
    if checkIfTweetShouldBeDeleted(api, tweetId) is True:
        print("delete status")
        response = api.destroy_status(tweetId)
        print(str(response))
    else:
        print("do not delete status")

    writeToFile(idFile, "")
    return 0


def readInId(fileName):
    # figure out if we have to update or delete
    idFile = fileName
    f = open(idFile, "r")
    tweetId = f.read()
    f.close()
    return tweetId


def writeToFile(fileName, text):
    f = open(fileName, "w")
    f.write(text)
    f.close()
    return 0


def updateOrDeleteStatus():
    print("---")
    print("starting bot")
    print("utc time now: " + datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))

    api = initApi()
    fileName = os.environ['ID_FILE']
    tweetId = readInId(fileName)

    try:
        if tweetId == "":
            updateStatus(api, fileName, tweetText.tweetArray, int(datetime.now().strftime('%d')) - 1)
        else:
            deleteStatus(api, tweetId, fileName)

    except tweepy.error.TweepError as err:
        print(f"error while working with twitter api: {err}")
        traceback.print_exc()
        print("exiting")
        print(sys.exc_info())
        sys.exit(1)

    return 0


def initApi():
    auth = tweepy.OAuthHandler(os.environ['TWITTER_API_KEY'], os.environ['TWITTER_API_SECRET_KEY'])
    auth.set_access_token(os.environ['TWITTER_ACCESS_TOKEN'], os.environ['TWITTER_ACCESS_TOKEN_SECRET'])
    api = tweepy.API(auth)
    return api


if __name__ == "__main__":
    updateOrDeleteStatus()
