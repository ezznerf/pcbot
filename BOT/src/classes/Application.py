from aiogram import types
from src.classes.Config import Config
from src.classes.WindowsOS import WindowsOS
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram import Bot, types



class Application:

    def __init__(self, config: Config, keyboard, keyboard2, keyboard3):
        self.__config = config
        self.__keyboard = keyboard
        self.__brightness = keyboard2
        self.__hotkeys = keyboard3
        self.__bot = Bot(token=config.get_param('token'))
        self.__dp = Dispatcher(self.__bot)

        os = config.get_param('os')
        if os is None:
            raise Exception('Not found os')
        if os == 'linux':
            # self.__os = LinuxOS(self.__dp, self.__bot, self.__config, self.__keyboard)
            pass
        elif os == 'windows':
            self.__os = WindowsOS(self.__dp, self.__bot, self.__config, self.__keyboard.keyboard)
        else:
            raise Exception('Not found support os')

    async def show_help(self, message: types.Message):
        await self.__bot.send_message(message.from_user.id, self.__keyboard.help, reply_markup=self.__keyboard.keyboard)

    async def show_main_keyboard(self, message: types.Message):
        await self.__bot.send_message(message.from_user.id, "Главное меню!", reply_markup=self.__keyboard.keyboard)

    async def show_brightness(self, message: types.Message):
        await self.__bot.send_message(message.from_user.id, text='Выберите яркость вашего экрана', reply_markup=self.__brightness.brightness)


    async def show_hotkeys(self, message: types.Message):
        await self.__bot.send_message(message.from_user.id, text='Выберите сочетание клавиш', reply_markup=self.__hotkeys.hotkeys)


    def register_handlers(self):
        self.__dp.register_message_handler(self.show_help, commands=['help'])
        self.__dp.register_message_handler(self.__os.screenshot, commands=["📸СКРИНШОТ📸"])
        self.__dp.register_message_handler(self.__os.make_photo, commands=["📸КАМЕРА📸"])
        self.__dp.register_message_handler(self.__os.shutdown, commands=["🖥ВЫКЛЮЧИТЬ🖥"])
        # self.__dp.register_message_handler(self.__os.disk_area, commands=["🚮УДАЛИТЬ🚮"])
        self.__dp.register_message_handler(self.__os.win_locker, commands=["🔒ПАРОЛЬ🔒"])
        self.__dp.register_message_handler(self.__os.reboot, commands=["♻️Перезагрузить♻️"])
        self.__dp.register_message_handler(self.__os.disk_area, commands=["💾ДИСКИ💾"])
        self.__dp.register_message_handler(self.__os.charac, commands=["💻ХАРАКТЕРИСТИКИ💻"])
        self.__dp.register_message_handler(self.__os.ip_get, commands=["🧿АЙПИ🧿"])
        self.__dp.register_message_handler(self.show_brightness, commands=["☀️ЯРКОСТЬ☀️"])
        self.__dp.register_message_handler(self.__os.brightness25, commands=["25"])
        self.__dp.register_message_handler(self.__os.brightness50, commands=["50"])
        self.__dp.register_message_handler(self.__os.brightness75, commands=["75"])
        self.__dp.register_message_handler(self.__os.brightness100, commands=["100"])
        self.__dp.register_message_handler(self.show_main_keyboard, commands=["⏹"])
        self.__dp.register_message_handler(self.__os.temperature, commands=["🌡ТЕМПЕРАТУРА🌡"])
        self.__dp.register_message_handler(self.show_hotkeys, commands=["⌨️ГОРЯЧИЕ_КЛАВИШИ⌨️"])
        self.__dp.register_message_handler(self.__os.ctrl_shift_esc, commands=["CTRL+SHIFT+ESC"])
        self.__dp.register_message_handler(self.__os.win_a, commands=["WIN+A"])
        self.__dp.register_message_handler(self.__os.win_d, commands=["WIN+D"])

    def run(self):
        executor.start_polling(self.__dp, skip_updates=True)