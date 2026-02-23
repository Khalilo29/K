# كود معدل لضمان الوصول للدردشة 📡
CHANNEL_ID = os.environ.get('CHANNEL_ID') # يجب أن يكون @Visionary_X في GitHub Secrets

def publish_to_channel(caption, markup):
    try:
        bot.send_message(CHANNEL_ID, caption, parse_mode='Markdown', reply_markup=markup)
        print("✅ تم النشر في القناة بنجاح!")
    except Exception as e:
        print(f"❌ فشل النشر: {e}")
