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
from handlers.deal_products import start_handler, applying_deal_handler
from handlers.other_services_of_bank import other_services_of_bank

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)



async def main():
    bot = Bot(token="7202636214:AAFXSMZsAuHhy7j2ZvBISdwNhf6xzxDdFiY", default = DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp.include_routers(start_handler.router, applying_deal_handler.router, other_services_of_bank.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
