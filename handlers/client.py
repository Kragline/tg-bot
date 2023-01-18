from aiogram import types, Dispatcher
from create_bot import bot, dp
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle
from keyboards import kb_client
from data_base import sqlite_db
import hashlib


async def comand_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Хэллоу', reply_markup=kb_client)
    except:
        await message.reply('Общение с ботом только в ЛС \nhttps://t.me/ithinkitsnormalbot')


async def comand_help(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, '''Существующие команды\n\n/start - начать работу (показать кнопки)\n/help - все команды''')
    except:
        await message.reply('Общение с ботом только в ЛС \nhttps://t.me/ithinkitsnormalbot')


async def instructions(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Добавьне бота в чат и он начнёт выполнять свои функции')
    except:
        await message.reply('Общение с ботом только в ЛС \nhttps://t.me/ithinkitsnormalbot')


async def bot_functions(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Бот распознаёт сообщение с матом и удаляет его')
    except:
        await message.reply('Общение с ботом только в ЛС \nhttps://t.me/ithinkitsnormalbot')


async def contacts(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Если есть проблемы с ботом: https://t.me/wntrsld')
    except:
        await message.reply('Общение с ботом только в ЛС \nhttps://t.me/ithinkitsnormalbot')


async def all_members(message : types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(comand_start, commands=['start'])
    dp.register_message_handler(comand_help, commands=['help'])
    dp.register_message_handler(instructions, commands=['Как_пользоваться'])
    dp.register_message_handler(bot_functions, commands=['Функции_бота'])
    dp.register_message_handler(contacts, commands=['Обратная_сжязь'])
    dp.register_message_handler(all_members, commands=['Участники'])
    