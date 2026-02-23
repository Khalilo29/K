import os
import telebot
import feedparser
import requests
from bs4 import BeautifulSoup

# إعدادات الربط 🗝️
TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL = os.environ.get('CHANNEL_ID')
bot = telebot.TeleBot(TOKEN)

def get_latest_news():
    # استخدام رابط RSS لموقع تقني (الجزيرة نت - تكنولوجيا كمثال)
    feed_url = "https://www.aljazeera.net/xml/rss/all/dictator/72b15777-66a9-4676-905c-e69d7b93192a"
    feed = feedparser.parse(feed_url)
    
    if feed.entries:
        entry = feed.entries[0]
        title = entry.title
        link = entry.link
        summary = entry.summary
        
        # محاولة استخراج صورة من الخبر (اختياري)
        img_url = "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600" # صورة افتراضية
        
        return {
            "caption": f"📰 *خبر تقني جديد:*\n\n*{title}*\n\n{summary[:200]}...",
            "link": link,
            "image": img_url
        }
    return None

def run_visionary_auto_news():
    news = get_latest_news()
    if news:
        # إنشاء زر لفتح الخبر الأصلي
        markup = telebot.types.InlineKeyboardMarkup()
        btn_read = telebot.types.InlineKeyboardButton("🔗 قراءة الخبر كاملاً", url=news['link'])
        markup.add(btn_read)
        
        # إرسال الخبر للقناة
        bot.send_photo(
            CHANNEL, 
            news['image'], 
            caption=news['caption'], 
            parse_mode='Markdown',
            reply_markup=markup
        )

if __name__ == "__main__":
    try:
        run_visionary_auto_news()
        print("✅ تم جلب ونشر الخبر التلقائي بنجاح!")
    except Exception as e:
        print(f"❌ خطأ في النظام: {e}")
