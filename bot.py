import telebot
import os

# التوكن المسجل في GitHub Secrets
TOKEN = os.getenv('BOT_TOKEN')
# الآيدي الخاص بك الذي أرسلته لي
ADMIN_ID = "6978631006" 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    help_text = (
        "👋 أهلاً بك في منصة الخدمات الموثوقة!\n\n"
        "💰 نحن نوفر لك خدمات (بيع حسابات، شحن ألعاب، خدمات برمجية).\n\n"
        "📩 لطلب أي خدمة أو للاستفسار عن الأسعار، أرسل رسالتك هنا مباشرة.\n\n"
        "✅ البوت يعمل 24/7 لاستلام طلباتكم."
    )
    bot.reply_to(message, help_text)

@bot.message_handler(func=lambda message: True)
def forward_to_admin(message):
    # إشعار للمستخدم بالاستلام
    bot.reply_to(message, "⏳ تم استلام طلبك بنجاح. المدير سيتواصل معك الآن.")
    
    # تحويل تفاصيل الطلب إليك مباشرة
    report = (
        "🆕 **طلب عمل جديد!**\n\n"
        f"👤 العميل: {message.from_user.first_name} (@{message.from_user.username})\n"
        f"🆔 الآيدي: {message.from_user.id}\n"
        f"📝 نص الطلب: {message.text}"
    )
    bot.send_message(ADMIN_ID, report)

print("🚀 البوت انطلق لتحقيق الأرباح...")
bot.infinity_polling()
