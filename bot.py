
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import json
import requests
from pprint import pprint


print("BOT INITIALISED")
# Add your bot token. You can do this using the Telegram Botfather
updater = Updater(token='832579248:AAEB6Tfd67ZrTmV_laZa7KgAMTERyl76pHs', use_context=True)
dispatcher = updater.dispatcher

global dict
global data

event = set()

# Add the repo name and number of forks obtained from the JSON data of the github API
response = requests.get("https://api.github.com/orgs/fedora-infra/repos")
data = response.json()


 
    
for i in data:

        
    name = i["name"]
    fork = i["forks"] 


    dict = {name:fork}
    print(dict)
  
print(dict)



#dict = {'bodhi': 155,'fedora-packages': 58,'fedora-tagger': 25,'fedmsg': 93,'busmon': 2,'tahrir': 40,'tahrir-api': 16,'pkgwat.cli': 8,'pkgwat.api': 8,'fedora-openhw2012': 5,'datanommer': 16,'fedbadges': 14,'supybot-fedmsg': 2,'fedmsg_middleware': 4,'apps.fp.o': 32,'fedmsg_meta_fedora_infrastructure': 41,'packagedb': 3,'python-fedora': 32,'datagrepper': 21,'fas': 52,'fedmsg-notify': 5,'askbot-fedmsg': 1,'supybot-fedora': 14,'elections': 6,'kitchen': 12,'rube': 4,'fedocal': 16,'pkgdb2': 26,'gnome-tagger': 0,'flock-registration': 4,}   

             
    # /start command to indroduce itself
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="FURK bot here, I am at your service master")

# Read the text received by the sender and check the dictionary to see if it's there

# /forks <name_of_repo> 

def forks(update, context):
    
    chat_id = update.message.chat_id

    try:
       
        repo_name = "".join(context.args)

        print("Repo requested:", repo_name)

        update.message.reply_text('Searching...')

        print(dict.get(repo_name, "Repo not found :("))

        value = dict.get(repo_name, "Repo not found :(")

        update.message.reply_text(value)

        # Prints this message if there is any problem    
    except (IndexError, ValueError):
        update.message.reply_text('Usage: /forks <repo-name>')


dispatcher.add_handler(CommandHandler("forks", forks, pass_args=True,pass_job_queue=True,pass_chat_data=True))
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()