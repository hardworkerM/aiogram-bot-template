from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

from message_texts import texts as txx
from states.nw_state import nw
from handlers.users.start import bot_start
from help_functions.sql.nw_sql import add_word


@dp.callback_query_handler(text='add')
async def user_word(call: CallbackQuery, state: FSMContext):
    await call.message.answer(txx.new_word)
    await nw.eng_w.set()


@dp.message_handler(state=nw.eng_w)
async def nw_take_eng(message: types.Message, state: FSMContext):
    #Запомнили англ слово
    async with state.proxy() as data:
        data['en_w'] = message.text
    # Просим перевод
    await message.answer(txx.ru_word)
    await nw.rus_w.set()


@dp.message_handler(state=nw.rus_w)
async def nw_take_eng(message: types.Message, state: FSMContext):
    #Запомнили англ слово
    data = await state.get_data()
    en_w = data['en_w']
    ru_w = message.text
    user_id = message.from_user.id
    # Записываем слово
    add_word(user_id, en_w, ru_w)
    # Завершаем, вызываем меню
    await message.answer("Спасибо! Будем учить")
    await state.finish()
    await bot_start(message)
