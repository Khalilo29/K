import os
import telebot

TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL = os.environ.get('CHANNEL_ID')
bot = telebot.TeleBot(TOKEN)

def send_test():
    bot.send_message(CHANNEL, "🚀 تجربة نظام التشغيل التلقائي كل 5 دقائق بنجاح!")

if __name__ == "__main__":
    send_test()
