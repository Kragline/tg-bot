import sqlite3
from create_bot import bot, dp
from data_base import sqlite_db
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keyboards import kb_admin_1, kb_admin_2, kb_client
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ID = None

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()


async def moderator(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Что надо?', reply_markup=kb_admin_1)
    await message.delete()


async def cmnd_start(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply('Загрузи фото', reply_markup=kb_admin_2)


async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('Процесс отменён', reply_markup=kb_admin_1)


async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await message.reply('Теперь введи име')


async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            if message.text.startswith('@'):
                data['name'] = message.text
                await FSMAdmin.next()
                await message.reply('Введи описание')
            else:
                await message.reply('Введи ник участника чата')
        

async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        try:
            await sqlite_db.sql_add_command(state)
            await message.reply('Данные успешно сохранены', reply_markup=kb_client)
        except sqlite3.IntegrityError:
            await message.reply('Имена не должны повторяться', reply_markup=kb_admin_1)
        await state.finish()


async def del_callback(callback: types.CallbackQuery):
    await sqlite_db.sql_delete_command(callback.data.replace('del ', ''))
    await callback.message.answer('Готово')


async def delete_member(message: types.Message):
    if message.from_user.id == ID:
        read = await sqlite_db.sql_read2()
        for ret in read:
            await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}')
            await bot.send_message(message.from_user.id, text='^^^',reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text=f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cmnd_start, commands=['Загрузить'], state=None)
    dp.register_message_handler(cancel_handler, state="*", commands=['Отмена'])
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(moderator, commands=['moderator'], is_chat_admin = True)
    dp.register_callback_query_handler(del_callback, Text(startswith='del '))
    dp.register_message_handler(delete_member, commands=['Удалить'])