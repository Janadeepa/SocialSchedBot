# instagram_bot.py

from instabot import Bot
from config import INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD

class InstagramBot:
    def __init__(self):
        self.bot = Bot()
        self.bot.login(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)

    def post_photo(self, photo_path, caption):
        self.bot.upload_photo(photo_path, caption=caption)

    def follow_users(self, keywords):
        for user in self.bot.search_users(keywords):
            self.bot.follow(user['pk'])

    def respond_to_mentions(self, message):
        media_id = self.bot.get_last_user_medias(INSTAGRAM_USERNAME, 1)[0]
        comments = self.bot.get_media_comments(media_id)
        for comment in comments:
            if INSTAGRAM_USERNAME in comment['text']:
                self.bot.comment(media_id, f"@{comment['user']['username']} {message}")

if __name__ == "__main__":
    bot = InstagramBot()
    bot.post_photo("path_to_your_photo.jpg", "Hello World! This is an automated post.")
