from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.default_btn import menu

start_router = Router()


@start_router.message(Command("start"))
async def start_cmd(msg: Message):
    await msg.answer("SALOM Ustoz va shogird Botiga xush kelibsiz", reply_markup=menu)