from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

but1 = KeyboardButton('/Загрузить')
but2 = KeyboardButton('/Удалить')
but3 = KeyboardButton('/Отмена')

kb_admin_1 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_admin_1.add(but1).add(but2)

kb_admin_2 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_admin_2.add(but3)