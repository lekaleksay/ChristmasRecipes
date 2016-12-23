import config
from config import database_name
from SQLighter import SQLighter
import telebot

'''создаем объект бота, к которому будем обращаться'''
bot = telebot.TeleBot(config.token)

'''создаем объект базы данных'''
db = SQLighter(database_name)

'''чтобы не перегружать память создал отдельные списки, в которых будут храниться рецепты'''
item1= db.select(1)
item2=db.select(2)
item3=db.select(3)
item4=db.select(4)
item5=db.select(5)
item6=db.select(6)

'''хэндлер для клавиатуры, реагирует на тип команда, т.е. подключает клаву в начале диалога'''
@bot.message_handler(commands = ['start'])
def handle_start(message):
    '''создаем объект клавиатуры'''
    kb = telebot.types.ReplyKeyboardMarkup()
    '''Кнопки по горизонтали'''
    kb.row('Рождественский гусь с яблоками', 'Рождественский салат из сельди, яблок и клюквы')
    kb.row('Канапе с лососем и свеклой', 'Рождественский пудинг с мороженым')
    kb.row('Коктейль Рождественский пряник', 'Функции')
    '''отсылаем клавиатуру пользователю'''
    bot.send_message(message.from_user.id, 'Wellcome', reply_markup=kb)

'''хендлер реакции на сообщение с клавиатуры'''
@bot.message_handler(content_types=['text'])
def otvet1(message):

    if message.text == 'Рождественский гусь с яблоками':
        bot.send_message(message.chat.id, item1)
    elif message.text == 'Рождественский салат из сельди, яблок и клюквы':
        bot.send_message(message.chat.id, item2)
    elif message.text == 'Канапе с лососем и свеклой':
        bot.send_message(message.chat.id, item3)
    elif message.text == 'Рождественский пудинг с мороженым':
        bot.send_message(message.chat.id, item4)
    elif message.text == 'Коктейль Рождественский пряник':
        bot.send_message(message.chat.id, item5)
    elif message.text == 'Функции':
        bot.send_message(message.chat.id, item6)
    else:
        bot.send_message(message.chat.id, 'Приветствую в боте Рожденственские рецепты!\n Здесь собраны лучшие рецепты, которые украсят ваш новогодний стол\n ')

'''вводим в цикл'''
if __name__ == '__main__':
    bot.polling(none_stop=True)