from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kboard


# Подключение роутера (посредника) для замены роли диспетчера
router = Router()


class Registration(StatesGroup):
    name = State()
    age = State()
    genre = State()


# Команды, определяющие функционал (пишутся через /)
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет! Я - бот по имени Movisor. \n\
Прежде чем помогать тебе в выборе фильма, я должен узнать о тебе побольше - \
это нужно для того, чтобы мне легче было с тобой общаться и чтобы я смог \
выводить тебе фильмы c ограничением 18+. \n\n\
Чтобы сделать это - напиши команду /reg.")


@router.message(Command("reg"))
async def cmd_reg(message: Message, state: FSMContext):
    await state.set_state(Registration.name)
    await message.answer("Для начала скажи, как я могу к тебе обращаться:")


# Регистрация
@router.message(Registration.name)
async def reg_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Registration.age)
    await message.answer("Я должен знать, что тебе можно смотреть все фильмы. \
поэтому введи свой возраст:")


@router.message(Registration.age)
async def reg_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Registration.genre)
    await message.answer("Чтобы мои рекомендации работали точнее, \
введи свой любимый жанр фильмов:")


@router.message(Registration.genre)
async def reg_genre(message: Message, state: FSMContext):
    await state.update_data(genre=message.text)
    data = await state.get_data()
    await message.answer(f"Спасибо, информация сохранена.\nИмя: {data["name"]}\n\
Возраст: {data["age"]}\nЛюбимый жанр: {data["genre"]}.\n\n\
Рад знакомству, {data["name"]}! \nЧтобы вызвать меню - напиши /menu.")
    await state.clear()
##


@router.message(Command("menu"))
async def cmd_menu(message: Message):
    await message.answer(text="Выбери пункт меню:", reply_markup=kboard.menu)


@router.message(Command("more"))
async def cmd_more(message: Message):
    await message.answer(text="Выбери пункт меню:", reply_markup=kboard.more)


@router.message(Command("help"))
async def cmd_help(message: Message):
    with open("misc/help_commands.txt", "r", encoding="UTF-8") as file:
        help_text = file.read()
    await message.answer(help_text)
#


# Фильтр-команды и коллбэки, реагирующие на ситуации
@router.message(F.text == "Пока!")
async def f_text_thanks(message: Message):
    await message.answer("И вам, рад был помочь!", reply_markup=ReplyKeyboardRemove())


@router.message(F.text == "Ещё")
async def more(message: Message):
    await message.answer(text="Выбери пункт меню:", reply_markup=kboard.more)


@router.message(F.text == "Рекомендация")
async def recommend(message: Message):
    await message.answer("Recommendation.")


@router.message(F.text == "Помощь")
async def help(message: Message):
    with open("misc/help_commands.txt", "r", encoding="UTF-8") as file:
        help_text = file.read()
    await message.answer(help_text)


@router.callback_query(F.data == "contacts")
async def contacts(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.edit_text("Связаться с нами можно через:", reply_markup=kboard.contacts)


@router.callback_query(F.data == "about_us")
async def about_us(callback: CallbackQuery):
    with open("misc/about_us.txt", "r", encoding="UTF-8") as file:
        about_text = file.read()
    await callback.answer("")
    await callback.message.edit_text(about_text, reply_markup=kboard.previous)


@router.callback_query(F.data == "back")
async def back(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.edit_text(text="Выбери пункт меню:", reply_markup=kboard.more)


@router.callback_query(F.data == "close_keyboard")
async def close_keyboard(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.delete()
    await callback.message.edit_reply_markup(reply_markup=ReplyKeyboardRemove())
