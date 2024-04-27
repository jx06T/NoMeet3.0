import discord 
from discord.ext import commands
import socket
from Genv import ENV
from flask import Flask, request,jsonify
from flask_cors import CORS
import threading
import asyncio
import sched
import time
from threading import Timer
# ------------------------------------------------------------------------------------
def get_ip():
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address

def starDC(key):
    bot.run(key)

def remove_item(arr, item):
    # 使用列表推导式移除特定项
    return [x for x in arr if x != item]

def add_and_replace(arr, item):
    if item in arr:
        index = arr.index(item) 
        arr[index] = item 
    else:
        arr.append(item)  

async def get_member():
    people = data["people"]
    channel = bot.get_channel(int(ENV["MAIN_CHANNEL_ID"]))  # 填入要發送訊息的頻道 ID
    embed=discord.Embed(title="member", description="", color=0x860fbd)
    for i in  range(len(people)):
        embed.add_field(name=str(i+1)+"."+people[i], value="", inline=False)
    embed.set_footer(text=ENV["MainRoomCodde"])
    await channel.send(embed=embed)

AllMsg = []
data = {"rooms":[ENV["MainRoomCodde"]],"NewRooms":[],"OldRooms":[],"people":[],"DS":{"A_V":["?"],"A_S":["?"]}}
Lastfiles = []
# ------------------------------------------------------------------------------------

intents = discord.Intents.all()
bot = commands.Bot(command_prefix ="$", intents = intents)

@bot.event
async def on_message(message):
    # print(message.content)
    if message.attachments:
        for attachment in message.attachments:
            print("Attached File:", attachment.url)  # Print the URL of each attached file
            Lastfiles.append(attachment.url)
            bot.dispatch("lastfiles_update",Lastfiles)

    await bot.process_commands(message)

@bot.event
async def on_ready():
    print(f"Logged on as {bot.user}")
    channel = bot.get_channel(int(ENV["MAIN_CHANNEL_ID"]))  # 填入要發送訊息的頻道 ID
    await channel.send(f'{ENV["BOT_NAME"]}上線 ({get_ip()})')
    await bot.load_extension("cogs.msg")
    await bot.load_extension("cogs.fun")
    await bot.load_extension("cogs.setting")
    slash = await bot.tree.sync()
    bg_task = bot.loop.create_task(check_room())
    
# async def on_interaction(interaction: discord.Interaction):
#     if interaction.data.get("custom_id") in ["DEVICE_NAME_S","DEVICE_NAME_V","No_Entering"]:
# bot.add_listener(on_interaction)

@bot.event
async def on_get_DS():
    await asyncio.sleep(1)
    bot.dispatch("device_update",data["DS"])

@bot.event
async def on_get_member():
    await get_member()

@bot.event
async def on_msg_updated(allmsg):
    global AllMsg 
    AllMsg = allmsg
    print(AllMsg)

@bot.event
async def on_get_room_code():
    channel = bot.get_channel(int(ENV["MAIN_CHANNEL_ID"]))  # 填入要發送訊息的頻道 ID
    embed=discord.Embed(title="URL", url="https://meet.google.com/"+ENV["MainRoomCodde"], color=0x860fbd)
    embed.set_footer(text=ENV["MainRoomCodde"])
    await channel.send(embed=embed)

@bot.command()
async def unload(ctx,extension):
    await  bot.unload_extension(f"cogs.{extension}")
    # slash = await bot.tree.sync()
    await ctx.send(F'UnLoaded {extension} done.' )

@bot.command()
async def load(ctx,extension):
    await  bot.load_extension(f"cogs.{extension}")
    # slash = await bot.tree.sync()
    await ctx.send(F'Loaded {extension} done.' )

@bot.command()
async def reload(ctx,extension):
    await  bot.reload_extension(f"cogs.{extension}")
    # slash = await bot.tree.sync()
    await ctx.send(F'Reloaded {extension} done.' )

# -------------------------------------------------------------------------------------------------------------------------------
async def check_room():
    while not bot.is_closed():
        print(ENV["MainRoomCodde"],data["rooms"],data["NewRooms"],data["OldRooms"])
        channel = bot.get_channel(int(ENV["MAIN_CHANNEL_ID"]))  # 填入要發送訊息的頻道 ID

        for i in data["NewRooms"]:
            if ENV["MainRoomCodde"] == "AUTO":
                ENV["MainRoomCodde"] = i
                await channel.send(f'{ENV["BOT_NAME"]} 新會議 {i}(已設定)')
            else:
                await channel.send(f'{ENV["BOT_NAME"]} 新會議 {i}')
            bot.dispatch("rooms_update",data["rooms"])

        data["NewRooms"].clear()

        for i in data["OldRooms"]:
            await channel.send(f'{ENV["BOT_NAME"]} 離開 {i}')
            data["rooms"] = remove_item(data["rooms"],i)
            if len(data["rooms"])>0 and ENV["MainRoomCodde"] == i:
                ENV["MainRoomCodde"]  = data["rooms"][0]
                await channel.send(f'{ENV["BOT_NAME"]} 設定為 {ENV["MainRoomCodde"]}')

            bot.dispatch("rooms_update",data["rooms"])
            
        data["OldRooms"].clear()

        if not ENV["MainRoomCodde"]=="AUTO" and  all(s.strip() == "" for s in data["rooms"]):
            await channel.send(f'{ENV["BOT_NAME"]} 沒有會議')
            data["rooms"].clear()
            ENV["MainRoomCodde"] = "AUTO"
            bot.dispatch("ENV_update",ENV)

        for i in data["rooms"]:
            data["OldRooms"].append(i)
        
        await asyncio.sleep(6)
    
# -------------------------------------------------------------------------------------------------------------------------------
app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def api():
    rRoomCode = request.args.get('room_code')
    data["OldRooms"] = remove_item(data["OldRooms"],rRoomCode)
    
    if rRoomCode == ENV["MainRoomCodde"]:
        temp = AllMsg.copy()
        AllMsg.clear()  
    elif rRoomCode not in data["rooms"]:
        data["rooms"].append(rRoomCode)
        data["NewRooms"].append(rRoomCode)
        temp = []
    else:
        temp = []
        
    return jsonify(temp)

@app.route("/get", methods=['POST'])
def get():
    data_received = request.json
    data["people"] = data_received["people"]
    data["DS"]["A_V"] = data_received["A_V"]
    data["DS"]["A_S"] = data_received["A_S"]
    # print(data_received)  
    return "ok"
    

@app.route("/can_enter", methods=['GET'])
def gett():
    return ENV["No_Entering"]
    
if __name__=='__main__':
    DCthreads =threading.Thread(target=starDC,args=(ENV["DC_TOKEN"],))
    DCthreads.start()
    
    app.run()