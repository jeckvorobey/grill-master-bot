from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from tgbot.handlers.onboarding.manage_data import SECRET_LEVEL_BUTTON
from tgbot.handlers.onboarding.static_text import github_button_text, secret_level_button_text, menu_text


def make_keyboard_for_start_command() -> InlineKeyboardMarkup:
    buttons = [
        InlineKeyboardButton(menu_text, url="http://192.168.1.10:9000/"),
    ]

    return InlineKeyboardMarkup([buttons])
