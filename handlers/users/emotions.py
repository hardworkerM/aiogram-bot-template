from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from states.take_grif import grief
from help_functions.sql import sql_saf as sql_bad


@dp.message_handler(text='Грусть моя')
async def remember_memories(message: types.Message, state: FSMContext):
    await message.answer("Готов слушать\nПотом запишу")
    await grief.sad.set()


@dp.message_handler(state=grief.sad)
async def take_grief(message: types.Message, state: FSMContext):
    grief = message.text
    await message.answer("Ничего, друг. Забей хУй")
    sql_bad.remember_sad(message.from_user.id, grief)
    await state.finish()


@dp.message_handler(text = "Почему мне грустно")
async def show_all_sad(message: types.Message):
    text = sql_bad.show_sadness(message.from_user.id)
    await message.answer(text)

