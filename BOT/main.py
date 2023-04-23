from src.classes.Application import Application
from src.classes.Config import Config
from src.extensions.keyboards.KeyboardWrapper import KeyboardWrapper


if __name__ == '__main__':
    config_file = open('config/env')
    config = Config(file=config_file)
    config_file.close()

    greet_kb = KeyboardWrapper()
    greet_kb.add_button(text="/🖥ВЫКЛЮЧИТЬ🖥", description='мгновенное выключение компьютера')\
        .add_button("/♻️Перезагрузить♻️", description='мгновенная перезагрузка компьютера')\
        .add_button("/📸КАМЕРА📸", description='сделать фото')\
        .add_button("/📸СКРИНШОТ📸", description='фотография рабочего стола')\
        .add_button("/🔒ПАРОЛЬ🔒", description='заблокировать экран для разблокировки ввести пароль')\
        .add_button("/💾ДИСКИ💾", description='узнать сколько свободного места на жестких дисках')\
        .add_button("/💻ХАРАКТЕРИСТИКИ💻", description= 'вывести характеристики вашего ПК')\
        .add_button("/🧿АЙПИ🧿", description='выводит ваш актуальный ip адресс')\
        .add_button("/☀️ЯРКОСТЬ☀️", description='изменяет яркость вашего экрана')\
        .add_button("/🌡ТЕМПЕРАТУРА🌡", description='поможет узнать температуру вашего процессора, возможно и видеокарты')\
        .add_button("/⌨️ГОРЯЧИЕ_КЛАВИШИ⌨️", description='выводит список доступных горячих клавиш')\


    brightness_kb = BrightnessKeyboard()
    brightness_kb.add_button(text="/25")\
        .add_button("/50")\
        .add_button("/75")\
        .add_button("/100")\
        .add_button("/⏹")

    hotkeys_kb = HotkeysKeyboard()
    hotkeys_kb.add_button(text="/CTRL+SHIFT+ESC") \
        .add_button("/WIN+A")\
        .add_button("/WIN+D")\
        .add_button("/⏹")

    application = Application(config, greet_kb, brightness_kb, hotkeys_kb)

    application.register_handlers()

    application.run()
