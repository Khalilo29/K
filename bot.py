import os
import telebot
import feedparser
import random
from bs4 import BeautifulSoup

# إعدادات الربط 🗝️
TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID')
bot = telebot.TeleBot(TOKEN)

# قائمة المصادر 📡
RSS_SOURCES = ["https://www.aitnews.com/feed", "https://www.tech-wd.com/wd/feed"]

def smart_format_html(text):
    # تحويل الكلمات الهامة لوسوم ذكية 🏷️
    tags = {"ذكاء": "#ذكاء_اصطناعي", "آبل": "#آبل", "جوجل": "#جوجل", "تطبيق": "#تطبيق"}
    for word, tag in tags.items():
        text = text.replace(word, tag)
    # إضافة وسم القناة الثابت
    return text + "\n\n<b>#Visionary_X #تقنية</b>"

def run_bot():
    source = random.choice(RSS_SOURCES)
    feed = feedparser.parse(source)
    if not feed.entries: return
    
    entry = feed.entries[0]
    title = entry.title
    # تنظيف النص من أي أكواد HTML زائدة
    summary = BeautifulSoup(entry.summary, 'html.parser').get_text()[:200]
    
    # بناء الرسالة باستخدام تنسيق HTML 🏗️
    caption = f"🚨 <b>خبر جديد:</b>\n\n{title}\n\n{summary}..."
    caption = smart_format_html(caption)
    
    # إضافة الأزرار 🔘
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("🔗 التفاصيل الكاملة", url=entry.link))
    
    # الإرسال النهائي باستخدام HTML لحل مشكلة الرموز ✅
    try:
        bot.send_message(CHANNEL_ID, caption, parse_mode='HTML', reply_markup=markup)
        print("✅ تم النشر في القناة بنجاح!")
    except Exception as e:
        print(f"❌ خطأ في الإرسال: {e}")

if __name__ == "__main__":
    run_bot()
