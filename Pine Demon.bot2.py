import telebot
from telebot import types

bot = telebot.TeleBot('6391644151:AAEKqbNd6ttZYVpOv_QxApzXOdeVQVMMX7E')

@bot.message_handler(commands=['home'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Поздороваться")
    btn2 = types.KeyboardButton("Домашка?")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text='Привет, {0.first_name}, партия "Широкий Карамыш" встречает тебя!'.format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Поздороваться"):
        bot.send_message(message.chat.id, text="Привет,а  зачем я это добавил?, а Миша?")
    elif(message.text == "Домашка?"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Задания?")
        btn2 = types.KeyboardButton("Расписание?")
        back = types.KeyboardButton("В главное меню?")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Что хочешь узнать?", reply_markup=markup)
    
    elif(message.text == "Задания?"):
        bot.send_message(message.chat.id,"(https://t.me/c/1813662612/6748 это русский язык, делаем только тест) (Физика параграф 19, читать, упр. 19) (Алгебра Упр 249, 250) (https://t.me/homashkabot/3 Литература) (https://t.me/homashkabot/4 Английский)")
    
    elif (message.text == "Расписание?"):
        bot.send_message(message.chat.id, text="https://sun122-2.userapi.com/impg/PTJIVAGO751leUmzY7CJ2UCnApbv8l0JpNWhsg/tJx-yLmXerc.jpg?size=1280x720&quality=95&sign=fdfc1c616d030a9ef7f3d2855a088106&type=album")
    
    elif (message.text == "В главное меню?"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Поздороваться")
        button2 = types.KeyboardButton("Домашка?")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Ты что, такой команды не существует, только /home")

bot.polling(none_stop=True)