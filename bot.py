import telebot
from deep_translator import GoogleTranslator

# هنا تضع التوكن الخاص بالبوت
bot = telebot.TeleBot("YOUR_BOT_TOKEN_HERE")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! أنا بوت الترجمة، أرسل أي نص لترجمته.")

# ... باقي الكود الخاص بك
