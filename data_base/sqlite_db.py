import sqlite3 as sq
from create_bot import bot

def sql_start():
    global base, cur
    base = sq.connect('anti_mat.db')
    cur = base.cursor()
    if base:
        print('Data base connected!')
    base.execute('CREATE TABLE IF NOT EXISTS members(img TEXT, name TEXT PRIMARY KEY, description TEXT)')
    base.commit()


async def sql_add_command(state, data):
    async with state.proxy() as data:
        cur.execute('INSERT INTO members VALUES (?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_read(message):
    for ret in cur.execute('SELECT * FROM members').fetchall():
        try:
            await message.answer_photo(ret[0], f'{ret[1]}\nОписание: {ret[2]}')
        except:
            await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}')


async def sql_read2():
    return cur.execute('SELECT * FROM members').fetchall()


async def sql_delete_command(data):
    cur.execute('DELETE FROM members WHERE name == ?', (data,))
    base.commit()