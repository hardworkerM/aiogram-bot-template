"""
Хендлер для проверки знаний слов
Будет идти пока не закончится

"""

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

from states.learn_state import learning_w
from message_texts import texts as t
from help_functions.sql import user as u
from keyboards.inline import mane_kb as kb
from help_functions.sql import weight_sql as w_sql
from help_functions.sql import other_sql as o_sql
from message_texts import texts as tx
from handlers.users.start import bot_start
import random
import datetime


def count_time(start, end):
    space = end - start
    time_list = str(space).split(":")
    time_list[2] = time_list[2].split(".")[0]
    time_list = [int(i) for i in time_list]
    h, m, s = time_list
    time = h * 360 + m * 50 + s
    return time


def take_word(user_id):
    """
    Function return word to show user.
    //Checking with previous will be added
    """
    word_dict = w_sql.take_weights(user_id)
    words = list(word_dict.keys())
    weight = list(word_dict.values())
    print(weight, words)
    word = (random.choices(words, weights=weight))
    print(word)
    return word[0]


@dp.callback_query_handler(text='learn')
async def give_word(call: CallbackQuery, state: FSMContext):
    word = take_word(call.from_user.id)
    await call.message.answer(f"<b>{word}</b>"+tx.learn_text, reply_markup=kb.was_lerned(word))
    await learning_w.process.set()
    async with state.proxy() as data:
        data['id'] = call.from_user.id
        data['word'] = word
        data['time'] = datetime.datetime.now()


@dp.message_handler(state=learning_w.process)
async def check_translate(message: types.Message, state: FSMContext):
    data = await state.get_data()
    word = data['word']
    translate = message.text
    correct = o_sql.give_translate_r(word)
    if translate == correct:
        ans = 1
        await message.answer(tx.correct, reply_markup=kb.show_more_kb())
    else:
        ans = 0
        await message.answer(f'<b>{correct}</b>' + tx.incorrect,
                             reply_markup=kb.show_more_kb())
    async with state.proxy() as data:
        data['ans'] = ans
        data['end'] = datetime.datetime.now()
    await learning_w.choose_weight.set()


@dp.callback_query_handler(text='more', state=learning_w.choose_weight)
async def weight_hire(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    word = data['word']
    user_id = call.from_user.id
    ans = data['ans']
    time = count_time(data['time'], data['end'])
    w_sql.fill_data(user_id, word, ans, time, 1)
    await call.answer("Спасибо ❤")
    await give_word(call, state)


@dp.callback_query_handler(text='less', state=learning_w.choose_weight)
async def weight_hire(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    word = data['word']
    user_id = call.from_user.id
    ans = data['ans']
    time = count_time(data['time'], data['end'])
    w_sql.fill_data(user_id, word, ans, time, -1)
    await call.answer("Спасибо ❤")
    await give_word(call, state)


@dp.message_handler(state=learning_w.choose_weight)
async def remark(message: types.Message, state: FSMContext):
    await message.answer("Пожалуйста, нажмите на одну из кнопок выше, потом вы сможете выйти")


@dp.callback_query_handler(lambda x: 'was' in x.data, state=learning_w.process, )
async def delete_word(call: CallbackQuery, state: FSMContext):
    word = call.data[3:]
    await call.message.answer("Это слово мы вам больше не покажем")
    o_sql.delete_word(call.from_user.id, word)
    await give_word(call, state)


@dp.callback_query_handler(state=learning_w.process, text='out')
async def end_proccess(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await bot_start(call.message)






