import os
import telebot
from telebot import types
import random

# إعدادات الربط 🗝️
TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL = os.environ.get('CHANNEL_ID')
bot = telebot.TeleBot(TOKEN)

# بنك المحتوى الشامل (تخصصي + تفاعلي) 🗄️
content_pool = [
    {
        "category": "الذكاء الاصطناعي 🤖",
        "text": "💡 *مستقبل التقنية:* الذكاء الاصطناعي ليس مجرد أداة، بل هو شريك في الإبداع. هل بدأت باستخدامه في عملك اليومي؟",
        "img": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600"
    },
    {
        "category": "تطوير الذات 🚀",
        "text": "🌟 *رسالة اليوم:* الانضباط هو الجسر بين الأهداف والإنجاز. استمر في السعي، فالنتائج العظيمة تتطلب وقتاً.",
        "img": "https://images.unsplash.com/photo-1497032628192-86f99bcd76bc?w=600"
    },
    {
        "category": "أخبار التقنية 📱",
        "text": "💻 *معلومة رقمية:* لغات البرمجة تتطور باستمرار، لكن تعلم 'المنطق البرمجي' هو ما يجعلك مبرمجاً لا يقهر في أي لغة.",
        "img": "https://images.unsplash.com/photo-1542831371-29b0f74f9713?w=600"
    }
]

def run_visionary_system():
    # اختيار عشوائي للمنشور
    post = random.choice(content_pool)
    
    # بناء أزرار التفاعل 🔘
    markup = types.InlineKeyboardMarkup()
    btn_share = types.InlineKeyboardButton("📤 مشاركة المعرفة", switch_inline_query="Visionary_X")
    btn_contact = types.InlineKeyboardButton("👨‍💻 تواصل مع القائد", url="mailto:Khalilodjawad@gmail.com")
    markup.add(btn_share, btn_contact)
    
    # إرسال الصورة مع النص المنسق والأزرار
    caption = f"*{post['category']}*\n\n{post['text']}"
    bot.send_photo(
        CHANNEL, 
        post['img'], 
        caption=caption, 
        parse_mode='Markdown',
        reply_markup=markup
    )

if __name__ == "__main__":
    try:
        run_visionary_system()
        print("✅ تم تشغيل النظام الشامل بنجاح!")
    except Exception as e:
        print(f"❌ خطأ في النظام: {e}")
