import sqlite3
import time
from datetime import datetime

from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import re
from data.config import ADMINS
from keyboards.default.mainKeyb import mainMenu
from loader import dp, db, bot
from states.registState import newUser



name_pattern = re.compile(r'^[A-Za-z]+\s[A-Za-z]+$')
email_pattern = re.compile(r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+')
phone_number_pattern = re.compile(r'^\+998\d{9}$')

def validate_name(name):
    return bool(name_pattern.match(name))
def validate_email(email):
    return bool(email_pattern.match(email))

def validate_phone_num(phonenum):
    return bool(phone_number_pattern.match(phonenum))

@dp.message_handler(CommandStart(), user_id=ADMINS)
async def foradmin(msg: types.Message):
    await msg.answer("Siz adminsiz va siz ro'yhatdan o'tishinggiz shart emas.", reply_markup=mainMenu)

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    name = message.from_user.full_name
    try:
        # Check if the user already exists in the database
        existing_user = db.select_user(id=user_id)

        if existing_user:
            await message.answer("Assalomu alaykum! Sizga qanday yordam bera olamiz!😊", reply_markup=mainMenu)
        else:
            db.add_user(id=user_id, name=name)
            await newUser.fullname.set()
            await message.answer(
                "Assalomu alaykum, Astrum IT academy ning rasmiy botiga Xush kelibsiz!😊 \n\nBotdan foydalanish uchun ro'yhatdan o'ting. \n\nIsm va familiyanggizni kiriting:")

    except sqlite3.Error as err:
        print(err)
        print('\nerr nomli error')

        await message.answer("Xatolik yuz berdi. Iltimos, qaytadan urinib ko'ring.")

    except Exception as e:
        print(e)
        await message.answer("Assalomu alaykum! Sizga qanday yordam bera olaman!😊", reply_markup=mainMenu)


@dp.message_handler(state=newUser.fullname)
async def process_name(message: types.Message, state: FSMContext):
    if validate_name(message.text):
        name = message.text
        await state.update_data(
            {'name': name}
        )
        # Ask for the email
        await newUser.next()
        await message.answer('Iltimos emailinggizni kiriting')
    else:
        await message.answer("Ismda xatolik, Ism va familiyanggizni qayta kiriting")




@dp.message_handler(state=newUser.email)
async def process_email(message: types.Message, state: FSMContext):
    if validate_email(message.text):
        email = message.text
        # Store the email in the state data
        await state.update_data(
            {'email': email}
        )
        await newUser.next()
        await message.answer("Iltimos telefon raqaminggizni kiriting")
    else:
        await message.answer("Emailda xatolik, emailni qayta kiriting")



@dp.message_handler(state=newUser.phoneNum)
async def process_email(message: types.Message, state: FSMContext):
    if validate_phone_num(message.text):
        phone = message.text
        # Store the email in the state data
        await state.update_data(
            {'phone': phone}
        )
        await newUser.next()
        await message.answer("Sizning malumotlaringgiz adminga yuborildi, Endi sizga qanday yordam bera olaman", reply_markup=mainMenu)

        data = await state.get_data()
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')

        msg = f"Botdan yangi user ro'yhatdan o'tdi \n\n"
        msg += f"Ismi va Familyasi: {name} \n"
        msg += f"Email adresi: {email}\n"
        msg += f"Telefon raqami: {phone}"

        await bot.send_message(ADMINS[0], msg)
        await state.finish()

        db.update_user_email(email=email, id=message.from_user.id)
    else:
        await message.answer("Telefon raqamda xatolik mavjud. Iltimos qayta kiriting")


