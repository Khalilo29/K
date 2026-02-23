import os
import telebot
import feedparser
import random
from bs4 import BeautifulSoup

# الإعدادات 🗝️
TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID')
bot = telebot.TeleBot(TOKEN)

# قائمة مصادر موسعة لضمان التنوع 📡
RSS_SOURCES = [
    "https://www.aitnews.com/feed", 
    "https://www.tech-wd.com/wd/feed",
    "https://ar.technologyreview.com/feed/"
]

HISTORY_FILE = "published_urls.txt"

def get_image(entry):
    """استخراج الصورة بأكثر من طريقة لضمان ظهورها 🖼️"""
    soup = BeautifulSoup(entry.summary, 'html.parser')
    img = soup.find('img')
    if img: return img['src']
    if 'media_content' in entry: return entry.media_content[0]['url']
    return None

def run_visionary_ai():
    # تحميل الروابط القديمة لمنع التكرار
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            published_urls = f.read().splitlines()
    else:
        published_urls = []

    # اختيار مصدر عشوائي
    random.shuffle(RSS_SOURCES)
    for source in RSS_SOURCES:
        feed = feedparser.parse(source)
        for entry in feed.entries[:5]: # فحص آخر 5 أخبار
            if entry.link not in published_urls:
                # نشر الخبر الجديد
                img_url = get_image(entry)
                caption = f"🔥 <b>{entry.title}</b>\n\n🌐 #تكنولوجيا #ذكاء_اصطناعي\n📱 #Visionary_X"
                
                markup = telebot.types.InlineKeyboardMarkup()
                markup.add(telebot.types.InlineKeyboardButton("🔗 إقرأ التفاصيل", url=entry.link))
                markup.add(telebot.types.InlineKeyboardButton("👍", callback_data="1"), 
                           telebot.types.InlineKeyboardButton("🚀", callback_data="2"))

                try:
                    if img_url:
                        bot.send_photo(CHANNEL_ID, img_url, caption=caption, parse_mode='HTML', reply_markup=markup)
                    else:
                        bot.send_message(CHANNEL_ID, caption, parse_mode='HTML', reply_markup=markup)
                    
                    # حفظ الرابط في الذاكرة
                    with open(HISTORY_FILE, "a") as f:
                        f.write(entry.link + "\n")
                    print(f"✅ نُشر بنجاح: {entry.title}")
                    return # إنهاء البرنامج بعد نشر خبر واحد بنجاح
                except Exception as e:
                    print(f"❌ خطأ: {e}")
    print("💤 لا يوجد محتوى جديد حالياً.")

if __name__ == "__main__":
    run_visionary_ai()
