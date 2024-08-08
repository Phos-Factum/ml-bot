from aiogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,
                           KeyboardButton, InlineKeyboardButton)


menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Рекомендация")],
    [KeyboardButton(text="Помощь"),
     KeyboardButton(text="Ещё")], 
    [KeyboardButton(text="Пока!")]
], 
                    resize_keyboard=True, 
                    input_field_placeholder="Выбери пункт меню")


previous = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Назад", callback_data="back")]
])


more = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Контакты", callback_data="contacts")],
    [InlineKeyboardButton(text="О нас", callback_data="about_us")],
    [InlineKeyboardButton(text="Закрыть", callback_data="close_keyboard")]
])


contacts = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Telegram разработчика бота", url="https://t.me/Necro_Phosphorite")],
    [InlineKeyboardButton(text="VK разработчика бота", url = "https://vk.com/necro_phosphorite")],
    [InlineKeyboardButton(text="Telegram ML-разработчика", url = "https://t.me/Necro_Phosphorite")],
    [InlineKeyboardButton(text="Назад", callback_data="back")]
])
