from aiogram.dispatcher.filters.state import State, StatesGroup


class learning_w(StatesGroup):
    process = State()
    choose_weight = State()
    done = State()