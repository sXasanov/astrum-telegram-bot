from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

mainMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📝 Yo'nalishlar"),
            KeyboardButton(text="📥 Bog’lanish"),
        ],
    ],
    resize_keyboard=True
)