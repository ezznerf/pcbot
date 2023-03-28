from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


class BrightnessKeyboard:
    def __init__(self, resize_keyboard=True):
        self.__brightness = ReplyKeyboardMarkup(resize_keyboard=resize_keyboard)
    def add_button(self, text):
        button = KeyboardButton(text)
        self.__brightness.add(button)
        return self

    @property
    def brightness(self):
        return self.__brightness
