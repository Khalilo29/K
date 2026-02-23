import os
import telebot
import feedparser
import random
import requests
from bs4 import BeautifulSoup

# Configuration 🗝️
TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID')
bot = telebot.TeleBot(TOKEN)

SOURCES = [
    "https://www.theverge.com/rss/index.xml",
    "https://techcrunch.com/feed/",
    "https://www.engadget.com/rss.xml"
]

HISTORY_FILE = "published_urls.txt"

def get_crypto_prices():
    """Fetches live BTC and ETH prices 💰"""
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
        data = requests.get(url).json()
        btc = data['bitcoin']['usd']
        eth = data['ethereum']['usd']
        return f"📊 <b>Market Update</b>\n\n🪙 BTC: <b>${btc:,}</b>\n💎 ETH: <b>${eth:,}</b>\n\n#Crypto #Bitcoin #ETH"
    except:
        return None

def get_image(entry):
    soup = BeautifulSoup(entry.summary if 'summary' in entry else "", 'html.parser')
    img = soup.find('img')
    return img['src'] if img else None

def run_visionary_pro():
    # 1. Load Memory
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f: published_urls = f.read().splitlines()
    else: published_urls = []

    # 2. Decide: Post Crypto or News?
    # (Optional: Only post crypto once an hour or randomly)
    if random.random() < 0.1:  # 10% chance to post crypto update every 5 mins
        crypto_update = get_crypto_prices()
        if crypto_update:
            bot.send_message(CHANNEL_ID, crypto_update, parse_mode='HTML')
            return

    # 3. Post News
    feed = feedparser.parse(random.choice(SOURCES))
    for entry in feed.entries[:10]:
        if entry.link not in published_urls:
            title = entry.title
            img_url = get_image(entry)
            caption = f"🌐 <b>VISIONARY X | Global Update</b>\n\n🔥 <b>{title}</b>\n\n#Tech #Innovation @Visionary_X"
            
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton("🔗 Full Story", url=entry.link))

            try:
                if img_url:
                    bot.send_photo(CHANNEL_ID, img_url, caption=caption, parse_mode='HTML', reply_markup=markup)
                else:
                    bot.send_message(CHANNEL_ID, caption, parse_mode='HTML', reply_markup=markup)
                
                with open(HISTORY_FILE, "a") as f: f.write(entry.link + "\n")
                return
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    run_visionary_pro()
