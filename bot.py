from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler


def echo(update, context):
    try:
        list = update.message.text.split(' ')
        print(list[1:])
        print(context.text)
        update.message.reply_text('succesful')
    except:
        update.message.reply_text('something went wrong')


def main():
    updater = Updater('1515524053:AAFWWpQGYRb6rZ6UeVFhdFfviOHXTqzgkkY', use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("draw", echo))
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()