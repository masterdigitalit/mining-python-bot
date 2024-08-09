from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


def confirmationButton(confirmationId, text):

    inline_btn_1 = InlineKeyboardButton(text, callback_data=f'confirmation-button:{confirmationId}')
    return InlineKeyboardMarkup().add(inline_btn_1)
def confirmationButtons(confirmationId, text):
    inline_btn_1 = InlineKeyboardButton(text[0], callback_data=f'confirmation-button:{confirmationId[0]}')
    inline_btn_2 = InlineKeyboardButton(text[1], callback_data=f'confirmation-button:{confirmationId[1]}')
    return InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2)
def registrationButton(confirmationId, text):
    inline_btn_1 = InlineKeyboardButton(text, callback_data=f'registration-button:{confirmationId}')
    return InlineKeyboardMarkup().add(inline_btn_1)
