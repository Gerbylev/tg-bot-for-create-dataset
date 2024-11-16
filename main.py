from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
# from state.state_manager import StateManager

from src.config.Config import CONFIG
from src.handlers.command_handlers import rating, start
from src.handlers.message_handlers import process_message


def main():
    application = ApplicationBuilder().token(CONFIG.botConfig.token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("rating", rating))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_message))

    application.run_polling()


if __name__ == '__main__':
    main()
