from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\n\n"
                         f"Это тестовый бот интернет магазина, который синхронизируется с количеством "
                         f"товара на складе (базой данных), однако покупка в нем невозможна!\n\n"
                         f"Жми /menu , чтобы посмотреть принцип работы")
