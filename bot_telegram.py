# -*- coding: utf-8 -*-
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.markdown import text
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import filters, FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ContentType, Message
from image import delete_all_imgs, remove_bg
from settings import settings


bot = Bot(token=settings.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start', 'menu'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "🤟Добро пожаловать. Этот бот может убирать задний фон со снимка, отправь нам фото и "
                           "получи отредактированную картинку")


@dp.message_handler(content_types=['photo'])
async def get_photo(message: types.Message):
    await bot.send_message(message.from_user.id, "Подождите, это займет несколько секунд")

    name = message.from_user.id

    await message.photo[-1].download(destination_file=f'./input_imgs/{name}.jpg')

    try:
        remove_bg()

    except:
        await bot.send_message(message.from_user.id, "На этом фото невозможно удалить фон")

    out = open(f'./output_imgs/{name}_output.png', 'rb')
    await bot.send_photo(message.from_user.id, out)

    delete_all_imgs(name)


if __name__ == '__main__':
    executor.start_polling(dp)
