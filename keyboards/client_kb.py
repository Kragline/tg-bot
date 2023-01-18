from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

but1 = KeyboardButton('/Участники')
but2 = KeyboardButton('/Как_пользоваться')
but3 = KeyboardButton('/Функции_бота')
but4 = KeyboardButton('/Обратная_сжязь')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(but1).add(but2).row(but3, but4)


il_but1 = InlineKeyboardButton(text='Да', callback_data='like_+1')
il_but2 = InlineKeyboardButton(text='Нет', callback_data='like_-1')
il_but3 = InlineKeyboardButton(text='Я пас', callback_data='like_+0')

il_kb_client = InlineKeyboardMarkup(row_width=1)
il_kb_client.add(il_but1, il_but2, il_but3)