from aiogram import bot
from database import getAllUsersId
async def dailyNewsletter(bot:bot):
    for i in getAllUsersId():

        await bot.send_message(i[0], 'hi')