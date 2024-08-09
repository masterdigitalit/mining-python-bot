from database import getWarning, updateBlockTime, changeConfirmationState, getFailed
from aiogram import Bot
from keyboard import confirmationButton
async def statesChecker(bot: Bot):
    async def checkWarning():
        arr = getWarning()
        if(len(arr)):
            for i in arr:
                changeConfirmationState(i[1], 'warning')
                updateBlockTime(i[1])
                await bot.send_message(i[8], 'Прошло много времени , срочно выполните задание',
                                       reply_markup=confirmationButton(i[1], 'подтвердить'))

    async def checkFailed():
        arr = getFailed()
        for i in arr:
            changeConfirmationState(i[1], 'not-done')
            await bot.send_message(i[8], f'Задание {i[2]}, не выполнено ')
    await checkFailed()
    await checkWarning()