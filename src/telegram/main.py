import asyncio
import os
import logging
import sys

from os import getenv
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode, setup_dialogs
from dotenv import load_dotenv
from pathlib import Path

from src.telegram.db import user_exists
from src.telegram.state import key_dialog, KeySG

env_path = Path(".env")
load_dotenv(dotenv_path=env_path)

dp = Dispatcher()
TOKEN = getenv("BOT_TOKEN")
bot = Bot(TOKEN)


@dp.message(CommandStart())
async def start_handler(message: Message, dialog_manager: DialogManager):
    try:
        if not user_exists(message.from_user.id):
            await dialog_manager.start(state=KeySG.key, mode=StartMode.RESET_STACK, data={"user_id": message.from_user.id})
        else:
            await message.answer(f"Welcome to the key system, you have already activated the key\n\nYour ID: {message.from_user.id}")
    except Exception as e:
        print("Oops!\nMake sure to generate the keys first", e)


async def main():
    dp.include_routers(key_dialog)
    setup_dialogs(dp)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())