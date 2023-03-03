import logging
from telegram import Update
from telegram.ext import ContextTypes
from bot.dopfunk import btn_val, valyuta

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)

    await update.message.reply_text("Valyutani tanlang", reply_markup=btn_val())


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start to test this bot.\n"
                                    "Use /info to info this user.\n"
                                    "Use /caps to caps this text.")


async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f'username: {user.username}\n'
                                        f'user_id: {user.id}\n'
                                        f'Premium: {user.is_premium}\n'
                                        f'ism: {user.first_name}\n'
                                        f'familiya: {user.last_name}\n'
                                        f'language: {user.language_code}\n')


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global page
    page = 0
    msg = update.message.text
    if msg == '⬅back' or msg == 'next➡':
        if msg == 'next➡':
            page += 9
            return await update.message.reply_text('Valyutani tanlang', reply_markup=btn_val(page))

    a = update.message.text.split('(')[1]
    val = valyuta(a.split(')')[0])
    r = f'''
Rate: {val['Rate']}
Nomi: {val['CcyNm_UZ']}
Code: {val['Code']}
Date: {val['Date']}
'''
    await context.bot.send_message(chat_id=update.effective_chat.id, text=r)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()

    await query.edit_message_text(text=f"Selected option: {query.data}")


async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

