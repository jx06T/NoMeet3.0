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
        self.devices = {"A_V":["?"],"A_S":["?"]}
        print("setting load")
        

    class ModalClass(discord.ui.Modal, title = "設定-A"):
        def __init__(self,bot):
            super().__init__()
            self.bot = bot
            self.add_item(discord.ui.TextInput(custom_id ="BOT_NAME",label = "BotName",default = ENV["BOT_NAME"]))
            self.add_item(discord.ui.TextInput(custom_id = "MAIN_CHANNEL_ID",label = "Channel-ID",default = ENV["MAIN_CHANNEL_ID"]))
            self.add_item(discord.ui.TextInput(custom_id = "_delete_S_V_file",label = "!!delete_S-V-file!!(type 'DELETE-S-V')",default = "___"))
            self.add_item(discord.ui.TextInput(custom_id = "_delete_all",label = "!!deleteALL!!(type 'DELETE-ALL')",default = "___"))
            
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
                custom_id="reget_Ds"
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
        IDD = interaction.data.get("custom_id")
        if IDD in ["DEVICE_NAME_S","DEVICE_NAME_V","No_Entering"]:
            await interaction.response.send_message(content=IDD+"："+interaction.data.get("values")[0])
            R = update_env_variable(IDD,interaction.data.get("values")[0])
            self.bot.dispatch("ENV_update",R)

        elif IDD == "reget_Ds":
            await interaction.response.send_message(content="ok")
            self.AllMsg.append({"type":"GET1","from":interaction.user.name})
            self.bot.dispatch("msg_updated", self.AllMsg)
            await asyncio.sleep(2)
            self.bot.dispatch("get_DS")
        elif IDD == "No_Entering" :
            await interaction.response.send_message(content=IDD+"："+interaction.data.get("value"))
            R = update_env_variable(IDD,interaction.data.get("value"))
            self.bot.dispatch("ENV_update",R)




    @commands.Cog.listener()
    async def on_device_update(self,d):
        print("device",d)
        self.devices = d.copy()
        channel = self.bot.get_channel(int(ENV["MAIN_CHANNEL_ID"])) 
        await channel.send(view=self.SelectView(self.devices))


   
async def setup(bot):
    await bot.add_cog(setting(bot))