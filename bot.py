import os
import telebot
import feedparser
import random
from bs4 import BeautifulSoup

# جلب البيانات من الإعدادات 🗝️
TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID') # سيعمل الآن مع الرقم 6978631006
bot = telebot.TeleBot(TOKEN)

# المصادر التقنية الموثوقة 📡
RSS_SOURCES = ["https://www.aitnews.com/feed", "https://www.tech-wd.com/wd/feed"]

def get_image(entry):
    """استخراج الصورة الأصلية من الخبر 🖼️"""
    soup = BeautifulSoup(entry.summary, 'html.parser')
    img = soup.find('img')
    return img['src'] if img else None

def start_visionary_engine():
    try:
        # جلب خبر عشوائي
        source = random.choice(RSS_SOURCES)
        feed = feedparser.parse(source)
        if not feed.entries: return
        
        entry = feed.entries[0]
        title = entry.title
        link = entry.link
        img_url = get_image(entry)
        
        # تنسيق النص بأسلوب احترافي 🚀
        caption = f"🚨 <b>{title}</b>\n\n"
        caption += f"🌐 #تكنولوجيا #ذكاء_اصطناعي\n"
        caption += f"📱 #Visionary_X"

        # إضافة زر "إقرأ المزيد" 🔘
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("🔗 التفاصيل الكاملة", url=link))

        # عملية النشر
        if img_url:
            bot.send_photo(CHANNEL_ID, img_url, caption=caption, parse_mode='HTML', reply_markup=markup)
        else:
            bot.send_message(CHANNEL_ID, caption, parse_mode='HTML', reply_markup=markup)
            
        print("✅ مبروك! القناة استقبلت الخبر الأول بنجاح.")
        
    except Exception as e:
        print(f"❌ خطأ بسيط متبقي: {e}")

if __name__ == "__main__":
    start_visionary_engine()
