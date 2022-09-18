import Constants as keys
from telegram.ext import * 
import Responses as R


print("Bot started...")

def start_command(update,context):
    update.message.reply_text('type someting to get started!')

def help_command(update,context):
    update.message.reply_text('if u need help search it on google')

def handler_message(update,context):
    text=str(update.message.text).lower()
    responses=R.sample_responses(text)
    
    update.message.reply_text(responses)

def error(update,context):
    print(f"Update{update} caused error {context.error}")

def main():
    updater=Updater(keys.API_KEY,use_context=True)
    dp=updater.dispatcher
    
    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("help",help_command))

    dp.add_handler(MessageHandler(Filters.text,handler_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()