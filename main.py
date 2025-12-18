from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command
import asyncio

BOT_TOKEN = "8545421619:AAGtElqWl3VDvefdX3kq0DKdetCyXt6YY8Q"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

schedule = {
    "mon": ["Matematika", "Ingliz tili", "Fizika"],
    "tue": ["Ona tili", "Tarix", "Biologiya"],
    "wed": ["Geografiya", "Informatika", "Matematika"],
    "thu": ["Fizika", "Ingliz tili", "Tarix"],
    "fri": ["Matematika", "Biologiya", "Jismoniy tarbiya"],
}

days_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Dushanba", callback_data="day_mon")],
    [InlineKeyboardButton(text="Seshanba", callback_data="day_tue")],
    [InlineKeyboardButton(text="Chorshanba", callback_data="day_wed")],
    [InlineKeyboardButton(text="Payshanba", callback_data="day_thu")],
    [InlineKeyboardButton(text="Juma", callback_data="day_fri")],
])

@dp.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer(
        "Maktab jadvali botiga xush kelibsiz.\nKunni tanlang:",
        reply_markup=days_kb
    )


@dp.callback_query(F.data.startswith("day_"))
async def show_schedule(callback: CallbackQuery):
    day = callback.data.split("_")[1]
    lessons = schedule.get(day, [])

    if not lessons:
        text = "Bu kunga darslar topilmadi."
    else:
        text = "Darslar:\n"
        for i, lesson in enumerate(lessons, start=1):
            text += f"{i}) {lesson}\n"

    await callback.message.edit_text(text, reply_markup=days_kb)
    await callback.answer()


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
