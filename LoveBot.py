import datetime
import os
import random
import time

import emoji
from dotenv import load_dotenv
from PIL import Image, ImageDraw, ImageFont
from telegram import (Bot, InlineKeyboardButton, InlineKeyboardMarkup, Poll,
                      Update)
from telegram.ext import (CallbackQueryHandler, CommandHandler, Filters,
                          MessageHandler, PollAnswerHandler, PollHandler,
                          Updater)

load_dotenv()
token = os.environ['TG_BOT_TOKEN']
bot = Bot(token)
updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id,
                             'Привет, перед тобой LoveBot. Он создан специально для моей любимой супруги ' + emoji.emojize(
                                 ":face_blowing_a_kiss:"))
    time.sleep(4)
    return klava(update, context)


def klava(update, context):
    keyboard = [
        [InlineKeyboardButton('Любимый', callback_data='1'), InlineKeyboardButton('Инфа', callback_data='2')],
        [InlineKeyboardButton('Эмоция-метр', callback_data='3'),
         InlineKeyboardButton('Комплимент', callback_data='4')],
        [InlineKeyboardButton('День недели', callback_data='5'), InlineKeyboardButton('Твое фото', callback_data='6')],
        [InlineKeyboardButton('Настроение', callback_data='7'), InlineKeyboardButton('Qwiz', callback_data='8')],
        [InlineKeyboardButton('Утро', callback_data='9'), InlineKeyboardButton('Вечер', callback_data='10')],
        [InlineKeyboardButton('Любовные sms', callback_data='11'),
         InlineKeyboardButton('Стоп таймер', callback_data='12')]
    ]
    context.bot.send_message(update.effective_chat.id, 'Вот что умеет этот бот',
                             reply_markup=InlineKeyboardMarkup(keyboard))

quiz_score = 0


def button(update, context):
    q = update.callback_query
    q.answer()
    if q.data == '1':
        return father(update, context)
    elif q.data == '2':
        context.bot.send_message(update.effective_chat.id, get_open('info.txt'))
    elif q.data == '3':
        return emotion(update, context)
    elif q.data == '4':
        return compliment(update, context)
    elif q.data == '5':
        return day_week(update, context)
    elif q.data == '6':
        return send_photo(update, context)
    elif q.data == '7':
        return photos(update, context)
    elif q.data == '8':
        return quiz_start(update, context)
    elif q.data == '9':
        return goodmorning(update, context)
    elif q.data == '10':
        return goodevening(update, context)
    elif q.data == '11':
        return love_message(update, context)
    elif q.data == '12':
        return stop_timers(update, context)
    elif q.data == '13':
        return
    elif q.data == '14':
        return
    elif q.data == '15':
        return
    elif q.data == '16':
        return
    elif q.data == '17':
        context.bot.send_message(update.effective_chat.id, get_open('info2.txt'))
    elif q.data == '18':
        global quiz_score
        quiz_score += 1
        context.bot.send_message(update.effective_chat.id, 'Это правильный ответ')
        context.bot.send_message(update.effective_chat.id, emoji.emojize(":fireworks:"))
        time.sleep(3)
        return quiz1(update, context)
    elif q.data == '19':
        context.bot.send_message(update.effective_chat.id, 'Это неправильный ответ' + emoji.emojize(":man_shrugging:"))
        time.sleep(3)
        return quiz1(update, context)
    elif q.data == '20':
        context.bot.send_message(update.effective_chat.id, 'Это неправильный ответ' + emoji.emojize(":man_shrugging:"))
        time.sleep(3)
        return quiz1(update, context)
    elif q.data == '21':
        context.bot.send_message(update.effective_chat.id, 'Это неправильный ответ' + emoji.emojize(":man_shrugging:"))
        time.sleep(3)
        return quiz1(update, context)
    elif q.data == '22':
        context.bot.send_message(update.effective_chat.id, 'Это неправильный ответ' + emoji.emojize(":man_shrugging:"))
        time.sleep(3)
        return quiz1(update, context)
    elif q.data == '23':
        context.bot.send_message(update.effective_chat.id, 'Это неправильный ответ' + emoji.emojize(":man_shrugging:"))
        time.sleep(3)
        return quiz1(update, context)
    elif q.data == '24':
        time.sleep(3)
        return quiz2(update, context)
    elif q.data == '25':
        context.bot.send_message(update.effective_chat.id, 'Это неправильный ответ' + emoji.emojize(":man_shrugging:"))
        time.sleep(3)
        return quiz2(update, context)
    elif q.data == '26':
        context.bot.send_message(update.effective_chat.id, 'Это неправильный ответ' + emoji.emojize(":man_shrugging:"))
        time.sleep(3)
        return quiz2(update, context)
    elif q.data == '27':
        quiz_score += 1
        context.bot.send_message(update.effective_chat.id, 'Это правильный ответ')
        context.bot.send_message(update.effective_chat.id, emoji.emojize(":fireworks:"))
        time.sleep(3)
        return quiz2(update, context)
    elif q.data == '28':
        context.bot.send_message(update.effective_chat.id, 'Это неправильный ответ' + emoji.emojize(":man_shrugging:"))
        time.sleep(3)
        return quiz2(update, context)
    elif q.data == '29':
        context.bot.send_message(update.effective_chat.id, 'Это неправильный ответ' + emoji.emojize(":man_shrugging:"))
        time.sleep(3)
        return quiz2(update, context)
    elif q.data == '30':
        time.sleep(3)
        return quiz3(update, context)
    elif q.data == '31':
        context.bot.send_message(update.effective_chat.id, 'Это неправильный ответ' + emoji.emojize(":man_shrugging:"))
        time.sleep(3)
        return quiz3(update, context)
    elif q.data == '32':
        context.bot.send_message(update.effective_chat.id, 'Это неправильный ответ' + emoji.emojize(":man_shrugging:"))
        time.sleep(3)
        return quiz3(update, context)
    elif q.data == '33':
        context.bot.send_message(update.effective_chat.id, 'Это неправильный ответ' + emoji.emojize(":man_shrugging:"))
        time.sleep(3)
        return quiz3(update, context)
    elif q.data == '34':
        quiz_score += 1
        context.bot.send_message(update.effective_chat.id, 'Это правильный ответ')
        context.bot.send_message(update.effective_chat.id, emoji.emojize(":fireworks:"))
        time.sleep(3)
        return quiz3(update, context)
    elif q.data == '35':
        context.bot.send_message(update.effective_chat.id, 'Это неправильный ответ' + emoji.emojize(":man_shrugging:"))
        time.sleep(3)
        return quiz3(update, context)
    elif q.data == '36':
        time.sleep(3)
        return quiz4(update, context)
    elif q.data == '37':
        context.bot.send_message(update.effective_chat.id, 'Это неправильный ответ' + emoji.emojize(":man_shrugging:"))
        time.sleep(3)
        return quiz4(update, context)
    elif q.data == '38':
        quiz_score += 1
        context.bot.send_message(update.effective_chat.id, 'Это правильный ответ')
        context.bot.send_message(update.effective_chat.id, emoji.emojize(":fireworks:"))
        time.sleep(3)
        return quiz4(update, context)
    elif q.data == '39':
        context.bot.send_message(update.effective_chat.id, 'Это неправильный ответ' + emoji.emojize(":man_shrugging:"))
        time.sleep(3)
        return quiz4(update, context)
    elif q.data == '40':
        context.bot.send_message(update.effective_chat.id, 'Это неправильный ответ' + emoji.emojize(":man_shrugging:"))
        time.sleep(3)
        return quiz4(update, context)
    elif q.data == '41':
        context.bot.send_message(update.effective_chat.id, 'Это неправильный ответ' + emoji.emojize(":man_shrugging:"))
        time.sleep(3)
        return quiz4(update, context)
    elif q.data == '42':
        time.sleep(3)
        return quiz5(update, context)
    elif q.data == '43':
        context.bot.send_message(update.effective_chat.id, 'Это неправильный ответ' + emoji.emojize(":man_shrugging:"))
        time.sleep(3)
        return quiz5(update, context)
    elif q.data == '44':
        context.bot.send_message(update.effective_chat.id, 'Это неправильный ответ' + emoji.emojize(":man_shrugging:"))
        time.sleep(3)
        return quiz5(update, context)
    elif q.data == '45':
        context.bot.send_message(update.effective_chat.id, 'Это неправильный ответ' + emoji.emojize(":man_shrugging:"))
        time.sleep(3)
        return quiz5(update, context)
    elif q.data == '46':
        quiz_score += 1
        context.bot.send_message(update.effective_chat.id, 'Это правильный ответ')
        context.bot.send_message(update.effective_chat.id, emoji.emojize(":fireworks:"))
        time.sleep(3)
        return quiz6(update, context)
    elif q.data == '47':
        context.bot.send_message(update.effective_chat.id, 'Это неправильный ответ' + emoji.emojize(":man_shrugging:"))
        time.sleep(3)
        return quiz5(update, context)
    elif q.data == '48':
        quiz_score += 1
        context.bot.send_message(update.effective_chat.id, 'Это правильный ответ')
        context.bot.send_message(update.effective_chat.id, emoji.emojize(":fireworks:"))
        time.sleep(3)
        return quiz6(update, context)
    elif q.data == '49':
        context.bot.send_message(update.effective_chat.id, 'Это неправильный ответ' + emoji.emojize(":man_shrugging:"))
        time.sleep(3)
        return quiz6(update, context)
    elif q.data == '50':
        context.bot.send_message(update.effective_chat.id, 'Это неправильный ответ' + emoji.emojize(":man_shrugging:"))
        time.sleep(3)
        return quiz6(update, context)
    elif q.data == '51':
        context.bot.send_message(update.effective_chat.id, 'Это неправильный ответ' + emoji.emojize(":man_shrugging:"))
        time.sleep(3)
        return quiz6(update, context)
    elif q.data == '52':
        context.bot.send_message(update.effective_chat.id, 'Это неправильный ответ' + emoji.emojize(":man_shrugging:"))
        time.sleep(3)
        return quiz6(update, context)
    elif q.data == '53':
        time.sleep(3)
        return quiz_answer(update, context)
    elif q.data == '54':
        context.bot.send_message(update.effective_chat.id, 'Это неправильный ответ' + emoji.emojize(":man_shrugging:"))
        time.sleep(3)
        return quiz_answer(update, context)
    elif q.data == '55':
        quiz_score += 1
        context.bot.send_message(update.effective_chat.id, 'Это правильный ответ')
        context.bot.send_message(update.effective_chat.id, emoji.emojize(":fireworks:"))
        time.sleep(3)
        return quiz_answer(update, context)
    elif q.data == '56':
        context.bot.send_message(update.effective_chat.id, 'Это неправильный ответ' + emoji.emojize(":man_shrugging:"))
        time.sleep(3)
        return quiz_answer(update, context)
    elif q.data == '57':
        context.bot.send_message(update.effective_chat.id, 'Это неправильный ответ' + emoji.emojize(":man_shrugging:"))
        time.sleep(3)
        return quiz_answer(update, context)


def father(update, context):
    context.bot.send_message(update.effective_chat.id,
                             'Создатель этого бота Аникеев Максим - программист от бога. Это мой первый бот, который я посвещаю своей бесконечно любимой супруге Орловой Екатерине')
    time.sleep(5)
    context.bot.send_message(update.effective_chat.id, emoji.emojize(":kiss_mark:"))
    time.sleep(3)
    return klava(update, context)


def get_open(file):
    f = open(file, 'r', encoding='utf - 8')
    data = f.read()
    f.close()
    return data


list = ['Я тебя люблю', 'Ты мое сокровище', 'Я тебя обожаю', 'Счастье ты мое', 'Мир прекрасен, когда я рядом с тобой',
        'Ты моя королева', 'Ты мое солнышко, я бесконечно тебя люблю', 'Я счастлив рядом с тобой',
        'Как мне повезло что ты рядом со мной',
        'Жизнь прекрасна, когда ты рядом', 'Я тебя очень люблю', 'Ты мое счастье', 'Ты самое дорогое что у меня есть',
        'Ты солнышко, которое освещает весь мой жизненный путь', 'Я женат на самой прекрасной женщине на свете']

emoji_list = [emoji.emojize(":smiling_face_with_hearts:"), emoji.emojize(":smiling_face_with_heart-eyes:"),
              emoji.emojize(":face_blowing_a_kiss:"), emoji.emojize(":love_letter:"),
              emoji.emojize(":heart_with_arrow:"), emoji.emojize(":sparkling_heart:"), emoji.emojize(":growing_heart:")]


def alarm(context):
    job_love = context.job
    a = random.randint(0, (len(list) - 1))
    b = random.randint(0, (len(emoji_list) - 1))
    context.bot.send_message(job_love.context, list[a])
    context.bot.send_message(job_love.context, emoji_list[b])


def love_message(update, context):
    list1 = [10, 300, 1200, 3600, 4000]
    context.bot.send_message(update.effective_chat.id, 'Лови первые мои признания ' + emoji.emojize(":red_heart:"))
    time.sleep(3)
    context.bot.send_message(update.effective_chat.id,
                             'Сообщения будут приходить неожиданно ' + emoji.emojize(":winking_face:"))
    for i in list1:
        if i > 3600:
            context.job_queue.run_repeating(alarm, 10800, context=update.effective_chat.id,
                                            name=str(update.effective_chat.id))
        else:
            context.job_queue.run_once(alarm, i, context=update.effective_chat.id,
                                       name=str(update.effective_chat.id))


complement = ['Ты прекрасна ', 'Ты моя красавица ', 'У тебя суперическая фигурка ', 'Ты моя стройняшка ',
              'Ты сегодня прекрасна как всегда ',
              'Ты божественна ', 'Я обажаю твои шикарные длинные волосы ', 'Изгибы твоего тела меня сводят с ума ',
              'Ты сегодня хороша! ',
              'Ты моя богиня ']


def compliment(update, context):
    a = random.randint(0, (len(complement) - 1))
    context.bot.send_message(update.effective_chat.id, complement[a] + emoji.emojize(":red_heart:"))
    time.sleep(3)
    return klava(update, context)


def alarm2(context):
    job_evening = context.job
    context.bot.send_message(job_evening.context, 'Спокойной ночи любимая')
    context.bot.send_message(job_evening.context, emoji.emojize(":kiss_mark:"))


def goodevening(update, context):
    now = datetime.datetime.now()
    a = 23 * 3600 + 30 * 60 - (int(now.strftime('%H')) * 3600 + int(now.strftime('%M')) * 60)
    context.job_queue.run_once(alarm2, a, context=update.effective_chat.id, name=str(update.effective_chat.id))
    context.bot.send_message(update.effective_chat.id, 'Жди вечером сообщения :)')
    context.job_queue.run_once(alarm2, a + 86400, context=update.effective_chat.id, name=str(update.effective_chat.id))
    context.job_queue.run_once(alarm2, a + 86400 * 2, context=update.effective_chat.id,
                               name=str(update.effective_chat.id))
    context.job_queue.run_once(alarm2, a + 86400 * 3, context=update.effective_chat.id,
                               name=str(update.effective_chat.id))
    context.job_queue.run_once(alarm2, a + 86400 * 4, context=update.effective_chat.id,
                               name=str(update.effective_chat.id))
    time.sleep(3)
    return klava(update, context)


def alarm3(context):
    job_morning = context.job
    context.bot.send_message(job_morning.context, 'Доброе утро солнышко')
    context.bot.send_message(job_morning.context, emoji.emojize(":sun:"))


def goodmorning(update, context):
    now = datetime.datetime.now()
    a = 24 * 3600 + 30 * 60 - (int(now.strftime('%H')) * 3600 + int(now.strftime('%M')) * 60) + 9 * 3600 + 30 * 60
    context.job_queue.run_once(alarm2, a, context=update.effective_chat.id, name=str(update.effective_chat.id))
    context.bot.send_message(update.effective_chat.id, 'Теперь жди сообщений по утрам :)')
    context.job_queue.run_once(alarm3, a + 86400, context=update.effective_chat.id, name=str(update.effective_chat.id))
    context.job_queue.run_once(alarm3, a + 86400 * 2, context=update.effective_chat.id,
                               name=str(update.effective_chat.id))
    context.job_queue.run_once(alarm3, a + 86400 * 3, context=update.effective_chat.id,
                               name=str(update.effective_chat.id))
    context.job_queue.run_once(alarm3, a + 86400 * 4, context=update.effective_chat.id,
                               name=str(update.effective_chat.id))
    time.sleep(3)
    return klava(update, context)


def day_week(update, context):
    now = datetime.datetime.now()
    a = int(now.strftime('%w'))
    if a == 0:
        context.bot.send_message(update.effective_chat.id, 'Сегодня воскресенье, этот букет для тебя любимая')
        with open('images/розы.jpg', 'rb') as send:
            context.bot.send_document(update.effective_chat.id, send)
        time.sleep(7)
        return klava(update, context)
    elif a == 1:
        context.bot.send_message(update.effective_chat.id, 'Сегодня понедельник, этот букет для тебя любимая')
        with open('images/незабудки.jpg', 'rb') as send:
            context.bot.send_document(update.effective_chat.id, send)
        time.sleep(7)
        return klava(update, context)
    elif a == 2:
        context.bot.send_message(update.effective_chat.id, 'Сегодня вторник, этот букет для тебя любимая')
        with open('images/васильки.jpg', 'rb') as send:
            context.bot.send_document(update.effective_chat.id, send)
        time.sleep(7)
        return klava(update, context)
    elif a == 3:
        context.bot.send_message(update.effective_chat.id, 'Сегодня среда, этот букет для тебя любимая')
        with open('images/герберы.jpg', 'rb') as send:
            context.bot.send_document(update.effective_chat.id, send)
        time.sleep(7)
        return klava(update, context)
    elif a == 4:
        context.bot.send_message(update.effective_chat.id, 'Сегодня четверг, этот букет для тебя любимая')
        with open('images/пионы.jpg', 'rb') as send:
            context.bot.send_document(update.effective_chat.id, send)
        time.sleep(7)
        return klava(update, context)
    elif a == 5:
        context.bot.send_message(update.effective_chat.id, 'Сегодня пятница, этот букет для тебя любимая')
        with open('images/роза.jpg', 'rb') as send:
            context.bot.send_document(update.effective_chat.id, send)
        time.sleep(7)
        return klava(update, context)
    elif a == 6:
        context.bot.send_message(update.effective_chat.id, 'Сегодня суббота, этот букет для тебя любимая')
        with open('images/ромашка.jpg', 'rb') as send:
            context.bot.send_document(update.effective_chat.id, send)
        time.sleep(7)
        return klava(update, context)


def send_photo(update, context):
    context.bot.send_message(update.effective_chat.id, 'Загрузи свою фотографию (отправлять нужно без сжатия)')


def mem(username, bs):
    picture = Image.open(username + '2_photo.jpg')
    rgb_picture = picture.convert('RGB')
    x, y = rgb_picture.size
    mem = ImageDraw.Draw(rgb_picture)
    font = ImageFont.truetype('arial.ttf', size=int(x / 12))
    a = x / 2 - x * 2 / 5
    b = y - y / 5
    r, g, b = rgb_picture.getpixel((a, b))
    if r < 120 and g < 120 and b < 120:
        color = (255, 255, 255)
    else:
        color = (0, 0, 0)
    mem.text(((x / 2 - x * 2 / 5), y - y / 5), bs, color, font=font)
    rgb_picture.save(username + '2_mem.jpg')


list2 = ['самая прекрасная', 'лучшая на свете', 'фантастическая девушка']


def photo(update, context):
    username = str(update.message.from_user['first_name'] + '' + str(update.message.from_user['last_name']))
    photo_file = update.message.document.get_file()
    photo_file.download(username + '2_photo.jpg')
    a = random.randint(0, (len(list2) - 1))
    mem(username=username, bs=list2[a])
    with open(username + '2_mem.jpg', 'rb') as send:
        context.bot.send_document(update.effective_chat.id, send)
    time.sleep(10)
    return klava(update, context)


list3 = ['images/1.jpg', 'images/2.jpg', 'images/3.jpg', 'images/4.jpg', 'images/5.jpg', 'images/6.jpg',
         'images/7.jpg', 'images/8.jpg', 'images/9.jpg', 'images/10.jpg', 'images/11.jpg', 'images/12.jpg',
         'images/13.jpg', 'images/14.jpg', 'images/15.jpg', 'images/16.jpg', 'images/17.jpg',
         'images/18.jpg', 'images/19.jpg', 'images/20.jpg', 'images/21.jpg', 'images/22.jpg']


def photos(update, context):
    context.bot.send_message(update.effective_chat.id, 'Наши воспоминания')
    a = random.randint(0, (len(list3) - 1))
    with open(list3[a], 'rb') as send:
        context.bot.send_document(update.effective_chat.id, send)
    time.sleep(7)
    return klava(update, context)


def emotion(update, context):
    choices = ['Радость/Восторг ' + emoji.emojize(":zany_face:"), 'Азарт/Интерес ' + emoji.emojize(":star-struck:"),
               'Спокойствие/Ожидание ' + emoji.emojize(":thinking_face:"),
               'Раздражение/Настороженность' + emoji.emojize(":face_with_raised_eyebrow:"),
               'Грусть/Печаль/Растройство' + emoji.emojize(":sleepy_face:"),
               'Страх/Тревога ' + emoji.emojize(":weary_cat:"),
               'Злость/Раздрожение/Гнев ' + emoji.emojize(":face_with_steam_from_nose:"),
               'Апатие/Уныние/Депрессия ' + emoji.emojize(":woozy_face:")]
    message = context.bot.send_poll(update.effective_chat.id, 'Что ты сейчас чувствуешь? Можно несколько вариантов',
                                    choices, is_anonymous=False, allows_multiple_answers=True)
    payload = {
        message.poll.id: {
            'choices': choices,
            'message_id': message.message_id,
            'chat_id': update.effective_chat.id,
            'answers': 0, }}
    context.bot_data.update(payload)
    time.sleep(5)
    context.bot.send_message(update.effective_chat.id,
                             'Эти сообщения будут приходить каждый час до 22:00, а потом на основании их можно определить как прошел твой день. '
                             'Напиши боту слово Результат чтобы посмотреть результат в конце дня или в любое время. Слово результат '
                             'обнулит результаты и чтобы начать сначала нажми кнопку на клавиатуре бота')
    return message_emotion(update, context)


def emotion1(update, context):
    choices = ['Радость/Восторг ' + emoji.emojize(":zany_face:"), 'Азарт/Интерес ' + emoji.emojize(":star-struck:"),
               'Спокойствие/Ожидание ' + emoji.emojize(":thinking_face:"),
               'Настороженность' + emoji.emojize(":face_with_raised_eyebrow:"),
               'Грусть/Печаль/Расстройство' + emoji.emojize(":sleepy_face:"),
               'Страх/Тревога ' + emoji.emojize(":weary_cat:"),
               'Злость/Раздражение/Гнев ' + emoji.emojize(":face_with_steam_from_nose:"),
               'Апатие/Уныние/Депрессия ' + emoji.emojize(":woozy_face:")]
    message = context.bot.send_poll(update.effective_chat.id, 'Что ты сейчас чувствуешь? Можно несколько вариантов',
                                    choices, is_anonymous=False, allows_multiple_answers=True)
    payload = {
        message.poll.id: {
            'choices': choices,
            'message_id': message.message_id,
            'chat_id': update.effective_chat.id,
            'answers': 0, }}
    context.bot_data.update(payload)
    time.sleep(10)
    context.bot.send_message(update.effective_chat.id,
                             'Следующий вопрос через час ;) Либо пиши Результат чтобы посмотреть итоги дня')


score_answer = 0
quantity_ansvers = 0


def recive_poll_ansver(update, context):
    global quantity_ansvers
    quantity_ansvers += 1
    answer = update.poll_answer
    list_answer = answer['option_ids']
    global score_answer
    for i in list_answer:
        if i == 0:
            score_answer += 5
        if i == 1:
            score_answer += 5
        if i == 2:
            score_answer += 2
        if i == 3:
            score_answer -= 2
        if i == 4:
            score_answer -= 2
        if i == 5:
            score_answer -= 3
        if i == 6:
            score_answer -= 5
        if i == 7:
            score_answer -= 10


def alarm4(context):
    job = context.job
    context.bot.send_message(job.context, 'нажми /emotion1')


def message_emotion(update, context):
    now = datetime.datetime.now()
    a = int(now.strftime('%H'))
    a = 22 - a
    list_message = [3600, 7200, 10800, 14400, 18000, 21600, 25200, 28800, 32400, 36000, 39600, 43200, 46800, 50400,
                    54000]
    for i in range(a):
        context.job_queue.run_once(alarm4, list_message[i], context=update.effective_chat.id,
                                   name=str(update.effective_chat.id))


def message(update, context):
    a = update.message.text
    if a == 'Результат':
        result = score_answer / quantity_ansvers
        if result > 2.9:
            context.bot.send_message(update.effective_chat.id, 'это был отлтичный день')
        elif result > 0:
            context.bot.send_message(update.effective_chat.id, 'сегодняшний день был хорош')
        elif -3 < result < 0:
            context.bot.send_message(update.effective_chat.id, 'день так себе')
        else:
            context.bot.send_message(update.effective_chat.id,
                                     'день был, действительно, ужасный, подумай как сделать следующий день лучше')


def quiz_start(update, context):
    context.bot.send_message(update.effective_chat.id,
                             'Это викторина с вопросами о Любимом, будет 7 вопросов')
    time.sleep(5)
    quiz(update, context)


def quiz(update, context):
    keyboard = [
        [InlineKeyboardButton('черный', callback_data='18'), InlineKeyboardButton('синий', callback_data='19')],
        [InlineKeyboardButton('оранжевый', callback_data='20'),
         InlineKeyboardButton('зеленый', callback_data='21')],
        [InlineKeyboardButton('белый', callback_data='22'), InlineKeyboardButton('коричневый', callback_data='23')],
    ]
    context.bot.send_message(update.effective_chat.id, 'Вопрос №1: Мой любимый цвет в одежде',
                             reply_markup=InlineKeyboardMarkup(keyboard))


quiz_handler = CommandHandler('quiz', quiz)
dispatcher.add_handler(quiz_handler)


def quiz1(update, context):
    keyboard = [
        [InlineKeyboardButton('один', callback_data='24'), InlineKeyboardButton('два', callback_data='25')],
        [InlineKeyboardButton('пять', callback_data='26'),
         InlineKeyboardButton('семь', callback_data='27')],
        [InlineKeyboardButton('девять', callback_data='28'), InlineKeyboardButton('десять', callback_data='29')],
    ]
    context.bot.send_message(update.effective_chat.id, 'Вопрос №2: Какое число я выберу от 0 до 10?',
                             reply_markup=InlineKeyboardMarkup(keyboard))


quiz1_handler = CommandHandler('quiz1', quiz1)
dispatcher.add_handler(quiz1_handler)


def quiz2(update, context):
    keyboard = [
        [InlineKeyboardButton('дочка', callback_data='30'), InlineKeyboardButton('семья', callback_data='31')],
        [InlineKeyboardButton('капитал', callback_data='32'),
         InlineKeyboardButton('100кг от груди', callback_data='33')],
        [InlineKeyboardButton('директорство', callback_data='34'),
         InlineKeyboardButton('путешествие', callback_data='35')],
    ]
    context.bot.send_message(update.effective_chat.id, 'Вопрос №3: Мое самое большое достижение в жизни',
                             reply_markup=InlineKeyboardMarkup(keyboard))


quiz2_handler = CommandHandler('quiz2', quiz2)
dispatcher.add_handler(quiz2_handler)


def quiz3(update, context):
    keyboard = [
        [InlineKeyboardButton('дочка', callback_data='36'), InlineKeyboardButton('семья', callback_data='37')],
        [InlineKeyboardButton('Ты (любимая)', callback_data='38'),
         InlineKeyboardButton('капитал', callback_data='39')],
        [InlineKeyboardButton('статус', callback_data='40'), InlineKeyboardButton('кошки', callback_data='41')],
    ]
    context.bot.send_message(update.effective_chat.id, 'Вопрос №4: Самое ценное в моей жизни',
                             reply_markup=InlineKeyboardMarkup(keyboard))


quiz3_handler = CommandHandler('quiz3', quiz3)
dispatcher.add_handler(quiz3_handler)


def quiz4(update, context):
    keyboard = [
        [InlineKeyboardButton('Тунис', callback_data='42'), InlineKeyboardButton('Тайланд1', callback_data='43')],
        [InlineKeyboardButton('Тайланд2', callback_data='44'),
         InlineKeyboardButton('Кипр', callback_data='45')],
        [InlineKeyboardButton('Мармарис', callback_data='46'), InlineKeyboardButton('Паром', callback_data='47')],
    ]
    context.bot.send_message(update.effective_chat.id, 'Вопрос №5: Самое яркое путешествие?',
                             reply_markup=InlineKeyboardMarkup(keyboard))


quiz4_handler = CommandHandler('quiz4', quiz4)
dispatcher.add_handler(quiz4_handler)


def quiz5(update, context):
    keyboard = [
        [InlineKeyboardButton('Анатоля', callback_data='48'),
         InlineKeyboardButton('Денис Петрович', callback_data='49')],
        [InlineKeyboardButton('Повельев', callback_data='50'),
         InlineKeyboardButton('Ванька', callback_data='51')],
        [InlineKeyboardButton('Андрей Барышников', callback_data='52')],
    ]
    context.bot.send_message(update.effective_chat.id, 'Вопрос №6: Кто из этих людей наименее мне близок?',
                             reply_markup=InlineKeyboardMarkup(keyboard))


quiz5_handler = CommandHandler('quiz5', quiz5)
dispatcher.add_handler(quiz5_handler)


def quiz6(update, context):
    keyboard = [
        [InlineKeyboardButton('Гатчина', callback_data='53'),
         InlineKeyboardButton('Гиагинка', callback_data='54')],
        [InlineKeyboardButton('Ижевск', callback_data='55'),
         InlineKeyboardButton('Севск', callback_data='56')],
        [InlineKeyboardButton('Брянск', callback_data='57')],
    ]
    context.bot.send_message(update.effective_chat.id, 'Вопрос №7: Какой период своей жизни я считаю наиболее удачным?',
                             reply_markup=InlineKeyboardMarkup(keyboard))


quiz6_handler = CommandHandler('quiz6', quiz6)
dispatcher.add_handler(quiz6_handler)


def quiz_answer(update, context):
    if quiz_score >= 6:
        context.bot.send_message(update.effective_chat.id, 'Ты знаешь меня на все 100!')
        context.bot.send_message(update.effective_chat.id, emoji.emojize(":revolving_hearts:"))
        time.sleep(3)
        return klava(update, context)
    else:
        context.bot.send_message(update.effective_chat.id, 'А я оказался не так прост')
        context.bot.send_message(update.effective_chat.id, emoji.emojize(":man_shrugging:"))
        time.sleep(3)
        return klava(update, context)


def remove_job(name, context):
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    else:
        for job in current_jobs:
            job.schedule_removal()
        return True


def stop_timers(update, context):
    job_removed = remove_job(str(update.effective_chat.id), context)
    if job_removed:
        text = 'Все повторяющие процессы остановлены'
    else:
        text = 'Нет запущенных процессов'
    context.bot.send_message(update.effective_chat.id, text)


start_handler = CommandHandler('start', start)
klava_handler = CommandHandler('klava', klava)
button_handler = CallbackQueryHandler(button)
day_week_handler = CommandHandler('day', day_week)
emotion_handler = CommandHandler('emotion', emotion)
emotion1_handler = CommandHandler('emotion1', emotion1)
photo_handler = MessageHandler(Filters.document.category('image'), photo)
message_handler = MessageHandler(Filters.text, message)
recive_poll_ansver_handler = PollAnswerHandler(recive_poll_ansver)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(klava_handler)
dispatcher.add_handler(button_handler)
dispatcher.add_handler(day_week_handler)
dispatcher.add_handler(photo_handler)
dispatcher.add_handler(emotion_handler)
dispatcher.add_handler(emotion1_handler)
dispatcher.add_handler(message_handler)
dispatcher.add_handler(recive_poll_ansver_handler)

updater.start_polling()
updater.idle()
