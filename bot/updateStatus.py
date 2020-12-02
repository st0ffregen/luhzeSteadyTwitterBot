#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
from datetime import datetime
import sys
import os
from tweetText import tweetArray


def updateOrDeleteStatus():
    try:
        cliArgument = sys.argv[1]
        idFile = os.environ['ID_FILE']
    except IndexError as e:
        print("please specify delete/update")
        return 1

    if cliArgument == "update":

        oauth = OAuth()
        api = tweepy.API(oauth)

        response = api.update_status(statusArray[int(datetime.now().strftime('%d'))])

        f = open(idFile, "w")
        f.write(str(response.id))
        f.close()

        f = open(logFile, "a")
        f.write("\n---\n")
        f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        f.write(" updating \n")
        f.write(str(response))
        f.close()

        print(str(response))

    elif cliArgument == "delete":
        f = open(idFile, "r")
        tweetId = f.read()
        f.close()

        oauth = OAuth()
        api = tweepy.API(oauth)

        response = api.destroy_status(tweetId)

        f = open(logFile, "a")
        f.write("\n---\n")
        f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        f.write(" deleting \n")
        f.write(str(response))
        f.close()

        print(response)


    else:
        print("please specify if status should be updated or deleted")


def OAuth():
    try:
        auth = tweepy.OAuthHandler(os.environ['TWITTER_API_KEY'], os.environ['TWITTER_API_SECRET_KEY'])
        auth.set_access_token(os.environ['TWITTER_ACCESS_TOKEN'], os.environ['TWITTER_ACCESS_TOKEN_SECRET'])
        return auth
    except tweepy.error.TweepError as e:
        print(f"something went wrong while authenticating to twitter: {e}")
        return 1


if __name__ == "__main__":
    updateOrDeleteStatus()
