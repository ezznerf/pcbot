from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

markup = ReplyKeyboardMarkup(resize_keyboard = True)
btn_hello = KeyboardButton("/🖥ВЫКЛЮЧИТЬ🖥")

btn_screen = KeyboardButton("/📸СКРИНШОТ📸")

btn_video = KeyboardButton("/📹ВИДЕО📹")

btn_trash = KeyboardButton("/🚮УДАЛИТЬ🚮")

btn_characteristics = KeyboardButton("/💻ХАРАКТЕРИСТИКИ💻")

btn_restart = KeyboardButton("/♻️Перезагрузить♻️")

btn_locker = KeyboardButton("/🔒ПАРОЛЬ🔒")

btn_secret = KeyboardButton("/🤖ДОП🤖")

btn_help = KeyboardButton("/help")

btn_stop = KeyboardButton('/📸КАМЕРА📸')

btn_cmd = KeyboardButton('/cmd')

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_hello).add(btn_screen).add(btn_trash).add(btn_restart).add(btn_locker).add(btn_stop).add(btn_secret).add(btn_cmd).add(btn_help).add(btn_video)

btn_disks = KeyboardButton('/💾ДИСКИ💾')

btn_temp = KeyboardButton('/🌡ТЕМПЕРАТУРА🌡')

btn_back = KeyboardButton('/◀️')

secret_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_characteristics).add(btn_disks).add(btn_temp).add(btn_back)



video_kb = ReplyKeyboardMarkup(resize_keyboard= True).add(btn_stop)
