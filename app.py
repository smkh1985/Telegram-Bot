from googletrans import Translator


from telegram.ext import Updater,CommandHandler,MessageHandler, Filters
u=Updater('478164597:AAHVqFriOYPr9NfMRN-2GEOP5BUSIycN9EI')
dispatcher = u.dispatcher


def Translate(bot, update):
##    chat=update.message.chat
    inputname= update.message.text
##    inputname =' '.join(text)
    print(inputname)
    translator = Translator()
    translations = translator.translate([inputname], dest='fa')
    for translation in translations:
        bot.send_message(chat_id= update.message.chat_id,text=translation.text)
##    if(inputname=='ali'):
##        text = 'alavi'
##    elif inputname == 'shima':
##        text ='Javanmardi'
##    elif inputname == 'majid':
##        text = 'KHORASHADIZADEH'
##    else:
##        text = 'I dont know {}'.format(inputname)
##    name =chat['first_name']
    bot.send_message(chat_id= update.message.chat_id,text=text)
    print('welcom to this world')
def start_Func(bot, update):
    StartText='کاربر گرامي {} اين ربات يک مترجم انگليسي به فارسي است که توسط تیم پژوهشی پردازش تصویر دانشگاه یزد توسعه یافته است. لطفا متن خود را وارد کنید'.format(update.message.chat['first_name'])
    bot.send_message(chat_id= update.message.chat_id,text=StartText)
    print('this is a robot that can help u')

Translate_handler = MessageHandler(Filters.text, Translate)
dispatcher.add_handler(Translate_handler)

startHandler=CommandHandler('start',start_Func)
##WelCome_handler=CommandHandler('getname',getname_Func, pass_args=True)
dispatcher.add_handler(startHandler)
##dispatcher.add_handler(WelCome_handler)
u.start_polling()
u.idle()
