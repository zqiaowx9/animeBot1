import telebot
from telebot import types
import random
from random import choice

bot = telebot.TeleBot('7187511848:AAFfDNzC_SsE2NP_5Q9SVZ7UeNAGUWh8DaI')

animefacts = ['60 процентов всей анимации, что существует на нашей планете, — это японское аниме.',
              'Первым аниме, которое прославилось за пределами Японии, был сериал Astro Boy 1963 года.Факт',
              'Первое аниме, которое показали в СССР, был «Летающий корабль-призрак».',
              'Первое аниме, которое показали в СССР, был «Летающий корабль-призрак».',
              'По негласному закону аниме, чем важнее герой, тем детальнее ему прорисовывают глаза.',
              'В Японии на печать комиксов тратится больше бумаги, чем на производство туалетных рулонов.',
              'В отличие от американских и европейских комиксов, которые читают в основном подростки и нёрды, манга создаётся для людей всех возрастов.',
              'В Японии термин «отаку» используется в негативном ключе для описания людей, которые чем-то одержимы. Не только аниме, как это принято в России.',
              'Существует правило, из которого ещё не было исключений: если по манге выходит аниме, продажи первой возрастают как минимум на 10 процентов.',
              'Цвет волос в аниме подбирается не рандомно. Тут всё хитро и продуманно: цвет волос указывает на конкретные черты личности героя. Есть даже определённая теория заговора!',
              '«Покемон» первоначально был игрой для GameBoy. Только потом подтянулись манга и аниме.',
              'Евангелион» создавали, чтобы проверить, что приемлемо для аниме, а что нет. И всё бы ок — но финал...',
              'Самый длинный аниме-сериал — это «Садзаэ-сан», который выходит с 1969 года по сей день. В нем больше 7 тысяч серий. Хвалёная «Санта-Барбара», для сравнения, почти в 3,5 раза короче.',
              'Советские «Приключения пингвинёнка Лоло» сняты совместно с японскими анимационными студиями. То есть, технически этот мультфильм можно считать российским аниме.',
              '«Тетрадь смерти» была запрещена в Китае, так как местные фанаты этого аниме начали массово покупать тетради и вписывать туда имена всех, кого ненавидели, в надежде, что они умрут.',
              'Изначально Масаши Кишимото, автор «Наруто», не планировал создавать Саске. Он появился неожиданно для самого Масаши: издатель настоял на том, чтобы в истории появился таинственный и загадочный bad-ass.',
              'Издатель «Ван-Писа» боялся, что серия не проживёт и пяти лет.',
              'Самое кассовое аниме ever — «Унесённые призраками» Хаяо Миядзаки. В мировом прокате фильм собрал $275 миллионов.',
              'Знаменитое выражение-мем «over 9000!» появилось в Dragon Ball Z.',
              'Интересный факт: аниме в комиксах принято читать справа налево. Важно знать, что именно такой способ чтения характерен всем жителям Японии, независимо от текста.',
              'Аниме является исключительно японским жанром мультипликационной анимации, которая рассчитывается в основном на взрослую аудиторию. Такой мультсериал, как «Пикачу» и пара других, являются исключением.',
              'В Японии на печать комиксов тратится больше бумаги, чем на производство туалетных рулонов.',
              'Рисовку волос и тела в аниме придумали японцы, а стиль глаз был скопирован у Уолта Диснея, чего японцы, кстати, не отрицают.',
              'По негласному закону аниме, чем важнее герой, тем детальнее ему прорисовывают глаза.',
              'Титаны из "Атака на титанов" основаны на пьяницах.',
              'Все в «Код Гиасс» любят пиццу, потому что сериал был профинансирован Pizza Hut.',
              'Твое имя рекордсмен по кассовым сборам среди аниме фильмов во всем мире',
              'Садзае-сан самый длинный аниме сериал, который идет и по сей день.',
              'В Китае было запрещено показывать Тетрадь смерти.',
              'Каждый житель Японии в год тратит около 30$ на покупку манги (при том, что стоимость томика манги в пределах 2-3$).',
              'В начале 60-х годов авторами манги для девочек в основном были мужчины. Лишь с середины 60-х годов XX века начали появляться творения женских авторов-художниц.',
              'Один том манги содержит, как правило, не менее 150-300 стр.',
              'Только в Японии было куплено 50 млн. копий манги Bleach «Блич».',
              'Многие места продаж манги в Японии посещает не менее 1000 посетителей в день.',
              'В большинстве серий манг главными персонажами являются негативные герои, что иногда хорошо прикрывается авторами, но чаще нет.',
              'Мангака – художник, создающий иллюстрации для манги.',
              'В Японии есть несколько «Манга-кафе», где посетители могут не только попить кофе, но и насладиться чтением любимой манги. Первое из них открылось в 1988 году.',
              'В среднем на прочтение манги объемом 300 стр. у японцев уходит около 20 минут.',
              'Признаком возбуждения героев манги является носовое кровотечение.',
              'Около 60-70% читателей манги – женщины!',
              'В Японии научились с помощью аниме привлекать новобранцев в армию'
              ]


@bot.message_handler(commands=['start'])
def start(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  btn1 = types.KeyboardButton("🇷🇺 Русский")
  markup.add(btn1)
  bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

  if message.text == '🇷🇺 Русский':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Сайты для просмотра аниме")
    btn2 = types.KeyboardButton('Новости')
    btn3 = types.KeyboardButton('Советую посмотреть')
    btn4 = types.KeyboardButton('Зима2024')
    btn5 = types.KeyboardButton('Фильмы в жанре аниме')
    btn6 = types.KeyboardButton('Романтика')
    btn8 = types.KeyboardButton('Тесты')
    btn9 = types.KeyboardButton('👀 Ты этого точно не знал!')
    btn10 = types.KeyboardButton('🔙 Вернуться к выбору языка')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn8, btn9, btn10)
    bot.send_message(message.from_user.id, "👋 Вас приветствует Аниме бот⛩ ", reply_markup=markup)
    bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел')

  elif message.text == '🔙 Вернуться к выбору языка':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🇷🇺 Русский")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)

  elif message.text == '👀 Ты этого точно не знал!':
    for i in range(5):
      bot.send_message(message.from_user.id, random.choice(animefacts))

  elif message.text == 'Сайты для просмотра аниме':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('jut.su')
    btn2 = types.KeyboardButton('AnimeGO')
    btn3 = types.KeyboardButton('YummyAnime')
    btn4 = types.KeyboardButton('Anixart(приложение на андроид)')
    btn5 = types.KeyboardButton('ANIMESTARS')
    btn6 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)

  elif message.text == 'jut.su':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: jut.su\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == 'AnimeGO':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: AnimeGO\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://animego.org)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == 'YummyAnime':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: YummyAnime\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://yummy-anime.org)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == 'Anixart':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: Anixart\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://anixart.tv)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == 'ANIMESTARS':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: ANIMESTARS\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://animestars.org)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == '🔙 Главное меню':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Сайты для просмотра аниме")
    btn2 = types.KeyboardButton('Новости')
    btn3 = types.KeyboardButton('Советую посмотреть')
    btn4 = types.KeyboardButton('Зима2024')
    btn5 = types.KeyboardButton('Фильмы в жанре аниме')
    btn6 = types.KeyboardButton('Романтика')
    btn8 = types.KeyboardButton('Тесты')
    btn9 = types.KeyboardButton('👀 Ты этого точно не знал!')
    btn10 = types.KeyboardButton('🔙 Вернуться к выбору языка')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn8, btn9, btn10)
    bot.send_message(message.from_user.id, "👀 Выбери интересующий раздел", reply_markup=markup)

  elif message.text == 'Новости':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: Новости\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://shazoo.ru/forums)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == 'Советую посмотреть':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn01 = types.KeyboardButton('🔙 Главное меню')
    btn1 = types.KeyboardButton('🔎 1.«Атака титанов»')
    btn2 = types.KeyboardButton('🔎 2.Киберпанк: Бегущие по краю»')
    btn3 = types.KeyboardButton('🔎 3.«Стальной алхимик: Братство»')
    btn4 = types.KeyboardButton('🔎 4.«Ван-Пис» (One Piece)')
    btn5 = types.KeyboardButton('🔎 5.«Монстр»')
    btn6 = types.KeyboardButton('🔎 6.«Моб Психо')
    btn7 = types.KeyboardButton('🔎 7.«Евангелион»')
    btn8 = types.KeyboardButton('🔎 8.«Отчёт о буйстве духов»')
    btn9 = types.KeyboardButton('🔎 9.«Самурай Чамплу»')
    btn10 = types.KeyboardButton('🔎 10.«Шумиха!»')
    btn11 = types.KeyboardButton('🔎 11.«Код Гиас: Восставший Лелуш»')
    btn12 = types.KeyboardButton('🔎 12.«Истребитель демонов»')
    btn13 = types.KeyboardButton('🔎 13.«Ковбой Бибоп»')
    btn14 = types.KeyboardButton('🔎 14.«Человек-дьявол: Плакса»')
    btn15 = types.KeyboardButton('🔎 15.«Охотник х Охотник»')
    btn16 = types.KeyboardButton('🔎 16.«Фури-Кури»')
    btn17 = types.KeyboardButton('🔎 17.«Первый шаг»')
    btn18 = types.KeyboardButton('🔎 18.«Наруто: Ураганные хроники»')
    btn19 = types.KeyboardButton('🔎 19.«Созданный в Бездне»')
    btn20 = types.KeyboardButton('🔎 20.«Хост-клуб Оранской школы»')
    btn21 = types.KeyboardButton('🔎 21.«Моя геройская академия»')
    btn22 = types.KeyboardButton('🔎 22.«Триган»')
    btn23 = types.KeyboardButton('🔎 23.«Невероятные приключения ДжоДжо»')
    btn24 = types.KeyboardButton('🔎 24.«Драконий жемчуг Зет»')
    btn25 = types.KeyboardButton('🔎 25.«Волейбол!!»')
    markup.add(btn01, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15,
               btn16, btn17, btn18, btn19,
               btn20, btn21, btn22, btn23, btn24, btn25)
    bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)

  elif message.text == '🔎 1.«Атака титанов»':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: 🔎 1.«Атака титанов»\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/shingekii-no-kyojin/)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == '🔎 2.Киберпанк: Бегущие по краю»':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: 🔎 2.Киберпанк: Бегущие по краю»\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://animego.org/anime/kiberpank-beguschie-po-krayu-2128)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == '🔎 3.«Стальной алхимик: Братство»':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: 🔎 3.«Стальной алхимик: Братство»\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/fullmeetal-alchemist/)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == '🔎 4.«Ван-Пис» (One Piece)':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: 🔎 4.«Ван-Пис» (One Piece)\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/oneepiece/)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == '🔎 5.«Монстр»':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: 🔎 5.«Монстр»\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/kaibutsu-kun/)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == '🔎 6.«Моб Психо':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: 🔎 6.«Моб Психо\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/mob-100/)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == '🔎 7.«Евангелион»':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: 🔎 7.«Евангелион»\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/neon-evangelion/)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == '🔎 8.«Отчёт о буйстве духов»':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: 🔎 8.«Отчёт о буйстве духов»\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/yuu-hakusho/)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == '🔎 9.«Самурай Чамплу»':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: 🔎 9.«Самурай Чамплу»\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/samurai-champlo/)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == '🔎 10.«Шумиха!»':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: 🔎 10.«Шумиха!»\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/baccaano/)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == '🔎 11.«Код Гиас: Восставший Лелуш»':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: 🔎 11.«Код Гиас: Восставший Лелуш»\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/code-geass/)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == '🔎 12.«Истребитель демонов»':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: 🔎 12.«Истребитель демонов»\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/kime-no-yaiba/)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == '🔎 13.«Ковбой Бибоп»':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: 🔎 13.«Ковбой Бибоп»\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/cowboy-bebop/)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == '🔎 14.«Человек-дьявол: Плакса»':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: 🔎 14.«Человек-дьявол: Плакса»\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/devil-may-cry/)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == '🔎 15.«Охотник х Охотник»':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: 🔎 15.«Охотник х Охотник»\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/hunter-hunter/)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == '🔎 16.«Фури-Кури»':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: 🔎 16.«Фури-Кури»\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/furi-kuri/)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == '🔎 17.«Первый шаг»':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: 🔎 17.«Первый шаг»\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/hajime-no-ippo/)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == '🔎 18.«Наруто: Ураганные хроники»':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: 🔎 18.«Наруто: Ураганные хроники»\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/naruuto/season-2/episode-159.html)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == '🔎 19.«Созданный в Бездне»':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: 🔎 19.«Созданный в Бездне»\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/made-abyss/)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == '🔎 20.«Хост-клуб Оранской школы»':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: 🔎 20.«Хост-клуб Оранской школы»\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/host-club/)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == '🔎 21.«Моя геройская академия»':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: 🔎 21.«Моя геройская академия»\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/boku-hero-academia/)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == '🔎 22.«Триган»':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: 🔎 22.«Триган»\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/triguun/)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == '🔎 23.«Невероятные приключения ДжоДжо»':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: 🔎 23.«Невероятные приключения ДжоДжо»\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/jojo-bizarre-adventure/)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == '🔎 24.«Драконий жемчуг Зет»':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: 🔎 24.«Драконий жемчуг Зет»\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/dragonball/season-2/)',
                     reply_markup=markup, parse_mode='Markdown')



  elif message.text == 'Зима2024':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn01 = types.KeyboardButton('🔙 Главное меню')
    btn1 = types.KeyboardButton('Провожающая в последний путь Фрирен')
    btn2 = types.KeyboardButton('Добро пожаловать в класс превосходства 3')
    btn3 = types.KeyboardButton('Магия и мускулы')
    btn4 = types.KeyboardButton('Синий экзорцист')
    btn5 = types.KeyboardButton('Ишура')
    btn6 = types.KeyboardButton('Ниндзя Камуи')
    btn7 = types.KeyboardButton('Поднятие уровня в одиночку')
    btn8 = types.KeyboardButton('Сасаки и Пи')
    markup.add(btn01, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)

  elif message.text == 'Провожающая в последний путь Фрирен':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: Провожающая в последний путь Фрирен\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/sousou-no-frieren/episode-23.html)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == 'Добро пожаловать в класс превосходства 3':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: Добро пожаловать в класс превосходства 3\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/shugi-no-kyoushitsu/season-3/)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == 'Магия и мускулы':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: Магия и мускулы\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/mashle/)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == 'Синий экзорцист':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: Синий экзорцист\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/ao-exorcist/)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == 'Ишура':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: Ишура\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/ishura/)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == 'Ниндзя Камуи':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: Ниндзя Камуи\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/ninja-kamui/)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == 'Поднятие уровня в одиночку':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: Поднятие уровня в одиночку\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/solo-leveling/)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == 'Сасаки и Пи':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: Сасаки и Пи\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/sasaki-to-pii/)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == 'Фильмы в жанре аниме':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn01 = types.KeyboardButton('🔙 Главное меню')
    btn1 = types.KeyboardButton("Ходячий замок")
    btn2 = types.KeyboardButton('Унесённые призраками')
    btn3 = types.KeyboardButton('Твоё имя')
    btn4 = types.KeyboardButton('Ди: Жажда крови')
    markup.add(btn01, btn1, btn2, btn3, btn4)
    bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)

  elif message.text == 'Ходячий замок':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: Ходячий замок\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://kinogo.inc/anime/11477-hodyachiy-zamok-hd-v7.html)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == 'Унесённые призраками':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: Унесённые призраками\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://kinogo.inc/#gsc.tab=0)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == 'Твоё имя"':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: Твоё имя"\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://kinogo.inc/anime/3846-tvoe-imya.html)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == 'Ди: Жажда крови':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: Ди: Жажда крови\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://animego.org/anime/di-ohotnik-na-vampirov-zhazhda-krovi-1233)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == 'Романтика':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn01 = types.KeyboardButton('🔙 Главное меню')
    btn1 = types.KeyboardButton('Сад изящных слов')
    btn2 = types.KeyboardButton('Пять сантиметров в секунду')
    btn3 = types.KeyboardButton('Дитя погоды')
    btn4 = types.KeyboardButton('Ловцы забытых голосов')
    btn5 = types.KeyboardButton('Единственному мне, кто тебя любил')
    btn6 = types.KeyboardButton('Хоримия')
    btn7 = types.KeyboardButton('Этот глупый свин не понимает мечту девочки-зайки')
    markup.add(btn01, btn1, btn2, btn3, btn4)
    bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)

  elif message.text == 'Сад изящных слов':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: Сад изящных слов\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://animego.org/anime/sad-izyaschnyh-slov-162)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == 'Пять сантиметров в секунду':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: Пять сантиметров в секунду\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://animego.org/anime/pyat-santimetrov-v-sekundu-1155)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == 'Дитя погоды':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: Дитя погоды\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://animego.org/anime/tenki-no-ko-1082)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == 'Ловцы забытых голосов':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: Ловцы забытых голосов\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut-su.net/1780-lovcy-zabytyh-golosov.html)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == 'Единственному мне, кто тебя любил':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: Единственному мне, кто тебя любил\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://animego.org/search/all?q=Единственному+мне%2C+кто+тебя+любил)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == 'Хоримия':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: Хоримия\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/horimiya/)',
                     reply_markup=markup, parse_mode='Markdown')

  elif message.text == 'Этот глупый свин не понимает мечту девочки-зайки':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     'Твой раздел: Этот глупый свин не понимает мечту девочки-зайки\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://jut.su/seishun-buta/)',
                     reply_markup=markup, parse_mode='Markdown')


  elif message.text == 'Тесты':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     '📲 Чтобы перейти к тестам перейди по [ссылке](https://pikuco.ru/tag/anime/)', reply_markup=markup,
                     parse_mode='Markdown')




bot.polling(none_stop=True, interval=0)

