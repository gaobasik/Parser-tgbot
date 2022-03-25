from aiogram import Bot,Dispatcher,executor,types
from config import token
import json
from Parser import check_news_update
import time

bot = Bot(token=token,parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

# @dp.message_handler(commands="start")
# async def start(message:types.Message):
#     await message.reply("Как делишки")

@dp.message_handler(commands="News")
async def get_fresh_news(message: types.Message):
    with open ("news_dict.json") as file:
        news_dict = json.load(file)
    for k, v in news_dict.items():
        news = f"{v['News']}"

        await message.answer(news)
@dp.message_handler(commands="lastNews")
async def get_fresh_news(message: types.Message):
    while True:
        time.sleep(10)

        fresh_news = check_news_update()

        if len(fresh_news) >= 1:
            for k, v in fresh_news.items():
              news = f"{v['News']}"

            await message.answer(news)

        else:
            await message.anwser("покА НОВОСТЕЙ НЕТ")



if __name__ == '__main__':
    executor.start_polling(dp)
