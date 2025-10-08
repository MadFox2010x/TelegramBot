from flask import Flask
import telebot
import os

# Токен бота (вставь свой)
BOT_TOKEN = "8259542088:AAEX7DdFDJ3n7CduRALxPeC4qVMkrfccpBc"

bot = telebot.TeleBot(BOT_TOKEN)

# Flask для Render (чтобы пингер мог будить)
app = Flask(__name__)

@app.route('/')
def home():
    return "Бот запущен и работает!"

# Команда /start
@bot.message_handler(commands=['start'])
def start_cmd(message):
    bot.reply_to(message, "Привет👋! Бот находится в тестовом режиме")

if __name__ == "__main__":
    # Запускаем бота в отдельном потоке
    import threading

    def run_bot():
        bot.polling(none_stop=True, interval=0)

    threading.Thread(target=run_bot).start()

    # Запускаем Flask-сервер для Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
