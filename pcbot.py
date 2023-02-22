
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor 
import time, subprocess
import keyboard as kb 
import os

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
	await bot.send_message(message.from_user.id, "ZNERF Давай это сделаем ZNERF ", reply_markup=kb.greet_kb )
	
@dp.message_handler(commands=['🖥ВЫКЛЮЧИТЬ🖥'])
async def process_start_command(message: types.Message):
	await bot.send_message(message.from_user.id, "Выключаю...")
	await os.system('shutdown -s')

if __name__ == '__main__':
    executor.start_polling(dp)
