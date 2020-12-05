import telebot
import config


bot = telebot.TeleBot(config.TOKEN)
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Привет', 'Пока')

@bot.message_handler(commands=['start', 'go', 'help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Приветствую, Вы решили мне написать?', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, дорогой Рыжулькинс! Помнишь какая у Гогена любимая группа?')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока, дорогой Рыжулькинс! Всех тебе ништяков!')
    elif message.text.lower() == 'нирвана':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAANiX8rBH9xFQJxek_aiof8d76-7GHkAAtQIAAIItxkCBaNkOqPpyIoeBA')
    elif message.text.lower() == 'nirvana':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAANiX8rBH9xFQJxek_aiof8d76-7GHkAAtQIAAIItxkCBaNkOqPpyIoeBA')
    else:
        bot.send_message(message.chat.id, 'Простите, Рыжулькинс, а есть ещё варианты?')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBK1_Lyk4hPz5Nki7gu6EV3-IMqfK6AALWCAACCLcZAoU9GYC_TH6JHgQ')


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()

