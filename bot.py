import telebot
import os

TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = "6978631006" 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "👋 أهلاً بك! أرسل طلبك (بيع/شراء) هنا وسيتواصل معك المدير فوراً.")

@bot.message_handler(func=lambda message: True)
def forward_to_admin(message):
    bot.reply_to(message, "⏳ تم استلام طلبك بنجاح.")
    bot.send_message(ADMIN_ID, f"🆕 طلب جديد:\n\n👤 العميل: {message.from_user.first_name}\n📝 الطلب: {message.text}")

bot.infinity_polling()
