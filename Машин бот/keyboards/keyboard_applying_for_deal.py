from aiogram.utils.keyboard import InlineKeyboardBuilder


def keyboard_category_of_deal():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Сейф', callback_data='deal_safe', width = 10)
    keyboard_builder.button(text='Аккредитив', callback_data='deal_accreditive', width = 10)
    keyboard_builder.button(text='Сейф+Аккредитив', callback_data='deal_safe')
    keyboard_builder.button(text='Сделки с цепочками', callback_data='deal_safe_and_accreditive')
    keyboard_builder.button(text='Другие услуги банка', callback_data='deal_other_services_of_bank')
    keyboard_builder.button(text='Электронная регистрация сделок с недвижимостью', callback_data='deal_online_registation', width = 10)
    keyboard_builder.button(text='Аренда переговорных комнат', callback_data='deal_meeting_rooms_rent')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

