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
        .add_button("/🖱МЫШЬ🖱", description='(BETA)управление мышью(BETA)')

    brightness_kb = KeyboardWrapper()
    brightness_kb.add_button(text="/25", description=False)\
        .add_button("/50", description=False)\
        .add_button("/75", description=False)\
        .add_button("/100", description=False)\
        .add_button("/⏹", description=False)

    hotkeys_kb = KeyboardWrapper()
    hotkeys_kb.add_button(text="/CTRL+SHIFT+ESC", description=False) \
        .add_button("/WIN+A", description=False)\
        .add_button("/WIN+D", description=False)\
        .add_button("/⏹", description=False)
        
    mouse_kb = KeyboardWrapper()
    mouse_kb.add_button("/⬆️", description=False)\
        .add_button("/⬅️", description=False)\
        .add_button("/➡️", description=False)\
        .add_button("/⬇️", description=False)\
        .add_button("/press", description=False)\
        .add_button("/⏹", description=False)

    application = Application(config, greet_kb, brightness_kb, hotkeys_kb)

    application.register_handlers()

    application.run()
