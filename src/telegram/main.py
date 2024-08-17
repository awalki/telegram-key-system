import asyncio
import os

from os import getenv
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode, setup_dialogs
from dotenv import load_dotenv

from src.telegram.db import user_exists
from src.telegram.state import key_dialog, KeySG

dp = Dispatcher()
env_path = os.path.join('keysystem', '.env')
load_dotenv(dotenv_path=env_path)
TOKEN = getenv("BOT_TOKEN")


@dp.message(CommandStart())
async def start_handler(message: Message, dialog_manager: DialogManager):
    try:
        await message.answer("Добро пожаловать в систему ключей!")

        if not user_exists(message.from_user.id):
            await dialog_manager.start(state=KeySG.key, mode=StartMode.RESET_STACK, data={"user_id": message.from_user.id})
        else:
            await message.answer(f"Добро пожаловать, похоже вы уже активировали ключ\n\nВаш айди: {message.from_user.id}")
    except Exception as e:
        print("Уп-с, ошибочка!\nУбедитесь, что сначала сгенерировали ключи в keygen", e)

async def main():
    bot = Bot(TOKEN)
    dp.include_routers(key_dialog)
    setup_dialogs(dp)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())