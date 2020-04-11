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
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    

def Teste(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="outro comando /teste")

from ocr import bot_counter
from os import remove as delete

def readRawImage(update, context):
    file =  context.bot.getFile(update.message.photo[-1].file_id)
    path = file.file_id+'.jpeg'
    file.download(path)
    result = bot_counter(path)
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(result))
    delete(path)
    
#fazer eles serem chamados
from telegram.ext import CommandHandler 

dispatcher.add_handler(CommandHandler('start', Start))

dispatcher.add_handler(CommandHandler('teste', Teste))


from telegram.ext import MessageHandler, Filters
dispatcher.add_handler(MessageHandler(Filters.photo, readRawImage))

updater.start_polling()
