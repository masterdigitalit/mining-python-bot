from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import logging


bot = Bot(token='7230354816:AAFHyFbl1Ihd5Foyl_9Ip2XiXOFADPNQ79M')
dp = Dispatcher(bot)