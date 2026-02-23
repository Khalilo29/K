import os
import telebot
import feedparser
import random
import re
from bs4 import BeautifulSoup

# إعدادات الربط 🗝️
TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL = os.environ.get('CHANNEL_ID')
bot = telebot.TeleBot(TOKEN)

# قائمة المصادر التقنية 📡
RSS_SOURCES = ["https://www.aitnews.com/feed", "https://www.tech-wd.com/wd/feed"]

def smart_format(text):
    # تحويل الكلمات الهامة إلى وسوم لزيادة المشاهدات 🏷️
    tags_map = {
        "الذكاء الاصطناعي": "#الذكاء_الاصطناعي",
        "تكنولوجيا": "#تكنولوجيا",
        "آبل": "#آبل",
        "جوجل": "#جوجل",
        "تطبيق": "#تطبيق"
    }
    for word, tag in tags_map.items():
        text = text.replace(word, tag)
    return text

def run_visionary_engine():
    # جلب خبر عشوائي من المصادر
    source = random.choice(RSS_SOURCES)
    feed = feedparser.parse(source)
    if not feed.entries: return
    
    entry = feed.entries[0]
    clean_desc = BeautifulSoup(entry.summary, 'html.parser').get_text()[:200]
    
    # تنسيق الرسالة النهائية
    final_text = f"🚨 *جديد التقنية:*\n\n{entry.title}\n\n{clean_desc}..."
    final_text = smart_format(final_text) + "\n\n#Visionary_X"

    # إضافة الأزرار 🔘
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("🔗 إقرأ الخبر كاملاً", url=entry.link))

    # النشر الفوري
    bot.send_message(CHANNEL, final_text, parse_mode='Markdown', reply_markup=markup)
    print("✅ تم النشر بنجاح مع الوسوم الذكية!")

if __name__ == "__main__":
    run_visionary_engine()
