import os
import telebot
import feedparser
import random
from bs4 import BeautifulSoup

# إعدادات الربط من GitHub Secrets 🗝️
TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID')
bot = telebot.TeleBot(TOKEN)

# قائمة المصادر التقنية 📡
RSS_SOURCES = [
    "https://www.aitnews.com/feed",
    "https://www.tech-wd.com/wd/feed"
]

def smart_format(text):
    # خريطة الوسوم لزيادة الانتشار 📈
    tags = {"ذكاء": "#ذكاء_اصطناعي", "آبل": "#آبل", "جوجل": "#جوجل", "تطبيق": "#تطبيق"}
    for word, tag in tags.items():
        text = text.replace(word, tag)
    return text + "\n\n#Visionary_X #تقنية"

def run_bot():
    # جلب أحدث خبر
    feed = feedparser.parse(random.choice(RSS_SOURCES))
    if not feed.entries: return
    
    entry = feed.entries[0]
    title = entry.title
    summary = BeautifulSoup(entry.summary, 'html.parser').get_text()[:200]
    
    # تنسيق الرسالة بالوسوم
    caption = smart_format(f"🚨 *خبر جديد:*\n\n{title}\n\n{summary}...")
    
    # إضافة زر الرابط
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("🔗 التفاصيل الكاملة", url=entry.link))
    
    # النشر
    bot.send_message(CHANNEL_ID, caption, parse_mode='Markdown', reply_markup=markup)
    print("✅ تم النشر بنجاح!")

if __name__ == "__main__":
    run_bot()
