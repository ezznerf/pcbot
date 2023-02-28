
import cv2
import asyncio
import GPUtil
import psutil
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import wmi 
import keyboard
from pynput.mouse import Button, Controller
import aiogram
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor 
import time, subprocess
import keyboards as kb 
import os
import pyautogui
from time import sleep
from config import TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

mouse = Controller()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class FSMAD(StatesGroup):
	delets = State()
	passww = State()
#class FSMAS(StatesGroup):
#	passww = State()
#cap = cv2.VideoCapture(0)
#fps = 20.0
#image_size = (640,480)
#video_file = 'res.mp4'

#out = cv2.VideoWriter(video_file, cv2.VideoWriter_fourcc(*'XVID'), fps, image_size)
#def vid():
#	while True:
#		ret, frame = cap.read()
#		cv2.imshow("camera", frame)
#		out.write(frame)
#		if cv2.waitKey(10) == 27:
#			break

#	cap.release()
#	cv2.destroyAllWindows()
#	print("SAVED")

def screen():
	screenshot = pyautogui.screenshot()
	screenshot.save('screenshot.png')

def update():   
    mouse.position = (1920/2, 1080/2)
    mouse.press(Button.left)
    mouse.release(Button.left)
    keyboard.press('f5')	
    
def message():
	@dp.message_handler(content_types=["text"])
	def input_trash(message:types.Message):
		textik = message.text


computer = wmi.WMI()
computer_info = computer.Win32_ComputerSystem()[0]
os_info = computer.Win32_OperatingSystem()[0]
proc_info = computer.Win32_Processor()[0]
gpu_info = computer.Win32_VideoController()[0]

os_version = ' '.join([os_info.Version, os_info.BuildNumber])
system_ram = float(os_info.TotalVisibleMemorySize) / 1048576

characteristics = 'OS Name: Windows 10' +'\n' +'OS Version: {0}'.format(os_version) + '\n' + 'CPU: {0}'.format(proc_info.Name) + '\n' + 'RAM: {0} GB'.format(system_ram) + '\n' + 'Graphics Card: {0}'.format(gpu_info.Name)



helptxt = '    🖥ВЫКЛЮЧИТЬ🖥 - мгновенное выключение компьютреа \n \n   📸СКРИНШОТ📸 - фотография рабочего стола \n \n   🚮УДАЛИТЬ🚮 - удаленние файла (требуется в ручную ввести название файла)\n \n   ♻️Перезагрузить♻️ - мгновенная перезагрузка компьютера \n \n   🔒ПАРОЛЬ🔒 - выводит на весь экран окно требующее пароль(после использования потребует придумать пароль) \n \n   '\
'🤖ДОП🤖 - открывает дополнительное меню для отслеживания состояния компьютера \n \n   💻ХАРАКТЕРИСТИКИ💻 - выводит характеристики вашего компьютера  \n \n   💾ДИСКИ💾 - свободное место на дисках в процентах \n \n   🌡ТЕМПЕРАТУРА🌡 - температура видеокарты и процессора'

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
	await bot.send_message(message.from_user.id, "ZNERF Давай это сделаем ZNERF ", reply_markup=kb.greet_kb)
	
@dp.message_handler(commands=['🖥ВЫКЛЮЧИТЬ🖥'])
async def process_start_command(message: types.Message):
	await bot.send_message(message.from_user.id, "Выключаю...")
	await os.system('shutdown -s -t 0')

@dp.message_handler(commands=['📸СКРИНШОТ📸'])
async def process_start_command(message: types.Message):
	screen()
	file = open('screenshot.png', 'rb')
	await bot.send_photo(message.chat.id,file, 'Вот скрин вашего экрана')
	
def deleater(textik):
	deleter = 'C:\\Users\\yakut\\Desktop\\'+ textik
	os.remove (deleter)

@dp.message_handler(commands= ['🚮УДАЛИТЬ🚮'], state= None)
async def del_func(message: types.Message):
	await FSMAD.delets.set()
	await bot.send_message(message.chat.id, "Напишите название файла который хотите удалить")	

@dp.message_handler(content_types=['text'], state = FSMAD.delets)
async def load_delle(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['deletes'] = message.text
		global textik
		textik = data['deletes']
		deleter = 'C:\\Users\\yakut\\Desktop\\'+ textik
		os.remove (deleter)
		await state.finish()
		
@dp.message_handler(commands=['💻ХАРАКТЕРИСТИКИ💻'])
async def process_start_command(message: types.Message):
	await bot.send_message(message.from_user.id, characteristics)

@dp.message_handler(commands=['♻️Перезагрузить♻️'])
async def process_start_command(message: types.Message):
	await bot.send_message(message.from_user.id, 'Перезапускаю...')
	await os.system('shutdown -r -t 0')

@dp.message_handler(commands= ['🔒ПАРОЛЬ🔒'], state= None)
async def pas_func(message: types.Message):
	await FSMAD.passww.set()
	await bot.send_message(message.chat.id, "Напишите пароль")		

@dp.message_handler(state= FSMAD.passww)
async def load_pass(message:types.Message, state: FSMContext):
		async with state.proxy() as data:
			data['passww'] = message.text
			global passw
			passw = data['passww']
			def btn_click():
				k = ent.get()
				if k == passw:
					root.destroy()
			root = Tk()
			root.title('Windows has Locked')
			root.attributes("-fullscreen",True)
			root.geometry('400x200')
			frame = Frame(root)
			frame.place(relx=0.20, rely = 0.30, relwidth=0.6, relheight= 0.7)
			Label(frame, text= "Enter password", font = 'Arial 25', fg = 'white').pack()
			ent = Entry(frame, text = '', font = 'Arial 25', width=15)
			ent.pack()
			tk.Button(frame, text = 'Unlock', font='Arial 25', bg = 'red', fg = 'white', command=btn_click).pack()
			
			root.mainloop()
			await state.finish()
		

@dp.message_handler(commands=['🤖ДОП🤖'])
async def process_start_command(message: types.Message):
	await bot.send_message(message.from_user.id, 'Вы открыли дополнительное меню !', reply_markup=kb.secret_kb)		

@dp.message_handler(commands=['◀️'])
async def process_start_command(message: types.Message):
	await bot.send_message(message.from_user.id, 'Главное меню' ,reply_markup=kb.greet_kb)		


@dp.message_handler(commands=['💾ДИСКИ💾'])
async def process_start_command(message: types.Message):
	os.system('chcp 65001')
	conn = wmi.WMI()
	for disk in conn.Win32_LogicalDisk():
		if disk.size != None:
			await bot.send_message(message.from_user.id, ("Disk " + disk.Caption, "is {0:.2f}% free".format(
            100 * float(disk.FreeSpace) / float(disk.Size))))

@dp.message_handler(commands=['🌡ТЕМПЕРАТУРА🌡'])
async def process_start_command(message: types.Message):
	w = wmi.WMI(namespace='root\\wmi', privileges=["Security"])
	temperature = w.MSAcpi_ThermalZoneTemperature()[0]
	temperature = int(temperature.CurrentTemperature / 10.0 - 273.15)
	print(f'CPU temp: {temperature}.0 °C')
	gpus = GPUtil.getGPUs()
	for gpu in gpus:
		#global gpu_temperature 
		gpu_temperature = f"{gpu.temperature} °C"
	await bot.send_message(message.from_user.id,  f'CPU temp: {temperature}.0 °C' '\n' "GPU temp: " + gpu_temperature)

@dp.message_handler(commands=['cmd'])
async def process_start_command(message: types.Message):
	await bot.send_message(message.chat.id, "Напишите команду")
	os.startfile(r'C:\Users\yakut\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Command Prompt.lnk')
	@dp.message_handler(content_types=["text"])
	def cmddd(message:types.Message):
		cm = message.text
		print (cm)
		sleep(0.4)
		keyboard.write(cm)
		keyboard.press("enter")
		keyboard.release("enter")
		
#@dp.message_handler(commands=['📹ВИДЕО📹'])	
#async def process_start_command(message: types.Message):
#	await bot.send_message(message.from_user.id, 'Запись началась(5c)')
#	i = 0
#	while True:
#		ret, frame = cap.read()
#		#cv2.imshow("camera", frame)
#		out.write(frame)
#		time.sleep(0.05)
#		i = i + 1
#		if i > 120:
#			break
#	cap.release()
#	cv2.destroyAllWindows()
#	print("SAVED")
#	await bot.send_video(message.chat.id, open('res.mp4', 'rb'))

@dp.message_handler(commands=['📸КАМЕРА📸'])	
async def process_start_command(message: types.Message):
	await bot.send_message(message.from_user.id, 'Делаю фото...')
	cap = cv2.VideoCapture(0)
	for i in range(30):
		cap.read()
	ret,frame = cap.read()
	cv2.imwrite('cam.png', frame)
	cap.release()
	file = open('cam.png', 'rb')
	await bot.send_photo(message.chat.id,file, 'Вот фото с вебки')

@dp.message_handler(commands=['help'])
async def process_start_command(message: types.Message):
	await bot.send_message(message.from_user.id, helptxt)
	

if __name__ == '__main__':
    executor.start_polling(dp)
