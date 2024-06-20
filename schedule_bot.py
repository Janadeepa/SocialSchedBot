# schedule_bot.py

import schedule
import time
from twitter_bot import TwitterBot
from instagram_bot import InstagramBot

def scheduled_twitter_post():
    bot = TwitterBot()
    bot.post_tweet("Scheduled tweet!")

def scheduled_instagram_post():
    bot = InstagramBot()
    bot.post_photo("path_to_your_photo.jpg", "Scheduled post!")

def scheduled_follow_users():
    twitter_bot = TwitterBot()
    instagram_bot = InstagramBot()
    twitter_bot.follow_users("Python")
    instagram_bot.follow_users("Python")

def scheduled_respond_to_mentions():
    twitter_bot = TwitterBot()
    instagram_bot = InstagramBot()
    twitter_bot.respond_to_mentions("Thanks for the mention!")
    instagram_bot.respond_to_mentions("Thanks for the mention!")

schedule.every().day.at("09:00").do(scheduled_twitter_post)
schedule.every().day.at("10:00").do(scheduled_instagram_post)
schedule.every().day.at("11:00").do(scheduled_follow_users)
schedule.every().day.at("12:00").do(scheduled_respond_to_mentions)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
