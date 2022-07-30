from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp

from message_texts import texts as t
from help_functions.sql import user as u
from keyboards.inline.mane_kb import main_menu
from help_functions.sql import other_sql as o_sql


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    print(message.from_user.username)
    user_id = message.from_user.id
    if not u.check_user(user_id):
        o_sql.fill_dict(user_id)
        o_sql.fill_weight(user_id)
        await message.answer(f"Привет, {message.from_user.full_name}!")
        u_name = message.from_user.username
        await message.answer(t.hello_text)
        u.main_info_fill((user_id, u_name))
    await message.answer(t.menu_text, reply_markup=main_menu())


