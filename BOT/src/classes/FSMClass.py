import aiogram
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
storage = MemoryStorage()
class FSMAD(StatesGroup):
    pas = State()