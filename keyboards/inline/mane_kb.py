from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu(flag=0):
    markup = InlineKeyboardMarkup()
    m2 = InlineKeyboardMarkup()

    btn1 = InlineKeyboardButton("Учить", callback_data='learn')
    btn2 = InlineKeyboardButton("Добавить", callback_data='add')
    btn3 = InlineKeyboardButton("слова", callback_data='МОИ')

    markup.add(btn1, btn2, btn3)
    m2.add(btn1, btn2)
    if flag == 1:
        return m2
    return markup


def show_more_kb():
    markup = InlineKeyboardMarkup()

    btn1 = InlineKeyboardButton("Чаще", callback_data='more')
    btn2 = InlineKeyboardButton("Реже", callback_data='less')

    markup.add(btn1, btn2)
    return markup


def word_learned_kb():
    markup = InlineKeyboardMarkup()

    btn1 = InlineKeyboardButton("Выучил", callback_data='done')
    btn2 = InlineKeyboardButton("Ещё нет", callback_data='not_yet')
    btn3 = InlineKeyboardButton("Закончить", callback_data='end')

    markup.add(btn1, btn2, btn3)
    return markup


def back_btn():
    back = InlineKeyboardButton("Назад", callback_data='back')

    return back


def was_lerned(word):
    markup = InlineKeyboardMarkup()

    was = InlineKeyboardButton("знаю", callback_data=f'was{word}')
    out = InlineKeyboardButton("выйти", callback_data='out')

    markup.add(was, out)

    return markup
