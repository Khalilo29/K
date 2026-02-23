import os
import telebot
import feedparser
import random
import re
from bs4 import BeautifulSoup

# إعدادات الوصول من GitHub Secrets 🗝️
TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID')
bot = telebot.TeleBot(TOKEN)

# قائمة المصادر التقنية الموثوقة 📡
RSS_SOURCES = [
    "https://www.aitnews.com/feed",
    "https://www.tech-wd.com/wd/feed"
]

def get_smart_tags(text):
    """تحليل النص وإضافة وسوم لزيادة المشاهدات 📈"""
    mapping = {
        "ذكاء": "#الذكاء_الاصطناعي #AI",
        "آبل": "#آبل #Apple",
        "جوجل": "#جوجل #Google",
        "هاتف": "#هواتف #Tech",
        "تطبيق": "#تطبيقات"
    }
    found_tags = []
    for key, tag in mapping.items():
        if key in text:
            found_tags.append(tag)
    
    base_tags = "#Visionary_X #تقنية #تكنولوجيا"
    return base_tags + " " + " ".join(found_tags)

def run_visionary_bot():
    # اختيار مصدر عشوائي لجلب الخبر
    source = random.choice(RSS_SOURCES)
    feed = feedparser.parse(source)
    
    if not feed.entries:
        print("⚠️ لم يتم العثور على أخبار جديدة.")
        return
    
    entry = feed.entries[0]
    title = entry.title
    # تنظيف الملخص من أي وسوم HTML قديمة
    summary = BeautifulSoup(entry.summary, 'html.parser').get_text()[:250]
    
    # بناء الرسالة بتنسيق HTML لضمان الاستقرار 🏗️
    tags = get_smart_tags(title + summary)
    caption = f"🚨 <b>{title}</b>\n\n{summary}...\n\n{tags}"
    
    # إضافة زر تفاعلي 🔘
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("🔗 إقرأ الخبر كاملاً", url=entry.link))
    
    try:
        # الإرسال النهائي
        bot.send_message(CHANNEL_ID, caption, parse_mode='HTML', reply_markup=markup)
        print("✅ تم النشر بنجاح مع الوسوم الذكية!")
    except Exception as e:
        print(f"❌ فشل الإرسال: {e}")

if __name__ == "__main__":
    run_visionary_bot()
