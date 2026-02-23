import os
import telebot

# جلب البيانات من الإعدادات
TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID')

bot = telebot.TeleBot(TOKEN)

def test_post():
    try:
        print(f"🔄 محاولة الإرسال إلى: {CHANNEL_ID}")
        bot.send_message(CHANNEL_ID, "🚀 رسالة تجريبية من محرك Visionary X\nإذا رأيت هذه الرسالة، فالاتصال سليم!")
        print("✅ تم الإرسال بنجاح! تفقد القناة الآن.")
    except Exception as e:
        print(f"❌ فشل الإرسال! السبب الحقيقي هو: {e}")

if __name__ == "__main__":
    test_post()
