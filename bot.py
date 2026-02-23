import os
import telebot
import random

# جلب المفاتيح من الإعدادات
TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL = os.environ.get('CHANNEL_ID')

bot = telebot.TeleBot(TOKEN)

# قائمة المحتوى المتنوعة (المخزن الرقمي) 📚
messages = [
    "🚀 *رؤية اليوم:* النجاح ليس وجهة، بل هو رحلة مستمرة من التطوير.",
    "💡 *نصيحة تقنية:* تعلم المنطق البرمجي أهم من حفظ الأكواد.",
    "🌟 *Visionary X:* المستقبل ينتمي لأولئك الذين يؤمنون بجمال أحلامهم.",
    "🛠️ *قاعدة العمل:* الجودة تعني أن تؤدي العمل بشكل صحيح عندما لا ينظر إليك أحد.",
    "📖 *اقتباس:* العقل الذي يتوسع بفكرة جديدة لا يعود أبداً إلى أبعاده الأصلية.",
    "💻 *تطوير:* البرمجة هي فن حل المشكلات قبل أن تكون مجرد كتابة أسطر.",
    "🎨 *إبداع:* لا تنتظر الإلهام، ابحث عنه في التفاصيل الصغيرة حولك.",
    "🔋 *تحفيز:* طاقتك هي أغلى ما تملك، استثمرها فيما يبني مستقبلك."
]

def send_random_post():
    # اختيار رسالة عشوائية من القائمة
    content = random.choice(messages)
    # إرسال الرسالة باستخدام Markdown للتنسيق
    bot.send_message(CHANNEL, content, parse_mode='Markdown')

if __name__ == "__main__":
    if TOKEN and CHANNEL:
        send_random_post()
        print("✅ تم اختيار ونشر رسالة جديدة بنجاح!")
    else:
        print("❌ خطأ: تأكد من ضبط الإعدادات (Secrets) بشكل صحيح.")
import os
import telebot

# هنا نختبر هل GitHub يرسل البيانات فعلاً للكود
TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL = os.environ.get('CHANNEL_ID')

if TOKEN is None:
    print("❌ خطأ: لم يتم العثور على BOT_TOKEN في الإعدادات!")
if CHANNEL is None:
    print("❌ خطأ: لم يتم العثور على CHANNEL_ID في الإعدادات!")

bot = telebot.TeleBot(TOKEN)
import os
import telebot

TOKEN = os.environ.get('BOT_TOKEN')
ID = os.environ.get('CHANNEL_ID')

bot = telebot.TeleBot(TOKEN)

try:
    print(f"Checking connection to: {ID}")
    bot.send_message(ID, "اختبار الاتصال: البوت يعمل الآن! 🎉")
    print("Success!")
except Exception as e:
    print(f"Error detail: {e}")
