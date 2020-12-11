telegramToken = ''
from telegram.ext import Updater
updater = Updater(token=telegramToken, use_context=True)
#acessar meu bot

dispatcher = updater.dispatcher

#lidar com erros
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


#criando os comandos
def Start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I can count how many bots are on your Call of Duty Mobile match\nJust send me a screenshot of the scoreboard📸\nFor additional information simply type /about")

def About(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="If you are confused about the usage of this application type /tutorial")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Maybe you are wondering how do I guess who looks like a bot and who doesnt")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Thats actually not that hard\nUsually bots have the same names, so I gathered information about their names playing many times at Pratice Against AI, so I guess im a snitch Bot")
    context.bot.send_message(chat_id=update.effective_chat.id, text="If you found someone that I thought was a bot and you disagree let me know at /feedback  👍")
    context.bot.send_message(chat_id=update.effective_chat.id, text="If you enjoyed my work you can support me at /donate , I really would appreciate that")

def Tutorial(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="It's really simple to use my services")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Just send me any screenshot of an in game scoreboard")
    tutorial_screenshot = context.bot.send_photo(chat_id=update.effective_chat.id, photo= open('stock.jpg', 'rb') , caption = "Like this one").message_id
    context.bot.send_message(chat_id=update.effective_chat.id, text="Then I'll reply like that :")
    context.bot.send_message(chat_id=update.effective_chat.id, text="There are at least 6 bots in this match:\n🔵 wreckU\n🔵 Apiodelodo\n🔴 ClamBamFam\n🔴 LILpyro\n🔴 HooRay\n🔴 JamminJerry"    , reply_to_message_id = tutorial_screenshot)
    

def Donate(update,context):
    pass

def Feedback(update,context):
    pass


from ocr import bot_counter
from os import remove as delete

def readRawImage(update, context):
    file =  context.bot.getFile(update.message.photo[-1].file_id)   #recive the image url on telegram server
    path = file.file_id+'.jpeg'
    file.download(path) #download image with a unique name
    
    
    try:
        result = bot_counter(path,update.message.photo[-1].width) #try to recive 2 lists with the botnames by analyzing the downloaded image
        
    except RuntimeError:
        texto = "That definitely insn't a CODM match screenshot😫\nIf you are confused about the usage of this application type /tutorial"
        
        delete(path) #delete the image
    else:
        delete(path) #delete the image if didnt raise error 
        if (len(result[0])+len(result[1]) > 0): #aprendendo o texto, pegando as duas listas
            texto = 'There are at least ' + str(len(result[0])+len(result[1])) + ' bots in this match: \n'
            for i in result[0]:
                texto +='🔵 ' + i + '\n'
            for i in result[1]:
                texto +='🔴 ' + i + '\n'
        else: #texto para se n tiver bot
            texto = "I couldn't find any bot in this match 🤔🤔"
    context.bot.send_message(chat_id=update.effective_chat.id, text= texto , reply_to_message_id =update.message.message_id)
    
#fazer eles serem chamados
from telegram.ext import CommandHandler 

dispatcher.add_handler(CommandHandler('start', Start))
dispatcher.add_handler(CommandHandler('about', About))
dispatcher.add_handler(CommandHandler('tutorial', Tutorial))
dispatcher.add_handler(CommandHandler('feedback', Feedback))
dispatcher.add_handler(CommandHandler('donate', Donate))


from telegram.ext import MessageHandler, Filters
dispatcher.add_handler(MessageHandler(Filters.photo, readRawImage))

updater.start_polling()