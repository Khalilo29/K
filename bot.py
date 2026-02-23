import os
import telebot
from telebot import types
import random

# إعدادات الوصول الآمن 🗝️
TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL = os.environ.get('CHANNEL_ID')
bot = telebot.TeleBot(TOKEN)

# بنك المحتوى الذكي (نصوص + صور + تصنيفات) 🗄️
content_pool = [
    {
        "type": "AI",
        "text": "🤖 *عالم الذكاء الاصطناعي:* هل تعلم أن نماذج اللغة الكبيرة مثل GPT-4 يمكنها الآن مساعدتك في كتابة تطبيقات كاملة من الصفر؟ التقنية تتطور، فلا تتوقف عن التعلم!",
        "img": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600"
    },
    {
        "type": "Code",
        "text": "💻 *نصيحة برمجية:* كتابة كود نظيف (Clean Code) أهم من كتابة كود يعمل فقط. اجعل كودك قابلاً للقراءة لزملائك ولنفسك في المستقبل! 🛠️",
        "img": "https://images.unsplash.com/photo-1542831371-29b0f74f9713?w=600"
    },
    {
        "type": "Success",
        "text": "🌟 *فلسفة النجاح:* لا تنتظر الظروف المثالية لتجاوز العقبات، ابدأ بما تملك وأينما كنت. النجاح هو مجموع محاولات صغيرة تتكرر يومياً. 🚀",
        "img": "https://images.unsplash.com/photo-1497032628192-86f99bcd76bc?w=600"
    }
]

def deploy_professional_post():
    # اختيار عشوائي ذكي
    post = random.choice(content_pool)
    
    # إنشاء أزرار تفاعلية احترافية 🔘
    markup = types.InlineKeyboardMarkup()
    btn_share = types.InlineKeyboardButton("📤 مشاركة المعرفة", switch_inline_query="Visionary_X")
    btn_owner = types.InlineKeyboardButton("👨‍💻 المبرمج", url="mailto:Khalilodjawad@gmail.com")
    markup.add(btn_share, btn_owner)
    
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
        deploy_professional_post()
        print("✅ تم تنفيذ عملية النشر الآلي بنجاح!")
    except Exception as e:
        print(f"❌ حدث خطأ في النظام: {e}")
