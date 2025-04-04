from aiogram import Router, F
from aiogram.filters import Command
from aiogram import types
from keyboards import keyboard_start
from keyboards import keyboard_applying_for_deal

router = Router()


@router.callback_query(F.data == 'bank_deal')
async def products_message(callback: types.CallbackQuery):
    message_to_user = 'Выберете пожалуйста тип сделки:'
    await callback.message.answer(message_to_user, reply_markup=keyboard_applying_for_deal.keyboard_category_of_deal())