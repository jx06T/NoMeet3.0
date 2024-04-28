# from rich import print
import discord
from discord import app_commands
from discord.ext import commands
from _cog_class import cog_class
from typing import Literal,Optional
from sound import SoundPlayer
from Genv import ENV ,update_env_variable
import math
import time
import asyncio

class fun(cog_class):
    def __init__(self, bot):
        super().__init__(bot)
        self.AllMsg = []
        self.rooms = ["AUTO"]
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
        view.add_item(
            discord.ui.Select(custom_id="MainRoomCodde", placeholder="MainRoomCodde("+ENV["MainRoomCodde"]+")", options=[
                discord.SelectOption(label=room) for room in self.rooms
                ])
        )
        await interaction.response.send_message(content="", view=view)
    
    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        IDD = interaction.data.get("custom_id")
        if IDD == "member":
            self.AllMsg.append({"type":"GET","from":interaction.user.name})
            self.bot.dispatch("msg_updated", self.AllMsg)
            await interaction.response.edit_message(content="Waiting..."+str(math.floor(time.time()*10)))
            await asyncio.sleep(1.5)
            self.bot.dispatch("get_member")
            
        elif IDD == "GRoomCode":
            await interaction.response.edit_message(content="Waiting..."+str(math.floor(time.time()*10)))
            self.bot.dispatch("get_room_code")

        elif IDD in ["MainRoomCodde"]:
            update_env_variable("MainRoomCodde",interaction.data.get("values")[0])
            await interaction.response.send_message(content ="ok")
            
        elif IDD in["HoldHandx10","HoldHand","reload","quit","FakeQuit","SendEmoji"]:
            self.AllMsg.append({"type":"FUN","FUN":IDD ,"from":interaction.user.name})
            self.bot.dispatch("msg_updated", self.AllMsg)
            await interaction.response.edit_message(content="OK..."+str(math.floor(time.time()*10)))
            
    @commands.Cog.listener()
    async def on_rooms_update(self,rooms):
        self.rooms = rooms.copy()
        if len(self.rooms)==0:
            self.rooms.append("AUTO")
        print("rooms",rooms)

    @commands.Cog.listener()
    async def on_ENV_update(self,env):
        ENV = env
        print("envvv")   
            

async def setup(bot):
    await bot.add_cog(fun(bot))