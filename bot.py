import telebot
import random
import time
import os

# إعداد البيانات من البيئة الأمنية (Secrets)
API_KEY = os.getenv('BOT_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')

bot = telebot.TeleBot(API_KEY)

def send_post():
    # قراءة المنشورات من ملف content.txt
    with open('content.txt', 'r', encoding='utf-8') as f:
        posts = f.readlines()
    
    # اختيار منشور عشوائي
    post = random.choice(posts).strip()
    
    # إرسال المنشور للقناة
    if post:
        bot.send_message(CHANNEL_ID, post)
        print(f"تم نشر: {post}")

if __name__ == "__main__":
    send_post()
