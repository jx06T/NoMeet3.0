import discord
from discord import app_commands
from discord.ext import commands
from _cog_class import cog_class
from typing import Literal,Optional
from sound import SoundPlayer
from env import ENV 
import math
import time
import asyncio

class main(cog_class):
    def __init__(self, bot):
        super().__init__(bot)
        self.AllMsg = []
        print("fun load")
        
    @app_commands.command(name = "fun", description = "fun")
    async def fun(self,interaction: discord.Interaction):
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

    @app_commands.command(name = "info", description = "info")
    async def info(self,interaction: discord.Interaction):
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

    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        if interaction.data.get("custom_id") == "member":
            self.AllMsg.append({"type":"GET","from":interaction.user.name})
            self.bot.dispatch("msg_updated", self.AllMsg)
            await interaction.response.edit_message(content="Waiting..."+str(math.floor(time.time()*10)))
            await asyncio.sleep(1.5)
            self.bot.dispatch("get_member")
            
        elif interaction.data.get("custom_id") == "GRoomCode":
            await interaction.response.edit_message(content="Waiting..."+str(math.floor(time.time()*10)))
            self.bot.dispatch("get_room_code")
        
        elif interaction.data.get("custom_id") in["HoldHandx10","HoldHand","reload","quit","FakeQuit","SendEmoji"]:
            self.AllMsg.append({"type":"FUN","FUN":interaction.data.get("custom_id") ,"from":interaction.user.name})
            self.bot.dispatch("msg_updated", self.AllMsg)
            await interaction.response.edit_message(content="OK..."+str(math.floor(time.time()*10)))

    @commands.Cog.listener()
    async def on_ENV_update(self,env):
        ENV = env
        print("envvv")   
            

async def setup(bot):
    await bot.add_cog(main(bot))