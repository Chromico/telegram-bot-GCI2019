from telegram.ext import Updater
from telegram.ext import CommandHandler
import json
import requests


updater = Updater(token='832579248:AAEB6Tfd67ZrTmV_laZa7KgAMTERyl76pHs', use_context=True)

dispatcher = updater.dispatcher


#response = requests.get("https://api.github.com/repos/fedora-infra/bodhi")
#data = response.json()
#fork = data["forks_count"]

response = requests.get("https://api.github.com/repos/fedora-infra/bodhi")
data = response.json()
fork2 = data["forks_count"]


response = requests.get("https://api.github.com/repos/fedora-infra/bodhi")
data = response.json()
fork3 = data["forks_count"]


response = requests.get("https://api.github.com/repos/fedora-infra/bodhi")
data = response.json()
fork4 = data["forks_count"]


response = requests.get("https://api.github.com/repos/fedora-infra/bodhi")
data = response.json()
fork5 = data["forks_count"]


response = requests.get("https://api.github.com/repos/fedora-infra/bodhi")
data = response.json()
fork6 = data["forks_count"]


response = requests.get("https://api.github.com/repos/fedora-infra/bodhi")
data = response.json()
fork7 = data["forks_count"]


response = requests.get("https://api.github.com/repos/fedora-infra/bodhi")
data = response.json()
fork8 = data["forks_count"]


response = requests.get("https://api.github.com/repos/fedora-infra/bodhi")
data = response.json()
fork9 = data["forks_count"]


response = requests.get("https://api.github.com/repos/fedora-infra/bodhi")
data = response.json()
fork10 = data["forks_count"]


response = requests.get("https://api.github.com/repos/fedora-infra/bodhi")
data = response.json()
fork11 = data["forks_count"]


response = requests.get("https://api.github.com/repos/fedora-infra/bodhi")
data = response.json()
fork12 = data["forks_count"]


response = requests.get("https://api.github.com/repos/fedora-infra/bodhi")
data = response.json()
fork13 = data["forks_count"]


response = requests.get("https://api.github.com/repos/fedora-infra/bodhi")
data = response.json()
fork14 = data["forks_count"]


response = requests.get("https://api.github.com/repos/fedora-infra/bodhi")
data = response.json()
fork15 = data["forks_count"]


response = requests.get("https://api.github.com/repos/fedora-infra/bodhi")
data = response.json()
fork16 = data["forks_count"]


response = requests.get("https://api.github.com/repos/fedora-infra/bodhi")
data = response.json()
fork17 = data["forks_count"]


response = requests.get("https://api.github.com/repos/fedora-infra/bodhi")
data = response.json()
fork18 = data["forks_count"]


response = requests.get("https://api.github.com/repos/fedora-infra/bodhi")
data = response.json()
fork19 = data["forks_count"]


response = requests.get("https://api.github.com/repos/fedora-infra/bodhi")
data = response.json()
fork20 = data["forks_count"]


response = requests.get("https://api.github.com/repos/fedora-infra/bodhi")
data = response.json()
fork21 = data["forks_count"]


response = requests.get("https://api.github.com/repos/fedora-infra/bodhi")
data = response.json()
fork22 = data["forks_count"]


response = requests.get("https://api.github.com/repos/fedora-infra/bodhi")
data = response.json()
fork23 = data["forks_count"]


response = requests.get("https://api.github.com/repos/fedora-infra/bodhi")
data = response.json()
fork24 = data["forks_count"]


response = requests.get("https://api.github.com/repos/fedora-infra/bodhi")
data = response.json()
fork25 = data["forks_count"]


response = requests.get("https://api.github.com/repos/fedora-infra/bodhi")
data = response.json()
fork26 = data["forks_count"]


response = requests.get("https://api.github.com/repos/fedora-infra/bodhi")
data = response.json()
fork27 = data["forks_count"]


response = requests.get("https://api.github.com/repos/fedora-infra/bodhi")
data = response.json()
fork28 = data["forks_count"]


response = requests.get("https://api.github.com/repos/fedora-infra/bodhi")
data = response.json()
fork29 = data["forks_count"]




def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Kreiger bot here, I am at your service master")

def fork(update, context):


    context.bot.send_message(chat_id=update.effective_chat.id, text="Here are the number of forks from the fedora repo api")

    context.bot.send_message(chat_id=update.effective_chat.id, text="Repo 1:")
    context.bot.send_message(chat_id=update.effective_chat.id, text=fork10)






start_handler = CommandHandler('ACTIVATE', start)
get_fork_handler = CommandHandler('forks', fork)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(get_fork_handler)

updater.start_polling()