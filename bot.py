import telebot
import os # مكتبة أساسية للتعامل مع النظام

# سيقوم الكود الآن بسحب التوكن من إعدادات GitHub التي أضفتها
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "تم الاتصال بنجاح! البوت يعمل الآن.")

bot.polling()
