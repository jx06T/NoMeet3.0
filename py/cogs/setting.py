import discord
from discord import app_commands
from discord.ext import commands
from discord.utils import MISSING
from _cog_class import cog_class
from typing import Literal,Optional
from Genv import ENV,update_env_variable
import math
import time
import asyncio
class setting(cog_class):
    def __init__(self, bot):
        super().__init__(bot)
        self.AllMsg = []
        # self.devices = {"V":[],"S":[]}
        self.devices = {"A_V":["?"],"A_S":["?"]}
        print("setting load")
        

    class ModalClass(discord.ui.Modal, title = "設定-A"):
        def __init__(self,bot):
            super().__init__()
            self.bot = bot
            self.add_item(discord.ui.TextInput(custom_id ="BOT_NAME",label = "BotName",default = ENV["BOT_NAME"]))
            self.add_item(discord.ui.TextInput(custom_id = "MAIN_CHANNEL_ID",label = "Channel-ID",default = ENV["MAIN_CHANNEL_ID"]))
            self.add_item(discord.ui.TextInput(custom_id = "_delete",label = "!!delete!!",default = "___"))
            # self.add_item(discord.ui.TextInput(custom_id="DEVICE_NAME",label = "devicename-s",default = ENV["DEVICE_NAME"]))
        # MainRoomCodde = discord.ui.TextInput(label = "MainRoomCodde",default = ENV["MainRoomCodde"])
        async def on_submit(self, interaction: discord.Interaction):
            for item in self.children:
                R = update_env_variable(item.custom_id,item.value)
            await interaction.response.send_message(f"ok!")
            self.bot.dispatch("ENV_update",R)

    class SelectView(discord.ui.View):
        def __init__(self,devices):
            super().__init__()
            self.add_item(
            discord.ui.Button(
                label="R",
                style=discord.ButtonStyle.blurple,
                custom_id="RRRR"
            )
            )
            self.add_item(
                discord.ui.Select(custom_id="DEVICE_NAME_S", placeholder="Sound_Device", options=
                    [discord.SelectOption(label=D) for D in self.remove_duplicates(devices['A_S'])]
                )
            )
            self.add_item(
                discord.ui.Select(custom_id="DEVICE_NAME_V", placeholder="Video_Device", options=
                    [discord.SelectOption(label=D) for D in self.remove_duplicates(devices['A_V'])]
                )
            )
            self.add_item(
                discord.ui.Select(custom_id="No_Entering", placeholder="No_Entering",
                    options=[
                    discord.SelectOption(label="F"),
                    discord.SelectOption(label="T")
                    ]
                )
            )
        def remove_duplicates(self,lst):
            lst = [item.rstrip() for item in lst]  # 移除每个字符串末尾的空格
            t = list(set(lst))
            # print(t[:25])
            return t

    @app_commands.command(name = "setting", description = "設定")
    @discord.app_commands.describe(all=':')
    async def setting(self,interaction: discord.Interaction,all:Literal['T', 'F'] = "F"):  
        if all == "T":
            await interaction.response.send_modal(self.ModalClass(self.bot))
        else:
            self.AllMsg.append({"type":"GET","from":interaction.user.name})
            self.bot.dispatch("msg_updated", self.AllMsg)
            self.bot.dispatch("get_DS")
            await interaction.response.send_message(content="Waiting..."+str(math.floor(time.time()*10)))
            
    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        if interaction.data.get("custom_id") in ["DEVICE_NAME_S","DEVICE_NAME_V","No_Entering"]:
            await interaction.response.send_message(content=interaction.data.get("custom_id")+"："+interaction.data.get("values")[0])
            R = update_env_variable(interaction.data.get("custom_id"),interaction.data.get("values")[0])
            self.bot.dispatch("ENV_update",R)
        elif interaction.data.get("custom_id") == "RRRR":
            await interaction.response.send_message(content="ok")
            self.AllMsg.append({"type":"GET1","from":interaction.user.name})
            self.bot.dispatch("msg_updated", self.AllMsg)
            await asyncio.sleep(2)
            self.bot.dispatch("get_DS")




    @commands.Cog.listener()
    async def on_device_update(self,d):
        print("device",d)
        self.devices = d.copy()
        channel = self.bot.get_channel(int(ENV["MAIN_CHANNEL_ID"]))  # 填入要發送訊息的頻道 ID
        await channel.send(view=self.SelectView(self.devices))


   
async def setup(bot):
    await bot.add_cog(setting(bot))