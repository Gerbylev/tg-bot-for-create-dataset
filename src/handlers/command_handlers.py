from telegram import Update, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

from src.dao.user_dao import UserDAO
from src.handlers.message_handlers import process_message


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await process_message(update, context)


async def rating(update: Update, context: ContextTypes.DEFAULT_TYPE):
    rank, user = UserDAO.get_user_rank_by_contribution(update.effective_user.id)
    if rank is None or user.contribution == 0:
        await update.message.reply_text("Не участвует в рейтинге")
    else:
        await update.message.reply_text(f"Твой рейтинг - {rank}")
