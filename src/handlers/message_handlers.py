from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler

from src.services.BaseServices import BaseService
from src.services.StatusService import StatusService

status_service = StatusService()

async def process_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text, buttons = status_service.magic(update, context)
    reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=False)
    await update.message.reply_text(message_text, reply_markup=reply_markup)