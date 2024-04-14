import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('7072795724:AAEG8Ii8WZMC6--ZjRsFZ56gZcfbzhmAkS8')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Удалить фото', callback_data = 'delete')
    markup.row(btn1)
    bot.reply_to(message, 'Какое красивое фото!', reply_markup = markup)

@bot.callback_query_handler(func = lambda callback: True)
def callback_vessage(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)

@bot.message_handler(commands=['message'])
def message(message):
    bot.send_message(message.chat.id, message)

@bot.message_handler(commands=['start', 'hello'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Привет')
    btn2 = types.KeyboardButton('Мой id')
    markup.row(btn1, btn2)
    btn3 = types.KeyboardButton('help')
    btn4 = types.KeyboardButton('Перейти на сайт')
    markup.row(btn3, btn4)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}. Я бот, который поможет тебе!P.S. Яман лох', reply_markup = markup)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Оооооо, вы из Англии?')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}. Я бот, который поможет тебе!P.S. Яман лох')
    elif message.text.lower() == 'мой id':
        bot.reply_to(message, f'ID{ message.from_user.id}')
    elif message.text.lower() == 'help':
        bot.send_message(message.chat.id, 'Оооооо, вы из Англии?')
    elif message.text.lower() == 'перейти на сайт':
        bot.send_message(message.chat.id, 'Сайт пока не добавлен :(')

bot.polling(none_stop=True, timeout=None)