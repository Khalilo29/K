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
