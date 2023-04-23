from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


class KeyboardWrapper:
    def __init__(self, resize_keyboard=True):
        self.__keyboard = ReplyKeyboardMarkup(resize_keyboard=resize_keyboard)
        self.__help = dict()
        self.__brightness = ReplyKeyboardMarkup(resize_keyboard=resize_keyboard)
        self.__hotkeys = ReplyKeyboardMarkup(resize_keyboard=resize_keyboard)
        self.__mouse = ReplyKeyboardMarkup(resize_keyboard=resize_keyboard)


    def add_button(self, text, description):
        button = KeyboardButton(text)

        self.__help[text] = description
        self.__keyboard.add(button)
        self.__brightness.add(button)
        self.__hotkeys.add(button)
        self.__mouse.add(button)

        return self

    @property
    def keyboard(self):
        return self.__keyboard
   
   @property
    def brightness(self):
        return self.__brightness

    @property
    def hotkeys(self):
        return self.__hotkeys

    @property
    def mouse(self):
        return self.__mouse

    @property
    def help(self):
        content = ''
        for key in self.__help:
            content += key + ' - ' + self.__help.get(key) + '\n'

        return content
