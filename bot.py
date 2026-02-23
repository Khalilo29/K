import telebot
import os
from deep_translator import GoogleTranslator

# سحب التوكن من النظام (الذي سنضبطه في إعدادات GitHub)
TOKEN = os.getenv('BOT_TOKEN')

if not TOKEN:
    print("خطأ: لم يتم العثور على التوكن!")
else:
    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "أهلاً بك! أنا بوت الترجمة. أرسل نصاً للترجمة.")

    @bot.message_handler(func=lambda message: True)
    def translate_message(message):
        # مثال لترجمة النص إلى العربية
        translated = GoogleTranslator(source='auto', target='ar').translate(message.text)
        bot.reply_to(message, translated)

    print("البوت يعمل الآن...")
    bot.polling()
