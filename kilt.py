import telebot
import ast
import time
from telebot import types

bot = telebot.TeleBot("789932335:AAFTc2N0FQFx7czhASPbW8S6c9EvZqBDOf4")
 

stringList = {"450£": "зелёный килт", "300£": "синий килт"}


def makeKeyboard():   
    markup = types.InlineKeyboardMarkup()
    
    for key, value in stringList.items():
        markup.add(types.InlineKeyboardButton(text=value,
                                              callback_data="['value', '" + value + "', '" + key + "']"))


    return markup

@bot.message_handler(commands=['test'])
def handle_command_adminwindow(message):
    
    bot.send_message(chat_id="@Scottish_pie",
                     text="Сколько стоят эти килты?",
                     reply_markup=makeKeyboard(),
                     parse_mode='HTML')

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):

    if (call.data.startswith("['value'")):
        valueFromCallBack = ast.literal_eval(call.data)[1]
        keyFromCallBack = ast.literal_eval(call.data)[2]
        bot.answer_callback_query(callback_query_id=call.id,
                              show_alert=True,
                              text="Отличный выбор! Это " + valueFromCallBack + " стоимостью в " + keyFromCallBack)


while True:
    try:
        bot.polling(none_stop=True, interval=0, timeout=0)
    except:
        time.sleep(10)

