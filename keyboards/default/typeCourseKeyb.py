from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

courseKeyb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👨‍💻Full-stack"),
        ],
        [
            KeyboardButton(text="🤖Software Engineering"),
        ],
        [
            KeyboardButton(text="⚙️Data Science"),
        ],
        [
            KeyboardButton(text="🔙 Ortga qaytish")
        ],
    ],
    resize_keyboard=True
)

