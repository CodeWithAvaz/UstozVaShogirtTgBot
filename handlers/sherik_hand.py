from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from states.menu_state import Sherik

sherik_router = Router()


@sherik_router.message(F.text == "Sherik kerak")
async def start_cmd(msg: Message, state: FSMContext):
    await msg.answer("Ism va Familiyangizni kiriting: ")
    await state.set_state(Sherik.full_name)

@sherik_router.message(Sherik.full_name)
async def full_name(msg: Message, state: FSMContext):
    await state.update_data(full_name=msg.text)
    await msg.answer("Talab qilinadigan Texnologiya: ")
    await state.set_state(Sherik.texnologiya)