import os
import telebot

# جلب البيانات من Secrets
TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL = os.environ.get('CHANNEL_ID')

bot = telebot.TeleBot(TOKEN)

def test_connection():
    try:
        # محاولة إرسال رسالة بسيطة
        bot.send_message(CHANNEL, "🚀 تم الاتصال بنجاح! Visionary_X جاهزة للانطلاق.")
        print("✅ Message sent successfully!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_connection()
