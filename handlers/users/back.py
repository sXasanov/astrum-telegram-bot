from aiogram import types

from keyboards.default.mainKeyb import mainMenu
from loader import dp


@dp.message_handler(text="🔙 Ortga qaytish")
async def back(msg: types.Message):
    await msg.answer("Siz bosh menyudasiz, Kerakli bo'limlardan birini tanlang", reply_markup=mainMenu)