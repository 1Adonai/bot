import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config_reader import config


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")
number = config.phone.get_secret_value()


dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Каско")],
        [types.KeyboardButton(text="Осаго")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Страхование"
    )
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Whatsup", url= f"https://wa.me/{number}")
    )

    await message.answer("Выберете вид страхования", reply_markup=keyboard)
    await message.answer(
        'Связаться в Whatsup',
        reply_markup=builder.as_markup(),
    )


@dp.message(F.text.lower() == "осаго")
async def with_puree(message: types.Message):
    await message.answer("Подробности - Пример/Осаго")


@dp.message(F.text.lower() == "каско")
async def without_puree(message: types.Message):
    await message.answer("Подробности - Пример/Каско")






async def main():
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())

