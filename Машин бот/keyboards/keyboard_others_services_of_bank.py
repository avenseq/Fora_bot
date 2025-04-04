from aiogram.utils.keyboard import InlineKeyboardBuilder

def keyboard_other_services():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text="Услуги, связанные со сделкой", callback_data="services_deal")
    keyboard_builder.button(text="Прочие услуги", callback_data="services_other")
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

def keyboard_deal_services():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text="Хранение ключа для сейфовой ячейки - 1000 рублей", callback_data="saving_key_1000rub")
    keyboard_builder.button(text="Проверка / пересчет денежных средств - рубли 0,1%, минимум 2000 руб., ", callback_data="checking_money")
    keyboard_builder.button(text="Доверенность по форме банка: к сейфовой ячейке - 500 рублей", callback_data="trustee_safe_500rub")
    keyboard_builder.button(text="Электронная регистрация", callback_data="deal_online_registation")
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


