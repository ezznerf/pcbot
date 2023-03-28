from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


class HotkeysKeyboard:
    def __init__(self, resize_keyboard=True):
        self.__hotkeys = ReplyKeyboardMarkup(resize_keyboard=resize_keyboard)
    def add_button(self, text):
        button = KeyboardButton(text)
        self.__hotkeys.add(button)
        return self

    @property
    def hotkeys(self):
        return self.__hotkeys