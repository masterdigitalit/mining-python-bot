from aiogram import Bot
from config import admins, times, listOfTemky
from keyboard import confirmationButton
import  uuid
from database import selectAllByTime, addTask
from datetime import datetime, timedelta
import json

async def send_message_to_admin(bot: Bot):
    for i in admins:
        print(i)
        await bot.send_message(text="Сообщение по таймеру", chat_id=i)


async def send_periodic_confirmation(bot: Bot ):
    # запись в бд

    tasks = selectAllByTime(f'{datetime.now().strftime("%d.%m.%Y %H:%M")}')

    for i in tasks:
        if(i[3] == 'periodic'):
            uniqueCode = uuid.uuid4()
            output_json =  [x for x in listOfTemky if x['name'] == i[2]]

            addTask(f'{uniqueCode}', output_json[0]['name'], 'periodic', 'not-activated', i[8], times[output_json[0]['name']]['periodic'] )
            await bot.send_message(i[8], text=f"забери временную награду в {output_json[0]['name']} \n {output_json[0]['link']}", reply_markup=confirmationButton(uniqueCode, 'подтвердить'))
        else:
            uniqueCode = uuid.uuid4()
            output_json = [x for x in listOfTemky if x['name'] == i[2]]

            addTask(f'{uniqueCode}', output_json[0]['name'], 'daily', 'not-activated', i[8],
                   None)
            await bot.send_message(i[8], text=f'ежедневка в {output_json[0]["name"]}\n {output_json[0]["link"]}',
                                   reply_markup=confirmationButton(uniqueCode, 'подтвердить'))


async def hamster_daily_notification(bot:Bot):
    pass
