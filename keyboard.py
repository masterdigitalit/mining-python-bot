from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
def confirmationButton(confirmationId, text):
    inline_btn_1 = InlineKeyboardButton(text, callback_data=f'confirmation-button:{confirmationId}')
    return InlineKeyboardMarkup().add(inline_btn_1)
def registrationButton(confirmationId, text):
    inline_btn_1 = InlineKeyboardButton(text, callback_data=f'registration-button:{confirmationId}')
    return InlineKeyboardMarkup().add(inline_btn_1)
