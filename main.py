import telebot
from telebot import types

bot = telebot.TeleBot('6215739697:AAG4LEu0OncOAfudFvz06wRpZlk84UM9Ufw')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Congratulations 🎊')
    item2 = types.KeyboardButton('Address 📍')
    item3 = types.KeyboardButton('Dress code 🕺')
    item4 = types.KeyboardButton('Time ⏰')

    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)


    bot.send_message(message.chat.id,
                     'Салем, нәзік жанды {0.first_name}! Группаңмен күшті уақыт өткізуге дайынсың ба?'.format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == 'Address 📍':
        bot.send_photo(message.chat.id, open('first.png', 'rb'))
        bot.send_message(message.chat.id, 'SDU G block, room 304')

    elif message.text == 'Dress code 🕺':
        bot.send_photo(message.chat.id, open('second.png', 'rb'))
        bot.send_message(message.chat.id, 'Жақсы көңіл-күймен және жүзіңізге күлкі ала келіңіз')


    elif message.text == 'Time ⏰':
        bot.send_photo(message.chat.id, open('8march.png', 'rb'))
        bot.send_message(message.chat.id, 'Сіздерді 10.08.23 күні сағат 18:00 де болатын кешіміздің қадірлі қонағы болуға шақырамыз')


    elif message.text == 'Congratulations 🎊':
        bot.send_photo(message.chat.id, open('third.png', 'rb'))
        bot.send_message(message.chat.id, '8 март - Нәзік жанды арулардың халықаралық мерекесі,\n'
                                          'Арта берсін арулардың жанұясының берекесі.\n'
                                          'Бұл күні тарихта өткен әртүрлі оқиғалар,\n'
                                          'Біз үшін сіздерді қуантудың бір себебі.\n\n'
                                          'Дей келе сіздерді 8 Наурыз Халықаралық әйелдер күнімен\n'
                                          '“Жұрттың группасы” жігіттері шын жүректен құттықтайды.🥳\n'
                                          'Жүздеріңізден күлкі кетпесін🙏. Әрдайым группамыздың гүлі болып жүре беріңіздер🌸🌹💐')


bot.polling(none_stop=True)
