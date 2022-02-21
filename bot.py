import telebot
from datetime import datetime
import time
bot = telebot.TeleBot('5161579558:AAHJp1QJgH9IzC_fCFGZ2I2r8fCdSORRlbw')
ChatId = 320643255
with open("AffectionateNames.txt") as file:
    ListWord = file.readlines()
NumWord = 0
def GoodMorning():
    bot.send_message(ChatId, 'Доброе утро, ' + ListWord[NumWord])
    ++NumWord
def main():
    while True:
        if datetime.now().hour == 8 and datetime.now().minute == 0:
            GoodMorning()        
        if abs(datetime.now().hour - 8) > 1 or abs(datetime.now().hour - 8) == 0:
            time.sleep(3600)
        else:
            time.sleep(1)
        
    
