def publish_to_channel(caption, markup):
    try:
        # استخدام HTML بدلاً من Markdown لحل مشكلة الرموز الخاصة 🛠️
        bot.send_message(CHANNEL_ID, caption, parse_mode='HTML', reply_markup=markup)
        print("✅ تم النشر في القناة بنجاح!")
    except Exception as e:
        print(f"❌ حدث خطأ أثناء الإرسال: {e}")
