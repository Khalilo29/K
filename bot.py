import os
import telebot
import feedparser
import random
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

# الإعدادات 🗝️
TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID')
bot = telebot.TeleBot(TOKEN)

# مصادر متنوعة لضمان وجود محتوى كل 5 دقائق 📡
SOURCES = {
    "AR": [
        "https://www.aitnews.com/feed", 
        "https://www.tech-wd.com/wd/feed",
        "https://ar.technologyreview.com/feed/"
    ],
    "EN": [
        "https://www.theverge.com/rss/index.xml", 
        "https://www.engadget.com/rss.xml",
        "https://www.wired.com/feed/rss"
    ]
}

HISTORY_FILE = "published_urls.txt"

def translate_content(text):
    try:
        return GoogleTranslator(source='en', target='ar').translate(text)
    except:
        return text

def get_image(entry):
    soup = BeautifulSoup(entry.summary if 'summary' in entry else "", 'html.parser')
    img = soup.find('img')
    if img: return img['src']
    if 'media_content' in entry: return entry.media_content[0]['url']
    return None

def run_visionary_autopilot():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f: published_urls = f.read().splitlines()
    else: published_urls = []

    # دمج المصادر والبحث عن خبر جديد
    lang_type = random.choice(["AR", "EN"])
    feed = feedparser.parse(random.choice(SOURCES[lang_type]))
    
    for entry in feed.entries[:15]:
        if entry.link not in published_urls:
            title = translate_content(entry.title) if lang_type == "EN" else entry.title
            img_url = get_image(entry)
            
            header = "🌍 <b>Visionary Global | خبر عالمي</b>" if lang_type == "EN" else "🔔 <b>Visionary News | خبر عاجل</b>"
            caption = f"{header}\n\n🔥 {title}\n\n🌐 #تكنولوجيا #الذكاء_الاصطناعي\n📱 @Visionary_X"
            
            markup = telebot.types.InlineKeyboardMarkup()
            markup.row(telebot.types.InlineKeyboardButton("🔗 تفاصيل الخبر", url=entry.link))
            markup.row(telebot.types.InlineKeyboardButton("👍", callback_data="1"), 
                       telebot.types.InlineKeyboardButton("🔥", callback_data="2"),
                       telebot.types.InlineKeyboardButton("🚀", callback_data="3"))

            try:
                if img_url:
                    bot.send_photo(CHANNEL_ID, img_url, caption=caption, parse_mode='HTML', reply_markup=markup)
                else:
                    bot.send_message(CHANNEL_ID, caption, parse_mode='HTML', reply_markup=markup)
                
                with open(HISTORY_FILE, "a") as f: f.write(entry.link + "\n")
                print(f"✅ تم النشر بنجاح: {title}")
                return
            except Exception as e:
                print(f"❌ خطأ: {e}")
    print("💤 لا توجد أخبار جديدة في هذه الخمس دقائق.")

if __name__ == "__main__":
    run_visionary_autopilot()
