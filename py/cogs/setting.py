import discord
from discord import app_commands
from discord.ext import commands
from discord.utils import MISSING
from _cog_class import cog_class
from typing import Literal,Optional
from sound import SoundPlayer
from Genv import ENV,update_env_variable

class setting(cog_class):
    def __init__(self, bot):
        super().__init__(bot)
        self.player = SoundPlayer(ENV["DEVICE_NAME"])
        self.AllMsg = []
        print("setting load")
        
    class ModalClass(discord.ui.Modal, title = "設定"):
        def __init__(self,bot):
            super().__init__()
            self.bot = bot

            self.add_item(discord.ui.TextInput(custom_id ="BOT_NAME",label = "BotName",default = ENV["BOT_NAME"]))
            self.add_item(discord.ui.TextInput(custom_id = "MAIN_CHANNEL_ID",label = "Channel-ID",default = ENV["MAIN_CHANNEL_ID"]))
            self.add_item(discord.ui.TextInput(custom_id="DEVICE_NAME",label = "devicename-s",default = ENV["DEVICE_NAME"]))
        # MainRoomCodde = discord.ui.TextInput(label = "MainRoomCodde",default = ENV["MainRoomCodde"])
        async def on_submit(self, interaction: discord.Interaction):
            for item in self.children:
                R = update_env_variable(item.custom_id,item.value)
            await interaction.response.send_message(f"ok!")
            self.bot.dispatch("ENV_update",R)
            
    @app_commands.command(name = "setting", description = "設定")
    async def setting(self,interaction: discord.Interaction):  
        await interaction.response.send_modal(self.ModalClass(self.bot))
        
   
async def setup(bot):
    await bot.add_cog(setting(bot))