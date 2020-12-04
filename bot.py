import telebot
import config


bot = telebot.TeleBot(config.TOKEN)
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Привет', 'Пока')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'нирвана':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAANiX8rBH9xFQJxek_aiof8d76-7GHkAAtQIAAIItxkCBaNkOqPpyIoeBA')
    elif message.text.lower() == 'nirvana':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAANiX8rBH9xFQJxek_aiof8d76-7GHkAAtQIAAIItxkCBaNkOqPpyIoeBA')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()
