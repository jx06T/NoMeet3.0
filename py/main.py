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
import pygame
from sound import SoundPlayer
# from discord import app_commands

load_dotenv()
DC_TOKEN = os.getenv("DC_TOKEN")
BOT_NAME = os.getenv("BOT_NAME")
MAIN_CHANNEL_ID = os.getenv("MAIN_CHANNEL_ID")
SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(SCRIPT_DIRECTORY, ".env")
# ------------------------------------------------------------------------------------
def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def get_current_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_time

def update_env_variable(variable_name, new_value):
    os.environ[variable_name] = new_value
    # Write the updated value to the .env file
    with open(ENV_PATH, "r") as env_file:
        lines = env_file.readlines()
    with open(ENV_PATH, "w") as env_file:
        for line in lines:
            if line.startswith(f"{variable_name}="):
                env_file.write(f"{variable_name}={new_value}\n")
            else:
                env_file.write(line)
def get_view_forPlay(t):
    view = discord.ui.View()
    view.add_item(
        discord.ui.Button(
            label="▶" if not t else "■",
            style=discord.ButtonStyle.blurple,
            custom_id="pause"
        )
    )
    return view
# -------------------------------------------------------------------------------------------------------------------------------
AllMsg = []
player = SoundPlayer(os.getenv("DEVICE_NAME"))
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
    # c = 0
    # async for message in channel.history(limit=30):
    #     print(message.content)
    #     if message.author == bot.user:
    #         c+=1
    #     if c >1:
    #         print("!!")
    #         break

@bot.event
async def on_message(message):
    print(message.content)
    if message.attachments:
        for attachment in message.attachments:
            print("Attached File:", attachment.url)  # Print the URL of each attached file
    
    # if message.content == '誰是機器人':
    #     await message.channel.send('誰叫我？')
    await bot.process_commands(message)

# @bot.command()
# async def opt(ctx):
#     await ctx.send("opt")
# -------------------------------------------------------------------------------------------------------------------------------
    
@bot.tree.command(name = "msg", description = "發訊息")
@discord.app_commands.describe(msg=':')
@discord.app_commands.describe(force=':')
@discord.app_commands.describe(hide=':')
async def Cmsg(interaction: discord.Interaction,msg:str,force:Literal['T', 'F'] = "F",hide:Literal['T', 'F'] = "T"):  
    await interaction.response.send_message("ok")
    AllMsg.append({"type":"Cmsg","from":interaction.user.name,"msg":msg,"force":force,"hide":hide})
    print(AllMsg)

# -------------------------------------------------------------------------------------------------------------------------------
@bot.tree.command(name="sound", description="說話")
@discord.app_commands.describe(audio_file=':')
@discord.app_commands.describe(force=':')
async def Cmsg(interaction: discord.Interaction,audio_file: discord.Attachment,force:Literal['T', 'F'] = "F"):
    view = get_view_forPlay(False)
    await interaction.response.send_message(content=audio_file.filename, view=view)
    # 將音訊檔案存入本地
    if audio_file:
        with open(SCRIPT_DIRECTORY+"\\sound\\"+audio_file.filename, "wb") as f:
            await audio_file.save(f)

    player.change_file(SCRIPT_DIRECTORY+"\\sound\\"+audio_file.filename)
    AllMsg.append({"type": "sound", "from":interaction.user.name, "file": audio_file.filename, "force": force})
    print(AllMsg)
    player.play()
    player.pause()

class ModalClass(discord.ui.Modal, title = "設定名稱"):
    name = discord.ui.TextInput(label = "BotName")
    id = discord.ui.TextInput(label = "Channel-ID")
    devicename = discord.ui.TextInput(label = "devicename-s")
    # Modal 提交後接著要執行的程式碼
    async def on_submit(self, interaction: discord.Interaction):
        # await interaction.response.send_message(f"Hello, {self.name.value}!")
        await interaction.response.send_message(f"ok,{self.name.value}!")
        BOT_NAME = self.name.value
        MAIN_CHANNEL_ID = self.id.value
        update_env_variable("BOT_NAME",BOT_NAME)
        update_env_variable("MAIN_CHANNEL_ID",MAIN_CHANNEL_ID)
        update_env_variable("DEVICE_NAME",self.devicename.value)
        player.change_devicename(self.devicename.value)
        
@bot.tree.command(name = "setting", description = "設定")
async def setting(interaction: discord.Interaction):  
    # await ctx.send("Opening modal...")
    await interaction.response.send_modal(ModalClass())
# -------------------------------------------------------------------------------------------------------------------------------

# 透過裝飾器創建按鈕交互
@bot.tree.command(name = "fun", description = "fun")
async def fun(interaction: discord.Interaction):
    view = discord.ui.View()
    view.add_item(
        discord.ui.Button(
            label="quit",
            style=discord.ButtonStyle.blurple,
            custom_id="quit"
        )
    )
    view.add_item(
        discord.ui.Button(
            label="FakeQuit",
            style=discord.ButtonStyle.blurple,
            custom_id="FakeQuit"
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
            label="Emoji",
            style=discord.ButtonStyle.blurple,
            custom_id="SendEmoji"
        )
    )
    await interaction.response.send_message(content="", view=view)

@bot.tree.command(name = "info", description = "info")
async def info(interaction: discord.Interaction):
    view = discord.ui.View()
    view.add_item(
        discord.ui.Button(
            label="Member",
            style=discord.ButtonStyle.blurple,
            custom_id="member"
        )
    )
    view.add_item(
        discord.ui.Button(
            label="Reload",
            style=discord.ButtonStyle.blurple,
            custom_id="reload"
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
        # embed.set_thumbnail(url="https://today-obs.line-scdn.net/0hIIJgK7YRFmZ3HgVElldpMU9IGhdEeAxvVSwLCAcdQFAKMgVgTnpFBQEeQUpSflZiV3FQBlQaHwZfJwJkSA/w644")
        embed.set_footer(text=data["RoomCode"])
        await channel.send(embed=embed)
        
    elif interaction.data.get("custom_id") in["HoldHandx10","HoldHand","reload","quit","FakeQuit","SendEmoji"]:
        AllMsg.append({"type":"FUN","FUN":interaction.data.get("custom_id") ,"from":interaction.user.name})
        await interaction.response.edit_message(content="OK..."+str(math.floor(time.time()*10)))
        
    elif interaction.data.get("custom_id") == "pause":
        if player.is_playing:
            player.pause()
        else:
            player.unpause()

        # await interaction.response.edit_message(content=("playing" if player.is_playing else "stop") +str(math.floor(time.time()*10)))
        await interaction.response.edit_message(view=get_view_forPlay(player.is_playing))
        


async def Rmember():
    people = data["people"]
    channel = bot.get_channel(int(MAIN_CHANNEL_ID))  # 填入要發送訊息的頻道 ID
    embed=discord.Embed(title="member", description="", color=0x860fbd)
    # embed.set_thumbnail(url="https://today-obs.line-scdn.net/0hIIJgK7YRFmZ3HgVElldpMU9IGhdEeAxvVSwLCAcdQFAKMgVgTnpFBQEeQUpSflZiV3FQBlQaHwZfJwJkSA/w644")
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
