# twitter_bot.py

import tweepy
from config import TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET

class TwitterBot:
    def __init__(self):
        auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
        auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
        self.api = tweepy.API(auth)

    def post_tweet(self, message):
        self.api.update_status(message)

    def follow_users(self, keywords):
        for tweet in tweepy.Cursor(self.api.search_tweets, q=keywords, lang="en").items(10):
            try:
                tweet.user.follow()
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

    def respond_to_mentions(self, message):
        mentions = self.api.mentions_timeline(count=5)
        for mention in mentions:
            self.api.update_status(f"@{mention.user.screen_name} {message}", in_reply_to_status_id=mention.id)

if __name__ == "__main__":
    bot = TwitterBot()
    bot.post_tweet("Hello World! This is an automated tweet.")
