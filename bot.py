import os
import telebot
import feedparser
import random
from bs4 import BeautifulSoup

# إعدادات البوت والقناة 🔑
TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID')
bot = telebot.TeleBot(TOKEN)

# قائمة المصادر الشاملة التي سنراقبها 📡
RSS_SOURCES = [
    "https://www.aitnews.com/feed",         # البوابة العربية للأخبار التقنية
    "https://www.tech-wd.com/wd/feed",      # عالم التقنية
    "https://www.aljazeera.net/xml/rss/all/dictator/72b15777-66a9-4676-905c-e69d7b93192a" # الجزيرة تقنية
]

def get_latest_news():
    all_news = []
    for url in RSS_SOURCES:
        feed = feedparser.parse(url)
        if feed.entries:
            # نأخذ أحدث خبر من كل مصدر
            all_news.append(feed.entries[0])
    
    # نختار خبراً واحداً عشوائياً لنشره الآن
    return random.choice(all_news) if all_news else None

def start_bot():
    news = get_latest_news()
    if news:
        # تنظيف الملخص من رموز HTML 🧹
        summary = BeautifulSoup(news.summary, 'html.parser').get_text()[:250] + "..."
        
        # تنسيق الرسالة
        message = f"📰 *{news.title}*\n\n{summary}"
        
        # إضافة زر "إقرأ المزيد" 🔘
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("🔗 إقرأ الخبر كاملاً", url=news.link))
        
        # إرسال الخبر للقناة
        bot.send_message(CHANNEL_ID, message, parse_mode='Markdown', reply_markup=markup)
        print("✅ تم نشر الخبر بنجاح!")

if __name__ == "__main__":
    start_bot()
# إضافة الوسوم تلقائياً لزيادة الانتشار 🏷️
hashtags = "\n\n#Visionary_X #تقنية #ذكاء_اصطناعي #أخبار_التقنية #تكنولوجيا"
caption += hashtags
# إضافة لمسة احترافية لزيادة الوصول 📈
hashtags = "\n\n#Visionary_X #تقنية #AI #أخبار_التكنولوجيا"
final_message = message + hashtags
