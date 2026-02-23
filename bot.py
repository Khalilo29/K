import os
import telebot
import feedparser
import random
from bs4 import BeautifulSoup

# Configuration 🗝️
TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID')
bot = telebot.TeleBot(TOKEN)

# Top-tier English Tech Sources 📡
SOURCES = [
    "https://www.theverge.com/rss/index.xml",
    "https://www.engadget.com/rss.xml",
    "https://www.wired.com/feed/rss",
    "https://techcrunch.com/feed/",
    "https://www.cnet.com/rss/news/"
]

HISTORY_FILE = "published_urls.txt"

def get_image(entry):
    """Extracts the best quality image from the news entry 🖼️"""
    if 'links' in entry:
        for link in entry.links:
            if 'image' in link.get('type', ''): return link.href
    soup = BeautifulSoup(entry.summary if 'summary' in entry else "", 'html.parser')
    img = soup.find('img')
    return img['src'] if img else None

def run_english_visionary():
    # Load Memory
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f: published_urls = f.read().splitlines()
    else: published_urls = []

    # Pick a random source and fetch news
    feed = feedparser.parse(random.choice(SOURCES))
    
    for entry in feed.entries[:15]:
        if entry.link not in published_urls:
            title = entry.title
            img_url = get_image(entry)
            
            # Formatting the post in Professional English 🚀
            header = "🌐 <b>VISIONARY X | Global Tech Update</b>"
            caption = f"{header}\n\n🔥 <b>{title}</b>\n\n🔹 #TechNews #AI #Innovation\n📱 @Visionary_X"
            
            markup = telebot.types.InlineKeyboardMarkup()
            markup.row(telebot.types.InlineKeyboardButton("🔗 Read Full Article", url=entry.link))
            markup.row(telebot.types.InlineKeyboardButton("👍", callback_data="1"), 
                       telebot.types.InlineKeyboardButton("🔥", callback_data="2"),
                       telebot.types.InlineKeyboardButton("🚀", callback_data="3"))

            try:
                if img_url:
                    bot.send_photo(CHANNEL_ID, img_url, caption=caption, parse_mode='HTML', reply_markup=markup)
                else:
                    bot.send_message(CHANNEL_ID, caption, parse_mode='HTML', reply_markup=markup)
                
                # Save to memory
                with open(HISTORY_FILE, "a") as f: f.write(entry.link + "\n")
                print(f"✅ Successfully Published: {title}")
                return
            except Exception as e:
                print(f"❌ Error: {e}")
    print("💤 No new global updates in the last 5 minutes.")

if __name__ == "__main__":
    run_english_visionary()
