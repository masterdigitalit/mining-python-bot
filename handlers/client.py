from aiogram import types, dispatcher
from create_bot import dp, bot
from keyboard import confirmationButton, registrationButton
import uuid
from adminNotification import adminNotification
from database import  addUser, isUserExist
async def startMessage(message: types.Message):
    try:

        chat_id = message.chat.id
        print(message['from'])
        id = uuid.uuid4()
        if( not isUserExist(message['from'].id)):
            addUser(message['from'].id, message['from'].first_name,  message['from'].username )
            await bot.send_message(chat_id, f'Давайте пройдем регистрацию', parse_mode='html',reply_markup=registrationButton(id,'начать'))
        else:
            await bot.send_message(chat_id, f'Вы уже зарегистрированы, ждите заданий', parse_mode='html')

    except Exception as e:
        await adminNotification(e, __name__)


def registerClientHandler(dp: dispatcher):
    dp.register_message_handler(startMessage, commands=['start'])