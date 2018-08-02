from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
import serial, time

help_text = """
Welcome to your DoorBot. I automatically decide who goes into your house for you, with your permission of course :)

Let me introduce you to the commands:

/help: That's me! At your service! 
/photo: Send the most recent picture of the guest in the Database
/all_photo: Send all the pictures of the guest in the Database
/open_door: Open the door at your designated house and let the guests in
"""


def arduino_open_door():
    print("Opening Door")
    ser = serial.Serial(port='COM3', baudrate=9600)
    time.sleep(2)
    ser.write('1'.encode())
    ser.close()


def help(bot, update):
    update.message.reply_text(help_text)


def echo(bot, update):
    update.message.reply_text('Hi! I am your DoorBot. Please go to /help for further details')


def open_door(bot, update):
    arduino_open_door()
    update.message.reply_text("The door has been opened")


def send_most_recent_pic(bot, update):
    try:
        update.message.reply_text("Sending most recent picture...")
        bot.send_photo(chat_id=update.message.chat_id, photo=open('./DataBase/test_pic_4.jpg', 'rb'))
    except Exception as e:
        print("Could not read file from Database. Picture sending failed")
        update.message.reply_text("Unable to send picture due to the error: " + str(e))


def send_all_pics(bot, update):
    try:
        update.message.reply_text("Sending all pictures...")
        for pic in range(5):
            bot.send_photo(chat_id=update.message.chat_id, photo=open('./DataBase/test_pic_' + str(pic) + '.jpg', 'rb'))
    except Exception as e:
        print("Could not read file from Database. Picture sending failed")
        update.message.reply_text("Unable to send picture due to the error: " + str(e))


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater('629898347:AAG4beXS5T7KwlLfbTdtnSgAzbIUec55-ik')

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("photo", send_most_recent_pic))
    dp.add_handler(CommandHandler("all_photo", send_all_pics))
    dp.add_handler(CommandHandler("open_door", open_door))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
