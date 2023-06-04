from aiogram.dispatcher.filters.state import StatesGroup, State


class newUser(StatesGroup):
    fullname = State()
    email = State()
    phoneNum = State()

class rek(StatesGroup):
    command = State()
    sendrek = State()

