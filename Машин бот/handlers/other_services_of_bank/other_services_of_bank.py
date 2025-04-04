from aiogram import Router, F
from aiogram.filters import Command
from aiogram import types
from keyboards import keyboard_start
from keyboards import keyboard_others_services_of_bank

router = Router()

#Посмотреть услуги банка
@router.callback_query(F.data == 'bank_services')
async def services_message(callback: types.CallbackQuery):
    message_to_user = 'Другие услуги банка:'
    await callback.message.answer(message_to_user, reply_markup=keyboard_others_services_of_bank.keyboard_other_services())

#Другие услуги банка
@router.callback_query(F.data == 'deal_other_services_of_bank')
async def services_message(callback: types.CallbackQuery):
    message_to_user = 'Другие услуги банка:'
    await callback.message.answer(message_to_user, reply_markup=keyboard_others_services_of_bank.keyboard_other_services())

#Услуги, связанные с сделкой
@router.callback_query(F.data == 'services_deal')
async def services_deal(callback: types.CallbackQuery):
    message_to_user = 'Выбор услуги по сделке:'
    await callback.message.answer(message_to_user, reply_markup=keyboard_others_services_of_bank.keyboard_deal_services())













