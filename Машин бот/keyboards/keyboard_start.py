from aiogram.utils.keyboard import InlineKeyboardBuilder

def keyboard_start():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text="Записаться на сделку", callback_data="bank_deal")
    keyboard_builder.button(text="Посмотреть услуги банка", callback_data="bank_services")
    keyboard_builder.button(text="Задать вопрос", callback_data="bank_questions")
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()
