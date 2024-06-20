# 🌟 SocialSchedBot

**SocialSchedBot** is a Python-based social media bot that automates posting, responding to mentions, and following users on Twitter and Instagram. It uses `Tweepy` for Twitter API interactions, `Instabot` for Instagram, and `schedule` for task scheduling.

## 🚀 Features

- 📅 Post scheduled content on Twitter and Instagram
- 💬 Respond to mentions on both platforms
- 🔍 Follow users based on specified keywords

## 🛠️ Tech Stack

- 🐍 Python
- 🐦 Tweepy (Twitter API)
- 📸 Instabot (Instagram)
- ⏰ Schedule

## 📁 Project Structure

```
SocialSchedBot/
│
├── twitter_bot.py
├── instagram_bot.py
├── schedule_bot.py
├── config.py
└── requirements.txt
```

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/SocialSchedBot.git
cd SocialSchedBot
```

### 2. Install Dependencies

Make sure you have Python installed. Then, install the required libraries:

```bash
pip install -r requirements.txt
```

### 3. Configure API Keys and Credentials

Update the `config.py` file with your Twitter and Instagram credentials:

```python
# config.py

TWITTER_API_KEY = 'your_twitter_api_key'
TWITTER_API_SECRET = 'your_twitter_api_secret'
TWITTER_ACCESS_TOKEN = 'your_twitter_access_token'
TWITTER_ACCESS_SECRET = 'your_twitter_access_secret'

INSTAGRAM_USERNAME = 'your_instagram_username'
INSTAGRAM_PASSWORD = 'your_instagram_password'
```

### 4. Running the Bot

You can run the bot by executing the `schedule_bot.py` script. This will start scheduling tasks for posting, responding to mentions, and following users.

```bash
python schedule_bot.py
```

## 📚 Usage

### 🐦 Twitter Bot

The `twitter_bot.py` script contains functions for:

- 📝 Posting tweets
- 👥 Following users based on keywords
- 💬 Responding to mentions

### 📸 Instagram Bot

The `instagram_bot.py` script contains functions for:

- 🖼️ Posting photos with captions
- 👥 Following users based on keywords
- 💬 Responding to mentions

### ⏰ Scheduling

The `schedule_bot.py` script schedules the tasks for posting, following users, and responding to mentions. It uses the `schedule` library to run these tasks at specified times.

## ✨ Customization

You can customize the scheduling times and tasks in the `schedule_bot.py` script. For example, to change the time for posting a tweet:

```python
schedule.every().day.at("09:00").do(scheduled_twitter_post)
```

Change `"09:00"` to your desired time.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.
