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
from datetime import datetime, timedelta
#
# clock_in_half_hour = datetime.now() + timedelta(minutes=30)
# print(clock_in_half_hour.strftime('%d.%m.%Y %H:%M'))


from config import admins, times, listOfTemky


#print((datetime.now() + timedelta(minutes=-20)).strftime('%d.%m.%Y %H:%M'))
#
# print(datetime.now().strftime('%d.%m.%Y %H:%M'))
# from dotenv import load_dotenv
# env = load_dotenv('.env')
# print(load_dotenv.main)

from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access environment variables
database_url = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")

# Now you can use these variables in your script
print(f"Database URL: {database_url}")
print(f"API Key: {api_key}")