import os
import telebot
import feedparser
import random
from bs4 import BeautifulSoup

# الإعدادات الأساسية 🗝️
TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID')
bot = telebot.TeleBot(TOKEN)

# قائمة المصادر 📡
RSS_SOURCES = ["https://www.aitnews.com/feed", "https://www.tech-wd.com/wd/feed"]

def get_image(entry):
    """استخراج رابط الصورة من الخبر 🖼️"""
    if 'links' in entry:
        for link in entry.links:
            if 'image' in link.get('type', ''): return link.href
    soup = BeautifulSoup(entry.summary, 'html.parser')
    img = soup.find('img')
    return img['src'] if img else None

def run_visionary_pro():
    feed = feedparser.parse(random.choice(RSS_SOURCES))
    if not feed.entries: return
    
    entry = feed.entries[0]
    title = entry.title
    link = entry.link
    img_url = get_image(entry)
    
    # تنسيق النص بأسلوب Visionary X 🚀
    caption = f"🚨 <b>{title}</b>\n\n"
    caption += f"🌐 #تكنولوجيا #الذكاء_الاصطناعي\n\n"
    caption += f"📱 #Visionary_X"

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("🔗 إقرأ التفاصيل", url=link))

    try:
        if img_url:
            bot.send_photo(CHANNEL_ID, img_url, caption=caption, parse_mode='HTML', reply_markup=markup)
        else:
            bot.send_message(CHANNEL_ID, caption, parse_mode='HTML', reply_markup=markup)
        print("✅ تم النشر بنجاح!")
    except Exception as e:
        print(f"❌ خطأ: {e}")

if __name__ == "__main__":
    run_visionary_pro()
