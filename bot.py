import os
import telebot
import feedparser
import random
import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

# الربط البرمجي 🗝️
TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID')
bot = telebot.TeleBot(TOKEN)

# مصادر الأنباء العالمية 📡
SOURCES = [
    "https://www.theverge.com/rss/index.xml",
    "https://techcrunch.com/feed/",
    "https://www.wired.com/feed/rss"
]

HISTORY_FILE = "published_urls.txt"

def translate_ar(text):
    try: return GoogleTranslator(source='en', target='ar').translate(text)
    except: return text

def get_crypto():
    try:
        data = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd").json()
        return f"📊 <b>تحديث الأسواق اللحظي</b>\n\n🪙 BTC: <b>${data['bitcoin']['usd']:,}</b>\n💎 ETH: <b>${data['ethereum']['usd']:,}</b>\n\n#Visionary_X #Crypto"
    except: return None

def run_pilot():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f: published = f.read().splitlines()
    else: published = []

    # 10% احتمال لنشر أسعار الكريبتو
    if random.random() < 0.1:
        msg = get_crypto()
        if msg: bot.send_message(CHANNEL_ID, msg, parse_mode='HTML'); return

    # جلب ونشر الأخبار التقنية
    feed = feedparser.parse(random.choice(SOURCES))
    for entry in feed.entries[:10]:
        if entry.link not in published:
            title = translate_ar(entry.title)
            caption = f"🌐 <b>تغطية حصرية | Visionary X</b>\n\n🔥 {title}\n\n#تقنية #أخبار_عالمية @Visionary_X"
            
            markup = telebot.types.InlineKeyboardMarkup()
            markup.row(telebot.types.InlineKeyboardButton("🔗 التفاصيل الكاملة", url=entry.link))
            
            try:
                bot.send_message(CHANNEL_ID, caption, parse_mode='HTML', reply_markup=markup)
                with open(HISTORY_FILE, "a") as f: f.write(entry.link + "\n")
                return
            except: pass

if __name__ == "__main__":
    run_pilot()
