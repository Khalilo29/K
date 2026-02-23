import telebot
import os
from deep_translator import GoogleTranslator

# قراءة التوكن من إعدادات GitHub الآمنة
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "تم تشغيل البوت بنجاح!")

bot.polling()
