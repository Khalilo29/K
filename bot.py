import telebot
import os
import time
from deep_translator import GoogleTranslator

# سحب التوكن من النظام (إعدادات GitHub Secrets)
TOKEN = os.getenv('BOT_TOKEN')

def run_bot():
    if not TOKEN:
        print("❌ خطأ إداري: التوكن مفقود من إعدادات Secrets!")
        return

    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "✅ تم التفعيل! هذا البوت يعمل الآن 24/24 تحت إشراف Gemini الإداري.")

    @bot.message_handler(func=lambda message: True)
    def handle_translation(message):
        try:
            # ترجمة ذكية تلقائية إلى العربية
            translated = GoogleTranslator(source='auto', target='ar').translate(message.text)
            bot.reply_to(message, f"🎯 الترجمة:\n\n{translated}")
        except Exception as e:
            print(f"⚠️ تنبيه: خطأ في معالجة النص: {e}")

    print("🚀 المدير: البوت انطلق في وضع التشغيل المستمر...")
    
    # حلقة تشغيل لا نهائية لمقاومة الانقطاع
    while True:
        try:
            bot.polling(none_stop=True, interval=0, timeout=40)
        except Exception as e:
            print(f"🔄 إعادة تشغيل تلقائية بعد انقطاع: {e}")
            time.sleep(5)

if __name__ == "__main__":
    run_bot()
