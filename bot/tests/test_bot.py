#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import tweepy
import os
import sys
from dotenv import load_dotenv
import random
import string
sys.path.insert(0, '..')
import updateStatus


load_dotenv()


class TestBot(unittest.TestCase):

    tweetId = ""
    fileName = os.environ['ID_FILE']
    api = None
    testingArray = [
        "testing tweet",
        "testing status",
        "testing update",
        "testing steady application",
        "testing new app",
        "testing with tweepy"
    ]

    @classmethod
    def setUpClass(cls) -> None:
        auth = tweepy.OAuthHandler(os.environ['TWITTER_API_KEY_TESTING'], os.environ['TWITTER_API_SECRET_KEY_TESTING'])
        auth.set_access_token(os.environ['TWITTER_ACCESS_TOKEN_TESTING'],
                              os.environ['TWITTER_ACCESS_TOKEN_SECRET_TESTING'])
        cls.api = tweepy.API(auth)
        # generate random string
        letters = string.ascii_lowercase
        # edit testing array
        for i in range(0, len(TestBot.testingArray)):
            resultStr = ''.join(random.choice(letters) for i in range(10))
            TestBot.testingArray[i] = TestBot.testingArray[i] + " " + resultStr

    def test_init_api(self):
        self.assertIsNotNone(updateStatus.initApi())

    def test_update_status(self):
        self.tweetId = updateStatus.updateStatus(TestBot.api, self.fileName, self.testingArray, random.randint(0, 5))
        self.assertIsInstance(self.tweetId, str)
        self.assertEqual(updateStatus.deleteStatus(TestBot.api, self.tweetId, self.fileName), 0)

    def test_read_tweet_id(self):
        self.tweetId = updateStatus.updateStatus(TestBot.api, self.fileName, self.testingArray, random.randint(0, 5))
        self.assertIsInstance(self.tweetId, str)
        self.assertEqual(updateStatus.readInId(self.fileName), self.tweetId)
        self.assertEqual(updateStatus.deleteStatus(TestBot.api, self.tweetId, self.fileName), 0)

    def test_check_likes(self):
        self.tweetId = updateStatus.updateStatus(TestBot.api, self.fileName, self.testingArray, random.randint(0, 5))
        self.assertIsInstance(self.tweetId, str)
        self.assertTrue(updateStatus.checkIfTweetShouldBeDeleted(TestBot.api, self.tweetId))
        self.assertEqual(updateStatus.deleteStatus(TestBot.api, self.tweetId, self.fileName), 0)

    def test_delete_status(self):
        self.tweetId = updateStatus.updateStatus(TestBot.api, self.fileName, self.testingArray, random.randint(0, 5))
        self.assertIsInstance(self.tweetId, str)
        self.assertEqual(updateStatus.deleteStatus(TestBot.api, self.tweetId, self.fileName), 0)


if __name__ == "__main__":
    unittest.main()
