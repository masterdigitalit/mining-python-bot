from aiogram.types import message
from aiogram import dispatcher
from create_bot import dp, bot

from adminNotification import adminNotification

async def startMessage(message: message):


    await adminNotification()


def registerClientHandler(dp: dispatcher):
    dp.register_message_handler(startMessage, commands=['help'])