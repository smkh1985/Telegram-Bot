from telegram import Bot
from telegram.ext import CommandHandler,Updater


token = '478164597:AAHVqFriOYPr9NfMRN-2GEOP5BUSIycN9EI'
bot = Bot(token)

botInfo = bot.get_me()
print(botInfo.name)

updater = Updater(bot= bot)
dispatcher = updater.dispatcher

def startFcn(bot,update):
    chat = update.message.chat
    chatid = chat['id']
    firstName = chat['first_name']
    message = 'سلام {}. من یک ربات هستم که میتوانم در انجام کارهایی از قبیل ترجمه یک متن به زبانهای مختلف به تو کمک کنم.'
    bot.send_message(chat_id = chatid,text =message.format(firstName))


start_handler = CommandHandler('start',startFcn)
dispatcher.add_handler(start_handler)

updater.start_polling()