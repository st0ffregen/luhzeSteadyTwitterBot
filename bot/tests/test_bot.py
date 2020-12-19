#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import tweepy
import os
import sys
from dotenv import load_dotenv
sys.path.insert(0, '..')
import updateStatus
import tweetText

load_dotenv()


def initTestingApi():
    auth = tweepy.OAuthHandler(os.environ['TWITTER_API_KEY_TESTING'], os.environ['TWITTER_API_SECRET_KEY_TESTING'])
    auth.set_access_token(os.environ['TWITTER_ACCESS_TOKEN_TESTING'], os.environ['TWITTER_ACCESS_TOKEN_SECRET_TESTING'])
    api = tweepy.API(auth)
    return api


class TestBot(unittest.TestCase):

    tweetId = ""
    fileName = os.environ['ID_FILE']

    def test_init_testing_api(self):
        self.assertIsNotNone(initTestingApi())

    def test_init_api(self):
        self.assertIsNotNone(updateStatus.initApi())

    def test_update_status(self):
        api = initTestingApi()
        self.tweetId = updateStatus.updateStatus(api, self.fileName)
        self.assertIsInstance(self.tweetId, str)

    def test_read_tweet_id(self):
        self.assertEqual(updateStatus.readInId(self.fileName), self.tweetId)

    def test_check_likes(self):
        api = initTestingApi()
        self.assertTrue(updateStatus.checkIfTweetShouldBeDeleted(api, self.tweetId))

    def test_delete_status(self):
        api = initTestingApi()
        self.assertEqual(updateStatus.deleteStatus(api, self.tweetId, self.fileName))


if __name__ == "__main__":
    unittest.main()
