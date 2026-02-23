import telebot
import os
from deep_translator import GoogleTranslator

# سحب التوكن من إعداداتك السرية
TOKEN = os.getenv('BOT_TOKEN')

if not TOKEN:
    print("فشل التشغيل: التوكن غير موجود في الإعدادات.")
else:
    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "مرحباً! أنا أعمل الآن تحت إدارة الذكاء الاصطناعي. أرسل أي نص وسأترجمه لك فوراً.")

    @bot.message_handler(func=lambda message: True)
    def auto_translate(message):
        try:
            # الترجمة التلقائية إلى العربية
            translated = GoogleTranslator(source='auto', target='ar').translate(message.text)
            bot.reply_to(message, f"الترجمة المعتمدة: \n\n {translated}")
        except Exception as e:
            bot.reply_to(message, "حدث خطأ أثناء المعالجة.")

    print("البوت في وضع التشغيل الذاتي...")
    bot.polling(non_stop=True)
