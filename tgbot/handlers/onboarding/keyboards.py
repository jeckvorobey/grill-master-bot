import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

from tgbot.handlers.onboarding.manage_data import SECRET_LEVEL_BUTTON
from tgbot.handlers.onboarding.static_text import github_button_text, secret_level_button_text, menu_text


def make_keyboard_for_start_command() -> InlineKeyboardMarkup:
    web_app = WebAppInfo("https://jeckvorobey.github.io/webapp/")
    buttons = [
        InlineKeyboardButton(menu_text, web_app=web_app),
    ]

    return InlineKeyboardMarkup([buttons])
