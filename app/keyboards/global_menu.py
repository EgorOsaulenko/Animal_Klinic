from aiogram.utils.keyboard import ReplyKeyboardBuilder


def build_global_menu():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Список тварин")
    builder.button(text="Додати нову тварину")
    builder.button(text="Вилікувані тварини")
    builder.button(text="Додати відгук")
    builder.button(text="Показати всі відгуки")
    builder.adjust(1)
    return builder.as_markup()