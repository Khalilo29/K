import os
import telebot
from telebot import types
import random

# إعدادات الوصول 🗝️
TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL = os.environ.get('CHANNEL_ID')
bot = telebot.TeleBot(TOKEN)

# مخزن البيانات الاحترافي 🗄️
professional_content = [
    {
        "category": "AI Tool",
        "text": "🛠️ *أداة اليوم:* هل جربت استخدام ChatGPT لتحليل البيانات الضخمة؟ يوفر عليك ساعات من العمل اليدوي! 🤖",
        "img": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=500"
    },
    {
        "category": "Tech Fact",
        "text": "📱 *هل تعلم؟* أول حاسوب في العالم كان يزن أكثر من 27 طناً ويحتل غرفة كاملة! 💻",
        "img": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=500"
    },
    {
        "category": "Motivation",
        "text": "🌟 *إلهام:* أفضل طريقة للتنبؤ بالمستقبل هي أن تخترعه بنفسك. ابدأ اليوم! 🚀",
        "img": "https://images.unsplash.com/photo-1497032628192-86f99bcd76bc?w=500"
    }
]

def run_visionary_system():
    # اختيار محتوى عشوائي من المخزن
    post = random.choice(professional_content)
    
    # بناء لوحة الأزرار التفاعلية 🔘
    markup = types.InlineKeyboardMarkup()
    btn_share = types.InlineKeyboardButton("📤 مشاركة المنشور", switch_inline_query="انظر ماذا وجدت في Visionary_X!")
    btn_support = types.InlineKeyboardButton("💬 تواصل معنا", url="https://t.me/khalilodjawad")
    markup.add(btn_share, btn_support)
    
    # إرسال المنشور المنسق
    bot.send_photo(
        CHANNEL, 
        post['img'], 
        caption=post['text'], 
        parse_mode='Markdown',
        reply_markup=markup
    )

if __name__ == "__main__":
    try:
        run_visionary_system()
        print("✅ تم النشر الآلي بنجاح!")
    except Exception as e:
        print(f"❌ خطأ في النظام: {e}")
