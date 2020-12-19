#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
from datetime import datetime
import sys
import os
from tweetText import tweetArray
import traceback


def updateStatus(api, idFile):
    print("update status")
    response = api.update_status(tweetArray[int(datetime.now().strftime('%d')) - 1])
    print(str(response))
    f = open(idFile, "w")
    f.write(str(response.id))
    f.close()
    return 0


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

    f = open(idFile, "w")
    f.write("")
    f.close()
    return 0


def updateOrDeleteStatus():
    print("---")
    print("starting bot")
    print("utc time now: " + datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))
    idFile = os.environ['ID_FILE']

    # figure out if we have to update or delete
    f = open(idFile, "r")
    tweetId = f.read()
    f.close()

    # get api
    oauth = OAuth()
    api = tweepy.API(oauth)

    try:
        if tweetId == "":
            updateStatus(api, idFile)
        else:
            deleteStatus(api, tweetId, idFile)

    except tweepy.error.TweepError as err:
        print(f"error while working with twitter api: {err}")
        traceback.print_exc()
        print("exiting")
        print(sys.exc_info())
        sys.exit(1)

    return 0


def OAuth():
    auth = tweepy.OAuthHandler(os.environ['TWITTER_API_KEY'], os.environ['TWITTER_API_SECRET_KEY'])
    auth.set_access_token(os.environ['TWITTER_ACCESS_TOKEN'], os.environ['TWITTER_ACCESS_TOKEN_SECRET'])
    return auth


if __name__ == "__main__":
    updateOrDeleteStatus()
