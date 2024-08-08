from aiogram.types import CallbackQuery
from aiogram import types, dispatcher
from create_bot import dp, bot
from config import listOfTemky
from adminNotification import adminNotification
from database import getTaskState, changeConfirmationState, addTask
from keyboard import confirmationButton
import uuid

async def confirmationBtn(callback_query: CallbackQuery):
    try:
        if getTaskState(callback_query.message.reply_markup.inline_keyboard[0][0].callback_data[20:]) == 'not-activated':
            changeConfirmationState(callback_query.message.reply_markup.inline_keyboard[0][0].callback_data[20:], 'activated')
            await bot.delete_message(callback_query.from_user.id,callback_query.message.message_id)
            await bot.send_message(callback_query.from_user.id, 'молодец')
    except Exception as e:
        await adminNotification(e, __name__)
async def registrationBtn(callback_query: CallbackQuery):
    try:
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
        for i in listOfTemky:
            name = i['name']
            link = i['link']
            uniqueCode = uuid.uuid4()
            addTask(f'{uniqueCode}', name, 'periodic', 'not-activated',callback_query.from_user.id )
            await bot.send_message(callback_query.from_user.id, f'{name}\n{link}', reply_markup=confirmationButton(uniqueCode, 'подтвердить'))
        await bot.send_message(callback_query.from_user.id, 'это было последнее задание, через время мы пришлем следующие')
    except Exception as e:
        await adminNotification(e, __name__)
def callbackQueryHandler(dp: dispatcher):
    dp.register_callback_query_handler(confirmationBtn, lambda c: c.data[0:20] == 'confirmation-button:')
    dp.register_callback_query_handler(registrationBtn, lambda c: c.data[0:20] == 'registration-button:')







    print('hi')



