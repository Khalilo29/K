import os
import telebot
import feedparser
import random
from bs4 import BeautifulSoup

# الإعدادات من GitHub Secrets 🗝️
TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID')
bot = telebot.TeleBot(TOKEN)

# مصادر الأخبار التقنية 📡
RSS_SOURCES = ["https://www.aitnews.com/feed", "https://www.tech-wd.com/wd/feed"]
HISTORY_FILE = "published_history.txt"

def get_image(entry):
    """استخراج الصورة الأصلية من الخبر 🖼️"""
    soup = BeautifulSoup(entry.summary, 'html.parser')
    img = soup.find('img')
    return img['src'] if img else None

def is_published(title):
    """التحقق مما إذا كان الخبر قد نُشر من قبل 🧠"""
    if not os.path.exists(HISTORY_FILE): return False
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        return title in f.read()

def save_to_history(title):
    """حفظ الخبر في الذاكرة لعدم التكرار ✅"""
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(title + "\n")

def run_visionary_ai_engine():
    try:
        source = random.choice(RSS_SOURCES)
        feed = feedparser.parse(source)
        if not feed.entries: return
        
        # البحث عن أول خبر لم يُنشر بعد
        new_entry = None
        for entry in feed.entries:
            if not is_published(entry.title):
                new_entry = entry
                break
        
        if not new_entry:
            print("🔍 لا توجد أخبار جديدة حالياً.. الذاكرة ممتلئة بالقديم.")
            return

        title = new_entry.title
        link = new_entry.link
        img_url = get_image(new_entry)
        
        # تنسيق الرسالة بأسلوب Visionary X 🚀
        caption = f"🔥 <b>{title}</b>\n\n"
        caption += f"🌐 #تكنولوجيا #ذكاء_اصطناعي\n"
        caption += f"📱 #Visionary_X"

        # إضافة أزرار التفاعل والأخبار 🔘
        markup = telebot.types.InlineKeyboardMarkup()
        btn_link = telebot.types.InlineKeyboardButton("🔗 إقرأ التفاصيل", url=link)
        btn_like = telebot.types.InlineKeyboardButton("👍", callback_data="like")
        btn_fire = telebot.types.InlineKeyboardButton("🔥", callback_data="fire")
        btn_wow = telebot.types.InlineKeyboardButton("🚀", callback_data="wow")
        
        markup.row(btn_link)
        markup.row(btn_like, btn_fire, btn_wow)

        # عملية النشر
        if img_url:
            bot.send_photo(CHANNEL_ID, img_url, caption=caption, parse_mode='HTML', reply_markup=markup)
        else:
            bot.send_message(CHANNEL_ID, caption, parse_mode='HTML', reply_markup=markup)
            
        save_to_history(title)
        print(f"✅ تم نشر الخبر الجديد بنجاح: {title}")
        
    except Exception as e:
        print(f"❌ خطأ تقني: {e}")

if __name__ == "__main__":
    run_visionary_ai_engine()
