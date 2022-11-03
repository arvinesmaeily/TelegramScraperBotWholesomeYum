from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from Scraper import scrape_recipe

bot = Bot(token="BOT_TOKEN")

dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'info'])
async def welcome(message: types.Message):
    await message.answer("This bot provides you with your desired healthy recipe. Just enter the name in correct format without \"Recipe\" at the end! \n\nExamples:\n\nBaked Salmon\n\neggplant rollatini\n\nTURKEY TACO STUFFED PEPPERS") #, reply_markup=kb1)

@dp.message_handler()
async def answer(message: types.Message):
    recipe = scrape_recipe(message.text)
    print(message.text)
    await message.answer_photo(recipe['image'], caption=recipe['title'])
    for ctx in recipe['context']:
        await message.answer(ctx, parse_mode='Markdown')


    
executor.start_polling(dp)


