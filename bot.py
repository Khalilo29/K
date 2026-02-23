import telebot
import os
import time
from deep_translator import GoogleTranslator

# استدعاء التوكن من إعدادات GitHub الآمنة
TOKEN = os.getenv('BOT_TOKEN')

def run_bot():
    if not TOKEN:
        print("خطأ: التوكن مفقود!")
        return

    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "✅ البوت يعمل الآن 24/24 تحت إشراف Gemini.")

    @bot.message_handler(func=lambda message: True)
    def handle_message(message):
        try:
            # ترجمة تلقائية ذكية
            translated = GoogleTranslator(source='auto', target='ar').translate(message.text)
            bot.reply_to(message, f"📍 الترجمة:\n\n{translated}")
        except Exception as e:
            print(f"خطأ بسيط في الترجمة: {e}")

    print("🚀 البوت انطلق الآن...")
    
    # ميزة التشغيل اللانهائي ومقاومة الانقطاع
    while True:
        try:
            bot.polling(none_stop=True, interval=0, timeout=20)
        except Exception as e:
            print(f"حدث انقطاع، أعيد التشغيل خلال 5 ثواني... {e}")
            time.sleep(5)

if __name__ == "__main__":
    run_bot()
