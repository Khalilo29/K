import os
import telebot
import feedparser
import random
from bs4 import BeautifulSoup

# الإعدادات من GitHub Secrets 🗝️
TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID') # الرقم الذي حصلت عليه 8571223481
bot = telebot.TeleBot(TOKEN)

# مصادر الأخبار 📡
RSS_SOURCES = ["https://www.aitnews.com/feed", "https://www.tech-wd.com/wd/feed"]

def get_image(entry):
    """استخراج الصورة من الخبر"""
    soup = BeautifulSoup(entry.summary, 'html.parser')
    img = soup.find('img')
    return img['src'] if img else None

def run_visionary_final():
    try:
        feed = feedparser.parse(random.choice(RSS_SOURCES))
        if not feed.entries: return
        
        entry = feed.entries[0]
        img_url = get_image(entry)
        
        # تنسيق الرسالة بأسلوب Visionary X 🚀
        caption = f"🚨 <b>{entry.title}</b>\n\n"
        caption += f"🌐 #تكنولوجيا #ذكاء_اصطناعي\n"
        caption += f"📱 #Visionary_X"

        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("🔗 إقرأ التفاصيل", url=entry.link))

        if img_url:
            bot.send_photo(CHANNEL_ID, img_url, caption=caption, parse_mode='HTML', reply_markup=markup)
        else:
            bot.send_message(CHANNEL_ID, caption, parse_mode='HTML', reply_markup=markup)
            
        print("✅ مبروك! تم النشر بنجاح.")
        
    except Exception as e:
        print(f"❌ خطأ في الإرسال: {e}")
        print("تأكد أن البوت بدأ محادثة مع الوجهة أو أنه مسؤول في القناة.")

if __name__ == "__main__":
    run_visionary_final()
