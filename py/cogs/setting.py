import discord
from discord import app_commands
from discord.ext import commands
from _cog_class import cog_class
from typing import Literal,Optional
from sound import SoundPlayer
from env import ENV,update_env_variable

class setting(cog_class):
    def __init__(self, bot):
        super().__init__(bot)
        self.player = SoundPlayer(ENV["DEVICE_NAME"])
        self.AllMsg = []
        print("setting load")
        
    class ModalClass(discord.ui.Modal, title = "設定名稱"):
        name = discord.ui.TextInput(label = "BotName",default = ENV["BOT_NAME"])
        MainRoomCodde = discord.ui.TextInput(label = "MainRoomCodde",default = ENV["MainRoomCodde"])
        iddd = discord.ui.TextInput(label = "Channel-ID",default = ENV["MAIN_CHANNEL_ID"])
        devicename = discord.ui.TextInput(label = "devicename-s",default = ENV["DEVICE_NAME"])
        async def on_submit(self, interaction: discord.Interaction):
            await interaction.response.send_message(f"ok!")
            update_env_variable("BOT_NAME",self.name.value)
            update_env_variable("MAIN_CHANNEL_ID",self.iddd.value)
            update_env_variable("DEVICE_NAME",self.devicename.value)
            update_env_variable("MainRoomCodde",self.MainRoomCodde.value)
            self.bot.dispatch("ENV_update")
            
                
    @app_commands.command(name = "setting", description = "設定")
    async def setting(self,interaction: discord.Interaction):  
        await interaction.response.send_modal(self.ModalClass())
        
async def setup(bot):
    await bot.add_cog(setting(bot))