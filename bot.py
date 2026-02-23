import os
import telebot
import feedparser
import random
import time
from bs4 import BeautifulSoup

TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID')
bot = telebot.TeleBot(TOKEN)

RSS_SOURCES = [
    "https://www.aitnews.com/feed", 
    "https://www.tech-wd.com/wd/feed"
]

HISTORY_FILE = "published_urls.txt"

def get_image(entry):
    soup = BeautifulSoup(entry.summary, 'html.parser')
    img = soup.find('img')
    return img['src'] if img else None

def run_smart_engine():
    # 1. تحميل الذاكرة
    published_urls = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            published_urls = f.read().splitlines()

    # 2. جلب الأخبار وتصفيتها
    all_entries = []
    for source in RSS_SOURCES:
        feed = feedparser.parse(source)
        all_entries.extend(feed.entries)
    
    # ترتيب الأخبار من الأحدث للأقدم
    all_entries.sort(key=lambda x: x.published_parsed, reverse=True)

    for entry in all_entries:
        # إذا لم يُنشر الخبر سابقاً
        if entry.link not in published_urls:
            img_url = get_image(entry)
            caption = f"🌟 <b>{entry.title}</b>\n\n🌐 #تكنولوجيا #أخبار\n📱 #Visionary_X"
            
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton("🔗 إقرأ التفاصيل", url=entry.link))
            markup.row(telebot.types.InlineKeyboardButton("👍", callback_data="1"), 
                       telebot.types.InlineKeyboardButton("🚀", callback_data="2"))

            try:
                if img_url:
                    bot.send_photo(CHANNEL_ID, img_url, caption=caption, parse_mode='HTML', reply_markup=markup)
                else:
                    bot.send_message(CHANNEL_ID, caption, parse_mode='HTML', reply_markup=markup)
                
                # 3. تحديث الذاكرة فوراً
                with open(HISTORY_FILE, "a") as f:
                    f.write(entry.link + "\n")
                
                print(f"✅ تم نشر خبر جديد وحصري: {entry.title}")
                return # توقف بعد نشر خبر واحد جديد
            except Exception as e:
                print(f"❌ خطأ: {e}")
    
    print("💤 لا يوجد أخبار جديدة حالياً، كل المحتوى تم نشره سابقاً.")

if __name__ == "__main__":
    run_smart_engine()
