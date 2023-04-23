from aiogram import types


class OSInterface:

    async def shutdown(self, message: types.Message):
        pass

    async def make_screenshot(self, message: types.Message):
        pass

    async def reboot(self, message: types.Message):
        pass

    async def disk_area(self, message: types.Message):
        pass

    async def get_temperature(self, message: types.Message):
        pass

    async def make_photo(self, message: types.Message):
        pass

    async def win_locker(selfs, message: types.Message):
        pass

    async def charac(self, message: types.Message):
        pass

    async def ip_get(self, message: types.Message):
        pass

    async def temperature(self, message:types.Message):
        pass

    async def ctrl_shift_esc(self, message: types.Message):
        pass

    async def win_a(self, message: types.Message):
        pass

    async def win_d(self, message: types.Message):
        pass
        
    async def brightness25(self, message: types.Message):
        pass

    async def brightness50(self, message: types.Message):
        pass

    async def brightness75(self, message: types.Message):
        pass

    async def brightness100(self, message:types.Message):
        pass

    async def mouse_up(self, messsage:types.Message):
        pass

    async def mouse_down(self, messsage: types.Message):
        pass

    async def mouse_left(self, messsage: types.Message):
        pass

    async def mouse_right(self, messsage: types.Message):
        pass

    async def alt_f4(self, messsage: types.Message):
        pass
