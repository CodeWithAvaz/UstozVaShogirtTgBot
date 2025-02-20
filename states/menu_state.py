from aiogram.fsm.state import State, StatesGroup


class Sherik(StatesGroup):
    full_name = State()
    texnologiya = State()
    aloqa = State()
    viloyat = State()
    narx = State()
    info = State()
    vaqt_murojat = State()
    maqsad = State()
    tekshirish = State()