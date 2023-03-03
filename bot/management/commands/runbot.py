from django.core.management import BaseCommand
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from bot.views import start, echo, info, caps, help_command, button
from src.settings import bot_token


class Command(BaseCommand):
    def handle(self, *args, **options):
        application = ApplicationBuilder().token(bot_token).build()

        application.add_handler(CommandHandler('start', start))
        application.add_handler(CommandHandler('info', info))
        application.add_handler(CommandHandler('caps', caps))
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(CallbackQueryHandler(button))
        application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))

        application.run_polling()

