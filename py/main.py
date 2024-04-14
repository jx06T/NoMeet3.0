import threading
import discord 
from discord.ext import commands
import socket
from datetime import datetime
# from flask_ngrok import run_with_ngrok   # colab 使用，本機環境請刪除
from flask import Flask, request,jsonify
# import json
from dotenv import load_dotenv
import os
from flask_cors import CORS
from typing import Literal,Optional
import time
import asyncio
import math
# from discord import app_commands

load_dotenv()
DC_TOKEN = os.getenv("DC_TOKEN")
BOT_NAME = os.getenv("BOT_NAME")
MAIN_CHANNEL_ID = os.getenv("MAIN_CHANNEL_ID")

def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def get_current_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_time

# -------------------------------------------------------------------------------------------------------------------------------
AllMsg = []

intents = discord.Intents.all()
# intents = discord.Intents.default()
# intents.message_content = True
bot = commands.Bot(command_prefix ="$", intents = intents)

@bot.event
# 當機器人完成啟動
async def on_ready():
    print(f"Logged on as {bot.user}")
    channel = bot.get_channel(int(MAIN_CHANNEL_ID))  # 填入要發送訊息的頻道 ID
    await channel.send(f'{BOT_NAME}上線({get_ip()})')
    slash = await bot.tree.sync()
    c = 0
    async for message in channel.history(limit=30):
        print(message.content)
        if message.author == bot.user:
            c+=1
        if c >1:
            print("!!")
            break

@bot.event
async def on_message(message):
    print(message.content)
    # if message.content == '誰是機器人':
    #     await message.channel.send('誰叫我？')
    await bot.process_commands(message)

# @bot.command()
# async def opt(ctx):
#     await ctx.send("opt")
    
@bot.tree.command(name = "msg", description = "發訊息")
@discord.app_commands.describe(msg=':')
@discord.app_commands.describe(force=':')
@discord.app_commands.describe(hide=':')
async def Cmsg(interaction: discord.Interaction,msg:str,force:Literal['T', 'F'] = "F",hide:Literal['T', 'F'] = "T"):  
    await interaction.response.send_message("ok")
    AllMsg.append({"type":"Cmsg","from":interaction.user.name,"msg":msg,"force":force,"hide":hide})
    print(AllMsg)

# -------------------------------------------------------------------------------------------------------------------------------
class ModalClass(discord.ui.Modal, title = "設定名稱"):
    name = discord.ui.TextInput(label = "Name")
    # Modal 提交後接著要執行的程式碼
    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Hello, {self.name.value}!")
@bot.tree.command(name = "setting", description = "設定")
async def setting(interaction: discord.Interaction):  
    # await ctx.send("Opening modal...")
    await interaction.response.send_modal(ModalClass())
# -------------------------------------------------------------------------------------------------------------------------------

# 透過裝飾器創建按鈕交互
@bot.tree.command(name = "opt", description = "opt")
async def opt(interaction: discord.Interaction):
    view = discord.ui.View()
    view.add_item(
        discord.ui.Button(
            label="member",
            style=discord.ButtonStyle.blurple,
            custom_id="member"
        )
    )
    view.add_item(
        discord.ui.Button(
            label="quit",
            style=discord.ButtonStyle.blurple,
            custom_id="quit"
        )
    )
    view.add_item(
        discord.ui.Button(
            label="Reload",
            style=discord.ButtonStyle.blurple,
            custom_id="Reload"
        )
    )
    view.add_item(
        discord.ui.Button(
            label="HoldHand",
            style=discord.ButtonStyle.blurple,
            custom_id="HoldHand"
        )
    )
    view.add_item(
        discord.ui.Button(
            label="HoldHand x15",
            style=discord.ButtonStyle.blurple,
            custom_id="HoldHandx10"
        )
    )
    view.add_item(
        discord.ui.Button(
            label="MeetURL",
            style=discord.ButtonStyle.blurple,
            custom_id="GRoomCode"
        )
    )
    await interaction.response.send_message(content="", view=view)
    # await ctx.send(content="", view=view)

# 監聽按鈕交互動作
@bot.event
async def on_interaction(interaction: discord.Interaction):
    if interaction.data.get("custom_id") == "member":
        AllMsg.append({"type":"GET","from":interaction.user.name})
        await interaction.response.edit_message(content="Waiting..."+str(math.floor(time.time()*10)))
        await asyncio.sleep(1.5)
        await Rmember()
    elif interaction.data.get("custom_id") == "GRoomCode":
        # AllMsg.append({"type":"GET","from":interaction.user.name})
        await interaction.response.edit_message(content="Waiting..."+str(math.floor(time.time()*10)))
        
        channel = bot.get_channel(int(MAIN_CHANNEL_ID))  # 填入要發送訊息的頻道 ID
        embed=discord.Embed(title="URL", url="https://meet.google.com/"+data["RoomCode"], color=0x860fbd)
        embed.set_thumbnail(url="https://today-obs.line-scdn.net/0hIIJgK7YRFmZ3HgVElldpMU9IGhdEeAxvVSwLCAcdQFAKMgVgTnpFBQEeQUpSflZiV3FQBlQaHwZfJwJkSA/w644")
        embed.set_footer(text=data["RoomCode"])
        await channel.send(embed=embed)
    elif interaction.data.get("custom_id") in["HoldHandx10","HoldHand","Reload","quit"]:
        AllMsg.append({"type":"FUN","FUN":interaction.data.get("custom_id") ,"from":interaction.user.name})
        await interaction.response.edit_message(content="OK..."+str(math.floor(time.time()*10)))


async def Rmember():
    people = data["people"]
    channel = bot.get_channel(int(MAIN_CHANNEL_ID))  # 填入要發送訊息的頻道 ID
    embed=discord.Embed(title="member", description="", color=0x860fbd)
    embed.set_thumbnail(url="https://today-obs.line-scdn.net/0hIIJgK7YRFmZ3HgVElldpMU9IGhdEeAxvVSwLCAcdQFAKMgVgTnpFBQEeQUpSflZiV3FQBlQaHwZfJwJkSA/w644")
    for i in  range(len(people)):
        embed.add_field(name=str(i+1)+"."+people[i], value="", inline=False)
    embed.set_footer(text=data["RoomCode"])
    await channel.send(embed=embed)
# -------------------------------------------------------------------------------------------------------------------------------
 
def starDC(key):
    bot.run(key)
    

# -------------------------------------------------------------------------------------------------------------------------------
data = {}
app = Flask(__name__)
CORS(app)
TR =  asyncio.new_event_loop()
# @app.route("/", methods=['POST'])
# def Rmsg():
#     return AllMsg

@app.route("/", methods=['GET'])
def api():
    temp = AllMsg.copy()
    AllMsg.clear()  
    data["RoomCode"] = request.args.get('room_code')
    # print(data)
    return jsonify(temp)

@app.route("/get", methods=['POST'])
def get():
    data_received = request.json
    data["people"] = data_received["people"]
    print(data_received)  
    return "ok"

# @app.route("/", methods=['GET','POST'])
# def test():
#     return AllMsg


if __name__ == "__main__":
    DCthreads =threading.Thread(target=starDC,args=(DC_TOKEN,))
    DCthreads.start()
    app.run()
    pass
