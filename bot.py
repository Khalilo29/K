import os
import telebot
import random

# إعدادات الربط
TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL = os.environ.get('CHANNEL_ID')
bot = telebot.TeleBot(TOKEN)

# مخزن المحتوى المطور (نصوص مع روابط صور اختيارية)
content_pool = [
    {"text": "🚀 *رؤية اليوم:* النجاح ليس وجهة، بل هو رحلة مستمرة من التطوير.", "img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=500"},
    {"text": "💡 *نصيحة تقنية:* تعلم المنطق البرمجي أهم من حفظ الأكواد المجردة.", "img": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=500"},
    {"text": "🌟 *Visionary X:* المستقبل ينتمي لأولئك الذين يؤمنون بجمال أحلامهم.", "img": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=500"},
    {"text": "🛠️ *قاعدة العمل:* الجودة تعني أداء العمل بإتقان حتى في غياب الرقابة.", "img": "https://images.unsplash.com/photo-1499750310107-5fef28a66643?w=500"},
    {"text": "💻 *تطوير:* البرمجة هي فن حل المشكلات قبل كتابة الأسطر.", "img": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=500"}
]

def send_smart_post():
    item = random.choice(content_pool)
    # إرسال الصورة مع النص التوضيحي
    bot.send_photo(CHANNEL, item['img'], caption=item['text'], parse_mode='Markdown')

if __name__ == "__main__":
    if TOKEN and CHANNEL:
        send_smart_post()
        print("✅ تم نشر المنشور البصري بنجاح!")
