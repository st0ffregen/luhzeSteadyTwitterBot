#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import tweepy
import os
import random
import string
from bot import updateStatus
from dotenv import load_dotenv

# test data
statusArray = [
    "testing tweet",
    "testing status",
    "testing update",
    "testing steady application",
    "testing new app",
    "testing with tweepy",
    "testing new application"
]

# example stati
# natuerlich nicht ganz best practice weil die aus production sind und es durchaus sein kann, dass sie z.b. noch geliked werden
normalStatusWithNoLikes = "1328725113278238721"
normalStatusWithLikesAndRetweets = "1340190140539555842"


load_dotenv()


class TestBot(unittest.TestCase):

    fileName = os.environ['ID_FILE']
    api = None

    @classmethod
    def setUpClass(cls) -> None:
        auth = tweepy.OAuthHandler(os.environ['TWITTER_API_KEY_TESTING'], os.environ['TWITTER_API_SECRET_KEY_TESTING'])
        auth.set_access_token(os.environ['TWITTER_ACCESS_TOKEN_TESTING'],
                              os.environ['TWITTER_ACCESS_TOKEN_SECRET_TESTING'])
        cls.api = tweepy.API(auth)
        # generate random string to append to statusArray
        letters = string.ascii_lowercase
        # edit testing array
        for i in range(0, len(statusArray)):
            resultStr = ''.join(random.choice(letters) for i in range(10))
            statusArray[i] = statusArray[i] + " " + resultStr

    def test_init_api(self):
        self.assertIsNotNone(updateStatus.initApi())

    def test_update_and_delete_status(self):
        tweetId = updateStatus.updateStatus(TestBot.api, self.fileName, statusArray, random.randint(0, 5))
        self.assertIsInstance(tweetId, str)
        self.assertEqual(updateStatus.deleteStatus(TestBot.api, tweetId, self.fileName), 0)

    def test_check_and_do_action(self):
        self.assertEqual(updateStatus.writeToFile(self.fileName, "update"), 0)
        self.assertEqual(updateStatus.checkAndDoAction(TestBot.api, self.fileName), 0)
        self.assertEqual(updateStatus.checkAndDoAction(TestBot.api, self.fileName), 0)

    def test_check_likes(self):
        self.assertTrue(updateStatus.checkIfTweetShouldBeDeleted(TestBot.api, normalStatusWithNoLikes))
        self.assertFalse(updateStatus.checkIfTweetShouldBeDeleted(TestBot.api, normalStatusWithLikesAndRetweets))


if __name__ == "__main__":
    unittest.main()
