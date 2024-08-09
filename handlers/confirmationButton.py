from aiogram.types import CallbackQuery
from aiogram import  dispatcher
from create_bot import dp, bot
from config import listOfTemky, times
from adminNotification import adminNotification
from database import getTaskState, changeConfirmationState, addTask
from keyboard import confirmationButton, confirmationButtons
import uuid

async def confirmationBtn(callback_query: CallbackQuery):
    try:
        if getTaskState(callback_query.data[20:]) == 'not-activated':

            changeConfirmationState(callback_query.data[20:], 'activated')
            await bot.delete_message(callback_query.from_user.id,callback_query.message.message_id)
    except Exception as e:
        await adminNotification(e, __name__)
async def registrationBtn(callback_query: CallbackQuery):
    try:
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
        for i in listOfTemky:
            uniquePeriodicCode = uuid.uuid4()
            name = i['name']
            link = i['link']
            addTask(f'{uniquePeriodicCode}', name, 'periodic', 'not-activated', callback_query.from_user.id,
                    times[name]['periodic'])

            if(i['daily']):
                uniqueDailyCode = uuid.uuid4()
                addTask(f'{uniqueDailyCode}', name, 'daily', 'not-activated', callback_query.from_user.id,None)
                await bot.send_message(callback_query.from_user.id, f'{name}\n{link}' , reply_markup=confirmationButtons([uniquePeriodicCode,uniqueDailyCode], ['подтвердить бонус','подтвердить ежедневку']))
            else:
                await bot.send_message(callback_query.from_user.id, f'{name}\n{link}',
                                       reply_markup=confirmationButton(uniquePeriodicCode, 'подтвердить бонус'))
        await bot.send_message(callback_query.from_user.id, 'это было последнее задание, через время мы пришлем следующие')
    except Exception as e:
        await adminNotification(e, __name__)

def callbackQueryHandler(dp: dispatcher):
    dp.register_callback_query_handler(confirmationBtn, lambda c: c.data[0:20] == 'confirmation-button:')
    dp.register_callback_query_handler(registrationBtn, lambda c: c.data[0:20] == 'registration-button:')










