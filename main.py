import telebot
from flask import Flask
import threading

BOT_TOKEN = "8259542088:AAEX7DdFDJ3n7CduRALxPeC4qVMkrfccpBc"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_cmd(message):
    bot.reply_to(message, "Hello! 👋 The bot is in test mode ✅")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, f"Ты написал: {message.text}")

# ---- Flask веб-сервер ----
app = Flask('')

@app.route('/')
def home():
    return "✅ Bot is running!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

# ---- Запуск бота ----
if __name__ == "__main__":
    print("Бот запущен...")
    keep_alive()
    bot.infinity_polling()
