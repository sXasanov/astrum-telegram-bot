from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admKey = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👨‍💻Adminlar"),
        ],
        [
            KeyboardButton(text="📊Statistika"),
            KeyboardButton(text="🙋‍♂️Barcha foydalanuvchilar"),
        ],
        [
            KeyboardButton(text="®️Reklama yuborish"),
            KeyboardButton(text="❎Bazani tozalash"),
        ],
        [
            KeyboardButton(text="🔙Bosh menyuga qaytish")
        ],
    ],
    resize_keyboard=True
)

dbKey = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅Tasdiqlash"),
            KeyboardButton(text="❌Bekor qilish"),
        ],
    ],
    resize_keyboard=True
)

#
# thank = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text="😊Rahmat"),
#         ],
#     ],
#     resize_keyboard=True
# )