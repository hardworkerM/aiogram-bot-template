import schedule
import aioschedule
import asyncio

import time
import datetime
from loader import bot
from help_functions.sql.weight_sql import take_date

"""
"""


# # Отправка сообщения
# async def send_notify(id, text):
#     await bot.send_message(id, text)
#
#
# # Проверяется совпала ли настоящая дата с тем, что есть у пользователя
# async def notify_users1():
#     data = datetime.datetime.now().date()
#     res = take_date(data)
#     print(res)
#     if res != 0:
#         for id in res:
#             for tasks in res[id]:
#                 await send_notify(id, tasks)
#
#
# # Каждый день происходит проверка
# async def  start_schedule():
#     aioschedule.every(10).seconds.do(notify_users1)
#     while True:
#         await aioschedule.run_pending()
#         await asyncio.sleep(1)
