import os
import telebot

# هنا نختبر هل GitHub يرسل البيانات فعلاً للكود
TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHANNEL = os.environ.get('CHANNEL_ID')

if TOKEN is None:
    print("❌ خطأ: لم يتم العثور على TELEGRAM_TOKEN في الإعدادات!")
if CHANNEL is None:
    print("❌ خطأ: لم يتم العثور على CHANNEL_ID في الإعدادات!")

bot = telebot.TeleBot(TOKEN)
import os
import telebot

TOKEN = os.environ.get('TELEGRAM_TOKEN')
ID = os.environ.get('CHANNEL_ID')

bot = telebot.TeleBot(TOKEN)

try:
    print(f"Checking connection to: {ID}")
    bot.send_message(ID, "اختبار الاتصال: البوت يعمل الآن! 🎉")
    print("Success!")
except Exception as e:
    print(f"Error detail: {e}")
