from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Sherik kerak"), KeyboardButton(text="Ish joyi kerak")],
        [KeyboardButton(text="Hodim kerak"), KeyboardButton(text="Ustoz kerak")],
        [KeyboardButton(text="Shogird kerak")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Bulimdan birini tanla",
    one_time_keyboard=True
)