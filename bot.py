import telebot
import os

# التوكن المسجل في GitHub Secrets
TOKEN = os.getenv('BOT_TOKEN')
# ضع معرف حسابك (ID) هنا لكي تصلك الطلبات عليه (احصل عليه من بوت @userinfobot)
ADMIN_ID = "ضع_الآيدي_الخاص_بك_هنا" 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    help_text = (
        "👋 أهلاً بك في بوت الخدمات السريعة!\n\n"
        "💰 أنا هنا لمساعدتك في الحصول على خدماتك أو عرضها.\n"
        "لطلب خدمة (تصميم، برمجة، بيع حسابات، إلخ)، أرسل طلبك الآن.\n\n"
        "📢 ملاحظة: سيتم إرسال طلبك للإدارة فوراً وسنتواصل معك."
    )
    bot.reply_to(message, help_text)

@bot.message_handler(func=lambda message: True)
def forward_to_admin(message):
    # إرسال تأكيد للمستخدم
    bot.reply_to(message, "✅ تم استلام طلبك! سيقوم المدير بالتواصل معك قريباً.")
    
    # تحويل الطلب إليك (كأدمن)
    report = (
        "🆕 طلب جديد وصل!\n\n"
        f"👤 من: {message.from_user.first_name} (@{message.from_user.username})\n"
        f"🆔 آيدي: {message.from_user.id}\n"
        f"📝 الطلب: {message.text}"
    )
    bot.send_message(ADMIN_ID, report)

print("🚀 البوت يعمل الآن كمنصة خدمات...")
bot.infinity_polling()
