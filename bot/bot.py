import asyncio
import os
from os import getenv
from handlears import router
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, BotCommand
from dotenv import load_dotenv

from keyboards import btn_keyboard

load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()


async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Botni ishga tushirish"),
        BotCommand(command="/help", description="Bot haqida yordam"),
    ]
    await bot.set_my_commands(commands)

# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "image", "image.png"))
    text = (f"Hush kelibsiz {message.from_user.full_name}, biz sizga birnechta savollar berib bilimingizni\n"
            "tekshirib beramiz!")
    await message.answer_photo(photo=img, caption=text, reply_markup=btn_keyboard)

async def main() -> None:
    bot = Bot(token=BOT_TOKEN)
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Starting bot...")

    asyncio.run(main())