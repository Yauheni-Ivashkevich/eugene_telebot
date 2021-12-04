import os
from dotenv import load_dotenv
import telebot
from pyowm import OWM

load_dotenv()

TOKEN = os.getenv("TOKEN")
API_KEY = os.getenv("API_KEY")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/weather':
        bot.send_message(message.from_user.id, 'Введите название города')
        bot.register_next_step_handler(message, get_weather)
    else:
        bot.send_message(message.from_user.id, "Напиши /weather чтобы узнать погоду")


# Обработчик команд '/start' и '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    pass


# Обработчик для документов и аудиофайлов
@bot.message_handler(content_types=['document', 'audio'])
def handle_document_audio(message):
    pass


def get_weather(message):
    city = message.text
    try:
        w = weather(city)
        bot.send_message(message.from_user.id, f'В городе {city} сейчас {round(w[0]["temp"])} градусов,'
                                               f' чувствуется как {round(w[0]["feels_like"])} градусов')
        bot.send_message(message.from_user.id, w[1])
        bot.send_message(message.from_user.id, 'Доброго времен суток! Введите название города')
        bot.register_next_step_handler(message, get_weather)
    except Exception:
        bot.send_message(message.from_user.id, 'Упс... такого города нет в базе, попробуйте ещё раз')
        bot.send_message(message.from_user.id, 'Введите название города')
        bot.register_next_step_handler(message, get_weather)


def get_location(lat, lon):
    url = f"https://yandex.ru/pogoda/maps/nowcast?lat={lat}&lon={lon}&via=hnav&le_Lighting=1"
    return url


def weather(city: str):
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    weather = observation.weather
    location = get_location(observation.location.lat, observation.location.lon)
    temperature = weather.temperature("celsius")
    return temperature, location


bot.polling(none_stop=True, interval=0)
