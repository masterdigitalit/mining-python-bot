# import asyncio
# import logging
#
# from aiogram import Bot, Dispatcher
#
# from apscheduler.schedulers.asyncio import AsyncIOScheduler
#
#
#
#
#
#
# async def send_message_to_admin(bot: Bot):
#
#
#     await bot.send_message(text="Сообщение по таймеру", chat_id=5273914742)
#
#
# # Создаем функцию, в которой будет происходить запуск наших тасков.
#
# async def main():
#
#
#     bot = Bot(token='7230354816:AAFHyFbl1Ihd5Foyl_9Ip2XiXOFADPNQ79M', parse_mode='HTML')
#     dp = Dispatcher(bot)
#
#     scheduler = AsyncIOScheduler(timizone='Europe/Moscow')
#     scheduler.add_job(send_message_to_admin, trigger='interval', seconds=5, kwargs={'bot':bot})
#
#
#     # Ставим наши таски на запуск, передаем нужные переменные.
#
#
#     # start
#     try:
#         scheduler.start()
#         await dp.start_polling()
#     finally:
#         pass
#
#
# if __name__ == '__main__':
#     asyncio.run(main())
#
# from datetime import datetime, timedelta
#
# clock_in_half_hour = datetime.now() + timedelta(minutes=30)
# print(clock_in_half_hour.strftime('%d.%m.%Y %H:%M'))


from config import admins, times, listOfTemky


print( [x for x in listOfTemky if x['name'] == 'tapswap'])