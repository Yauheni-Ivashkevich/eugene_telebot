import telebot
import config
from telebot import types


bot = telebot.TeleBot(config.TOKEN)
name = ""
surname = ""
age = 0


@bot.message_handler(commands=["start", "go", "help"])
def start_message(message):
    bot.send_message(message.chat.id, "Приветствую, дорогой друг, решил мне написать?")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text.lower() == "Привет":
        bot.reply_to(message, "Привет дорогой друг! Нажми пожалуйста /reg")
    elif message.text.lower() == "hi":
        bot.reply_to(message, "Hi again! Dear friend! Touch /reg you are welcome")
    elif message.text == "/reg":
        bot.send_message(message.from_user.id, "Давай познакомимся, друг! Как тебя зовут?")
        bot.register_next_step_handler(message, reg_name)
    else:
        bot.send_message(message.from_user.id, "Напиши /reg")
        bot.send_sticker(
            message.chat.id,
            "CAACAgIAAxkBAAIBK1_Lyk4hPz5Nki7gu6EV3-IMqfK6AALWCAACCLcZAoU9GYC_TH6JHgQ",
        )


def reg_name(message):  # получаем фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Какая у вас фамилия?")
    bot.register_next_step_handler(message, reg_surname)


def reg_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "Сколько вам лет?")
    bot.register_next_step_handler(message, reg_age)


def reg_age(message):
    global age
    # age = message.text
    while age == 0:  # проверяем что возраст изменился
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, "Вводите цифрами, пожалуйста!")

    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    key_yes = types.InlineKeyboardButton(text="Да", callback_data="yes")  # кнопка «Да»
    keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
    key_no = types.InlineKeyboardButton(text="Нет", callback_data="no")
    keyboard.add(key_no)
    question = "Тебе " + str(age) + " лет? И тебя зовут: " + name + " " + surname + "?"
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if (call.data == "yes"):  # call.data это callback_data, которую мы указали при объявлении кнопки
        bot.send_message(call.message.chat.id, "Приятно познакомиться! ")  # код сохранения данных, или их обработки
        bot.send_message(call.message.chat.id, "Безусловно, жизнь есть жизнь, и в ней всему есть место!")
        bot.send_message(call.message.chat.id, "Но, не забывайте про нас! ")
        bot.send_message(call.message.chat.id, "Всего хорошего! : )")
        bot.send_sticker(call.message.chat.id, "CAACAgIAAxkBAANiX8rBH9xFQJxek_aiof8d76-7GHkAAtQIAAIItxkCBaNkOqPpyIoeBA",)
    elif call.data == "no":
        bot.send_message(call.message.chat.id, "Попробуем еще раз!")
        bot.send_message(
            call.message.chat.id, "Привет! Давай познакомимся! Как тебя зовут?"
        )
        bot.register_next_step_handler(call.message, reg_name)
        bot.send_sticker(
            call.message.chat.id,
            "AAMCAgADGQEAAgTcX9KA5b5MxgGjDTO-fR-ojV7LH5AAApkIAAIItxkCU4nZ3lcmuhMTqjkPAAQBAAdtAAO8NgACHgQ",
        )


# @bot.message_handler(content_types=['sticker'])
# def sticker_id(message):
#     print(message)

bot.polling()
