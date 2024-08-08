from aiogram import types, dispatcher
from create_bot import dp, bot
from keyboard import confirmationButton, registrationButton
import uuid
from adminNotification import adminNotification
# from database import createUser
async def startMessage(message: types.Message):
    try:

        chat_id = message.chat.id

        id = uuid.uuid4()
        await bot.send_message(chat_id, f'Давайте пройдем регистрацию', parse_mode='html',reply_markup=registrationButton(id,'начать'))
#       рассылка всех тапалок для регистрации

    except Exception as e:
        await adminNotification(e, __name__)


def registerClientHandler(dp: dispatcher):
    dp.register_message_handler(startMessage, commands=['start'])