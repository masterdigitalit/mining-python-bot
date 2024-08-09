
from aiogram.utils import executor
from create_bot import dp, bot
from handlers import confirmationButton, client
from notification import  send_periodic_confirmation,hamster_daily_notification
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from statesChecker import statesChecker
from newsletter import dailyNewsletter

from datetime import datetime


client.registerClientHandler(dp)
confirmationButton.callbackQueryHandler(dp)


def telegram():

    scheduler = AsyncIOScheduler(timizone='Europe/Moscow')
    scheduler.add_job(send_periodic_confirmation, trigger='interval', seconds=60, kwargs={'bot': bot} )
    scheduler.add_job(statesChecker, trigger='interval', seconds=60, kwargs={'bot': bot})
    scheduler.add_job(hamster_daily_notification, trigger='cron', hour='12', minute='00', start_date=datetime.now(), kwargs={'bot': bot})
    # Ставим наши таски на запуск, передаем нужные переменные.

    # start
    try:
        scheduler.start()
        executor.start_polling(dp)

    finally:
        pass



# schedule.every(1).minutes.do(notification, bot)
if __name__ == '__main__':

    telegram()
