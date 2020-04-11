from telegram.ext import Updater
updater = Updater(token='924523571:AAENtlPHc8RXYARHVwJLt1J22usmtcVN8yM', use_context=True)
#acessar meu bot

dispatcher = updater.dispatcher

#lidar com erros
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

#criando os comandos
def Start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I can count how many bots are on your Call of Duty Mobile match\nJust send me a screenshot of the scoreboard??\nFor additional information simply type /about")

def About(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Maybe you are wondering how do I guess who looks like a bot and who doesnt")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Thats actually not that hard\nUsually bots have the same names, so I gathered information about their names playing many times at Pratice Against AI, so I guess im a snitch Bot")
    context.bot.send_message(chat_id=update.effective_chat.id, text="If you found someone that I thought was a bot and you disagree let me know at /feedback  ??")
    context.bot.send_message(chat_id=update.effective_chat.id, text="If you enjoyed my work you can support me at /donate , I really would appreciate that")


def Donate(update,context):
    pass

def Feedback(update,context):
    pass


from ocr import bot_counter
from os import remove as delete

def readRawImage(update, context):
    file =  context.bot.getFile(update.message.photo[-1].file_id)
    path = file.file_id+'.jpeg'
    file.download(path)
    result = bot_counter(path)
    if (len(result)>0):
        texto = 'There are at least ' +str (len(result))+ ' bots in this match\n'
        for i in result: #aprendendo o texto
            texto = texto + i + ' ,' 
        texto = texto[:-2] #removendo a ultima virgula
    else: #texto para se n tiver bot
        texto = "I couldn't find any bot in this match ????"
    context.bot.send_message(chat_id=update.effective_chat.id, text= texto , reply_to_message_id =update.message.message_id)
    delete(path)
    
#fazer eles serem chamados
from telegram.ext import CommandHandler 

dispatcher.add_handler(CommandHandler('start', Start))
dispatcher.add_handler(CommandHandler('about', About))



from telegram.ext import MessageHandler, Filters
dispatcher.add_handler(MessageHandler(Filters.photo, readRawImage))

updater.start_polling()