import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject, CommandStart
from datetime import datetime
from random import randint
from aiogram import F
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.formatting import Text, Bold
from aiogram import html
import re
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest
from typing import Optional
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
from aiogram import F

from aiogram import Bot, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
from aiogram import F


bot = Bot(token="7202636214:AAFXSMZsAuHhy7j2ZvBISdwNhf6xzxDdFiY",
          default = DefaultBotProperties(parse_mode=ParseMode.HTML))

logging.basicConfig(level=logging.INFO)

dp = Dispatcher()
# Создаем кнопку
button = InlineKeyboardButton(text="Моя карта", callback_data="my_card")

# Создаем клавиатуру с одной кнопкой
keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])

# Обработчик команды /start
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Выберите действие:", reply_markup=keyboard)

# Обработчик нажатия кнопки
@dp.callback_query(F.data == "my_card")
async def my_card_callback(callback: types.CallbackQuery):
    await callback.answer("Сообщ", show_alert=True)



async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
