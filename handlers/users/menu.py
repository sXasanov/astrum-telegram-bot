from aiogram import types
from keyboards.default.typeCourseKeyb import courseKeyb
from loader import dp

@dp.message_handler(text="📝 Yo'nalishlar")
async def course(msg: types.Message):
    await msg.answer("Kerakli kurslardan birini tanlang", reply_markup=courseKeyb)



@dp.message_handler(text="📥 Bog’lanish")
async def connect(msg: types.Message):
    msgtext = "Biz bilan bog’lanish uchun:\n\n☎️ +99893 111 11 11\n👩🏻‍💻 @Astrum_admin"
    await msg.answer_photo(caption=msgtext, photo="AgACAgIAAxkBAAICNWR56AoQ9cYjmRsVJB_gy7ehgvkvAAILzDEbi3vRS9ocFaseT7L7AQADAgADeQADLwQ")

