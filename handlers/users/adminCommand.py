import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove
from keyboards.default.adminKeyb import admKey, dbKey
from keyboards.default.backKeyb import back
from keyboards.default.mainKeyb import mainMenu
from states.registState import rek
from data.config import ADMINS
from loader import dp, db, bot
from environs import Env
import os
env = Env()
env.read_env()


id_pattern = r'(?<!\d)\d{9}(?!\d)'
def validate_id(id):
    return bool(id_pattern.find(id))


@dp.message_handler(Command('panel'), user_id=ADMINS)
async def panel(msg: types.Message):
    await msg.answer("Siz adminsiz, quyidagi funksiyalardan foydalanishinggiz mumkin", reply_markup=admKey)

@dp.message_handler(text="📊Statistika", user_id=ADMINS)
async def statis(msg: types.Message):
    userCount = db.count_users()
    await msg.answer(f"Botinggizdan foydalanuvchilar soni {userCount} tani tashkil etadi")

@dp.message_handler(text="🙋‍♂️Barcha foydalanuvchilar", user_id=ADMINS)
async def get_all_users(message: types.Message):
    try:
        users = db.select_all_users()
        allUser = ""
        i = 1
        for user in users:
            allUser += f"{i}. {user} \n"
            i+=1
            print(users[0][0])
        await message.answer(allUser)
    except:
        await message.answer("Botinggizda foydalanuvchilar mavjud emas")


@dp.message_handler(text="®️Reklama yuborish", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    await message.answer("Userlarga jo'natmoqchi bo'lgan habaringgizni yuboring", reply_markup=ReplyKeyboardRemove())
    await rek.command.set()



@dp.message_handler(state=rek.command)
async def reksend(msg: types.message, state: FSMContext):
    textrek = msg.text
    users = db.select_all_users()
    await msg.answer("Habaringgiz obunachilarga yuborildi", reply_markup=admKey)
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text=textrek)
        await asyncio.sleep(0.5)

    await state.finish()


@dp.message_handler(state=rek.sendrek)
async def sendmsg(msg: types.Message, state: FSMContext):
    await state.finish()

@dp.message_handler(text="❎Bazani tozalash", user_id=ADMINS)
async def get_all_users(message: types.Message):
    await message.answer("Siz haqiqatdan ham barcha foydalanuvchilar ro'yhatini tozalamoqchimisiz?", reply_markup=dbKey)



@dp.message_handler(text="✅Tasdiqlash", user_id=ADMINS)
async def cleanuser(msg: types.Message):
    db.delete_users()
    await msg.answer("Baza tozalandi!", reply_markup=admKey)

@dp.message_handler(text="❌Bekor qilish", user_id=ADMINS)
async def atmen(msg: types.Message):
    await msg.answer("Quyidagi funksiyalardan foydalanishinggiz mumkin", reply_markup=admKey)

@dp.message_handler(text="👨‍💻Adminlar", user_id=ADMINS)
async def adminlar(msg: types.Message):

    adminss = "Adminlar ro'yhati. \n\n"
    for index, admin in enumerate(ADMINS, start=1):
        adminss += f"{index} {admin}\n"
    await msg.answer(adminss)



@dp.message_handler(text="🔙Panelga qaytish", user_id=ADMINS)
async def backbtn(msg: types.Message, state: FSMContext):
    await msg.answer("Quyidagi funksiyalardan foydalanishinggiz mumkin", reply_markup=admKey)
    await state.finish()

@dp.message_handler(text="🔙Bosh menyuga qaytish")
async def mainmn(msg: types.Message):
    await msg.answer("Siz bosh menyudasiz:", reply_markup=mainMenu)