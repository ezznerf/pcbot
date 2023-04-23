import os
import socket
import cv2
import wmi

from pynput.mouse import Button, Controller

import screen_brightness_control as sbc

import keyboard

import random

import tkinter as tk
from tkinter import *


#from aiogram.dispatcher import FSMContext

import pyautogui
from aiogram import types

from src.classes import Config
from config.Charac import characteristics
from src.interfaces.OSInterface import OSInterface

mouse = Controller()

chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


class WindowsOS(OSInterface):

    def __init__(self, dp, bot, config: Config, keyboard):
        self.__dp = dp
        self.__bot = bot
        self.__application_config = config
        self.__keyboard = keyboard

    async def shutdown(self, message: types.Message):
        await self.__bot.send_message(message.from_user.id, "Выключаю...")
        os.system('shutdown -s -t 0')

    async def screenshot(self, message: types.Message):
        await self.__bot.send_message(message.from_user.id, "Делаю скрин...")
        self.screen()
        file = open(self.__application_config.get_param('media_path') + '\screenshot\screenshot.png', 'rb')
        await self.__bot.send_photo(message.chat.id, file, 'Вот скрин вашего экрана')

    async def reboot(self, message: types.Message):
        await self.__bot.send_message(message.from_user.id, 'Перезапускаю...')
        os.system('shutdown -r -t 0')

    def screen(self):
        screenshot = pyautogui.screenshot()
        path = self.__application_config.get_param('root_dir') \
               + '\\' + self.__application_config.get_param('media_path') + '\screenshot\screenshot.png'
        screenshot.save(path)

    async def disk_area(self, message: types.Message):
        os.system('chcp 65001')
        conn = wmi.WMI()
        for disk in conn.Win32_LogicalDisk():
            if disk.size != None:
                await self.__bot.send_message(message.from_user.id, ("Disk " + disk.Caption, "is {0:.2f}% free".format(
                    100 * float(disk.FreeSpace) / float(disk.Size))))

    async def get_temperature(self, message: types.Message):
        pass

    async def make_photo(self, message: types.Message):
        await self.__bot.send_message(message.from_user.id, "Улыбочку!")
        cap = cv2.VideoCapture(0)
        for i in range(30):
            cap.read()
        ret,frame = cap.read()
        cv2.imwrite(self.__application_config.get_param('media_path') + '\web_photo\wep.png', frame)
        cap.release()
        file = open(self.__application_config.get_param('media_path') + '\web_photo\wep.png', 'rb')
        await self.__bot.send_photo(message.from_user.id, file, "Вот ваше фото")


    async def win_locker(self, message: types.Message):
       password = ''
       for i in range(6):
           password += random.choice(chars)
       await self.__bot.send_message(message.from_user.id, "Вот пароль: " + password)

       def btn_click():
           k = ent.get()
           if k == password:
               root.destroy()
               print('lol')

       root = Tk()
       root.title('Windows has Locked')
       root.attributes("-fullscreen", True)
       root.geometry('400x200')
       frame = Frame(root)
       frame.place(relx=0.20, rely=0.30, relwidth=0.6, relheight=0.7)
       Label(frame, text="Enter password", font='Arial 25', fg='white').pack()
       ent = Entry(frame, text='', font='Arial 25', width=15)
       ent.pack()
       tk.Button(frame, text='Unlock', font='Arial 25', bg='red', fg='white', command=btn_click).pack()

       root.mainloop()

    async def charac(self, message: types.Message):
        await self.__bot.send_message(message.from_user.id, characteristics)

    async def ip_get(self, message: types.Message):
        await self.__bot.send_message(message.from_user.id,"IP: " + socket.gethostbyname(socket.getfqdn()))

    async def brightness25(self, message: types.Message):
        await self.__bot.send_message(message.from_user.id, "Готово! Яркость изменена на 25%")
        sbc.set_brightness(25)

    async def brightness50(self, message: types.Message):
        await self.__bot.send_message(message.from_user.id, "Готово! Яркость изменена на 50%")
        sbc.set_brightness(50)

    async def brightness75(self, message: types.Message):
        await self.__bot.send_message(message.from_user.id, "Готово! Яркость изменена на 75%")
        sbc.set_brightness(75)

    async def brightness100(self, message: types.Message):
        await self.__bot.send_message(message.from_user.id, "Готово! Яркость изменена на 100%")
        sbc.set_brightness(100)

    async def temperature(self, message: types.Message):
        w = wmi.WMI(namespace='root\\wmi', privileges=["Security"])
        temperature = w.MSAcpi_ThermalZoneTemperature()[0]
        temperature = int(temperature.CurrentTemperature / 10.0 - 273.15)
        await self.__bot.send_message(message.from_user.id, f'CPU temp: {temperature}.0 °C')


    async def ctrl_shift_esc(self, message: types.Message):
        keyboard.press('ctrl')
        keyboard.press('shift')
        keyboard.press('esc')
        keyboard.release('ctrl')
        keyboard.release('shift')
        keyboard.release('esc')
        await self.__bot.send_message(message.from_user.id, "Диспетчер задач открыт!")

    async def win_a(self, message: types.Message):
        keyboard.press('win')
        keyboard.press('a')
        keyboard.release('win')
        keyboard.release('a')
        await self.__bot.send_message(message.from_user.id, 'ГОТОВО!')

    async def win_d(self, message: types.Message):
        keyboard.press('win')
        keyboard.press('d')
        keyboard.release('win')
        keyboard.release('d')
        await self.__bot.send_message(message.from_user.id, "ГОТОВО!")
        
    async def alt_f4(self, message: types.Message):
        keyboard.press('alt')
        keyboard.press('f4')
        keyboard.release('f4')
        keyboard.release('alt')
        await self.__bot.send_message(message.from_user.id, 'Процесс завершен!')
            async def mouse_up(self, message: types.Message):
        mouse.move(0, -30)

    async def mouse_left(self, message:types.Message):
        mouse.move(-30, 0)

    async def mouse_right(self, message:types.Message):
        mouse.move(30, 0)

    async def mouse_down(self, message:types.Message):
        mouse.move(0, 30)

    async def mouse_click(self, message: types.Message):
        pyautogui.click(clicks=2)

 
