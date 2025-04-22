from aiogram.types import  KeyboardButton, ReplyKeyboardMarkup

btn_keyboard=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="LEVEL 1"),
         KeyboardButton(text="LEVEL 2"),],
        [KeyboardButton(text="LEVEL 3"),
        KeyboardButton(text="LEVEL 4"),]],resize_keyboard=True,)

stop_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="STOP"),]
    ],resize_keyboard=True,
)