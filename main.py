import telebot
import requests
bot = telebot.TeleBot('токен')
API = 'f2eee143cf2308e9ddedee40ad42accb'
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = res.json()
    bot.reply_to(message, f'Погода: {data["main"]["temp"]}')

bot.polling(none_stop=True)

