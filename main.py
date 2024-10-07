import random
from datetime import datetime
import telebot
from config import Password
from telebot import types
from model import Kard, db, Deck, User_Kard
from model import User, db

token = Password['password']
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    try:
        User.get(id=message.from_user.id)
        print('Этот пользователь существует')
    except User.DoesNotExist:
        User.create(id=message.from_user.id,
                    user_name=str(message.from_user.username),
                    level=1,
                    token=5,
                    count_card=0)
        user = User.get(id=message.from_user.id)
        Deck.create(user=user, count=0)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btm1 = types.KeyboardButton('👋Поздароваться')
    btm2 = types.KeyboardButton('🤷🏼‍Зачем данный бот?')
    btm3 = types.KeyboardButton('🙎🏼‍Мой профиль')
    btm4 = types.KeyboardButton('🃏Карты')
    btm5 = types.KeyboardButton('💸Токены')
    btm6 = types.KeyboardButton('🎁Получить токены')
    btm7 = types.KeyboardButton('🏆Моя Колода')
    markup.add(btm1, btm2, btm3, btm4, btm5, btm6, btm7)
    user = User.get(id=message.from_user.id)
    bot.send_message(message.chat.id,
                     text=f"Привет , {message.from_user.first_name}👋 "
                          f"Я телеграм-бот для развлечений🎮"
                          f"  Твои токены {user.token} из 5💸",
                     reply_markup=markup)


@bot.message_handler()
def chat(message):
    user = User.get(User.id == message.from_user.id)
    if message.text == "👋Поздароваться":
        bot.send_message(message.chat.id,
                         f"{message.from_user.first_name} , Добро пожаловать в Телеграм бот , Demaryyy.👋")
    if message.text == "🤷🏼‍Зачем данный бот?":
        bot.send_message(message.chat.id,
                         f"Значит, {message.from_user.first_name} , слушай, данный бот предназначен для развлечений и чтобы убить время.🙌🏻")
    if message.text == "🙎🏼‍Мой профиль":
        bot.send_message(message.chat.id,
                         f"{message.from_user.first_name}, вот твой уровень : {user.level}🆙 \n"
                         f"Твои токены: {user.token}💸 \n"
                         f"У тебя {user.count_card} карт🃏")
    if message.text == "💸Токены":
        bot.send_message(message.chat.id,
                         f"{message.from_user.first_name} , у тебя {user.token}💸")
    if message.text == '🃏Карты':
        if user.token > 0:
            chance = random.randint(1, 100)
            if 49 < chance < 101:
                card = Kard.get(Kard.id == random.randint(1, 2))
            if 20 < chance < 49:
                card = Kard.get(Kard.id == random.randint(3, 4))
            if 7 < chance < 20:
                card = Kard.get(Kard.id == random.randint(5, 6))
            if 2 < chance < 7:
                card = Kard.get(Kard.id == random.randint(7, 9))
            if 0 < chance < 2:
                card = Kard.get(Kard.id == random.randint(10, 11))

            photo = open(card.img, 'rb')
            user.count_card += 1
            user.token -= 1

            u_Kard = User_Kard.create(deck=user.deck, kard=card)
            user.save()
            u_Kard.save()

            bot.send_photo(message.chat.id, photo)

        else:
            bot.send_message(message.chat.id,
                             f"{message.from_user.first_name} , твои токены воспонятся завтра💸")

    if message.text == "🏆Моя Колода":
        deck = Deck.get(Deck.user == user)
        cards = User_Kard.select().join(Deck).where(Deck.user == user)

        card_names = [card.kard.kard_name for card in cards]

        bot.send_message(message.chat.id,
                         f"{message.from_user.first_name}, в твоей колоде есть следующие карты:\n\n"
                         + "\n".join(card_names))

    if message.text == "🎁Получить токены":
        if user.get_today == datetime.date(datetime.today()):
            bot.send_message(message.chat.id, "Вы уже получали токены")
        else:
            bot.send_message(message.chat.id,
                             f"{message.from_user.first_name} , а вот и твои токены💸\n"
                             f"У тебя {user.token}💸 из 5💸 \n"
                             f"Дата:  {datetime.date(datetime.today())}")

            user.get_today = datetime.date(datetime.today())
            user.token += 5
            user.save()


bot.polling(none_stop=True)
