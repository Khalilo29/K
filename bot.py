import os
import telebot
import feedparser
import random
from bs4 import BeautifulSoup

# الإعدادات 🗝️
TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID')
bot = telebot.TeleBot(TOKEN)

# الذاكرة (ملف نصي يحفظ الروابط المنشورة)
HISTORY_FILE = "published_urls.txt"

def get_image(entry):
    soup = BeautifulSoup(entry.summary, 'html.parser')
    img = soup.find('img')
    return img['src'] if img else None

def run_visionary_safe():
    # 1. قراءة الروابط المنشورة سابقاً
    published_urls = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            published_urls = f.read().splitlines()

    # 2. جلب الأخبار من المصادر
    sources = ["https://www.aitnews.com/feed", "https://www.tech-wd.com/wd/feed"]
    feed = feedparser.parse(random.choice(sources))
    
    # 3. البحث عن خبر جديد لم يُنشر بعد
    target_entry = None
    for entry in feed.entries:
        if entry.link not in published_urls:
            target_entry = entry
            break
    
    if not target_entry:
        print("💤 لا توجد أخبار جديدة حالياً. تم نشر كل شيء بالفعل.")
        return

    # 4. تنسيق ونشر الخبر الجديد فقط
    img_url = get_image(target_entry)
    caption = f"⭐ <b>{target_entry.title}</b>\n\n🌐 #تكنولوجيا #أخبار\n📱 #Visionary_X"
    
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("🔗 إقرأ التفاصيل", url=target_entry.link))
    markup.row(telebot.types.InlineKeyboardButton("👍", callback_data="1"), 
               telebot.types.InlineKeyboardButton("🚀", callback_data="2"))

    try:
        if img_url:
            bot.send_photo(CHANNEL_ID, img_url, caption=caption, parse_mode='HTML', reply_markup=markup)
        else:
            bot.send_message(CHANNEL_ID, caption, parse_mode='HTML', reply_markup=markup)
        
        # 5. تحديث الذاكرة فوراً لمنع التكرار مستقبلاً
        with open(HISTORY_FILE, "a") as f:
            f.write(target_entry.link + "\n")
        print(f"✅ تم نشر خبر جديد وحفظه في الذاكرة: {target_entry.title}")
        
    except Exception as e:
        print(f"❌ خطأ: {e}")

if __name__ == "__main__":
    run_visionary_safe()
