# This example requires the 'message_content' intent.

import threading
import discord 
AllMsg = []

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # print(f'Message from {message.author}: {message.content}')
        print(AllMsg)
        AllMsg.append({"from":message.author.name,"msg":message.content})

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

def starDC(key):
    client.run(key)

# -------------------------------------------------------------------------------------------------------------------------------
# from flask_ngrok import run_with_ngrok   # colab 使用，本機環境請刪除
from flask import Flask, request
# import json
from dotenv import load_dotenv
import os

load_dotenv()
DC_TOKEN = os.getenv("DC_TOKEN")
app = Flask(__name__)


# @app.route("/", methods=['POST'])
# def Rmsg():
#     return AllMsg


@app.route("/", methods=['GET','POST'])
def test():
    temp = AllMsg
    AllMsg.clear()  
    return temp

if __name__ == "__main__":
    DCthreads =threading.Thread(target=starDC,args=(DC_TOKEN,))
    DCthreads.start()
    app.run()
    pass
