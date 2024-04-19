import discord
from discord import app_commands
from discord.ext import commands
from _cog_class import cog_class
from typing import Literal,Optional
from sound import SoundPlayer
from env import ENV 
class msg(cog_class):
    def __init__(self, bot):
        super().__init__(bot)
        self.player = SoundPlayer(ENV["DEVICE_NAME"])
        self.AllMsg = []
        print("msg load")
        
    def get_view_forPlay(self,t):
        view = discord.ui.View()
        view.add_item(
            discord.ui.Button(
                label="▷" if not t else "▢",
                style=discord.ButtonStyle.blurple,
                custom_id="pause"
            )
        )
        return view    

    @app_commands.command(name="sound", description="說話")
    @discord.app_commands.describe(audio_file=':')
    @discord.app_commands.describe(force=':')
    async def Csound(self,interaction: discord.Interaction,audio_file: discord.Attachment,force:Literal['T', 'F'] = "F"):
        view = self.get_view_forPlay(False)
        await interaction.response.send_message(content=audio_file.filename, view=view)
        # 將音訊檔案存入本地
        if audio_file:
            with open(ENV["SCRIPT_DIRECTORY"]+"\\sound\\"+audio_file.filename, "wb") as f:
                await audio_file.save(f)

        self.AllMsg.append({"type": "sound", "from":interaction.user.name, "file": audio_file.filename, "force": force})
        self.bot.dispatch("msg_updated", self.AllMsg)

        self.player.change_file(ENV["SCRIPT_DIRECTORY"]+"\\sound\\"+audio_file.filename)
        self.player.play()
        self.player.pause()

    @app_commands.command(name = "msg", description = "發訊息")
    @discord.app_commands.describe(msg=':')
    @discord.app_commands.describe(force=':')
    @discord.app_commands.describe(hide=':')
    async def Cmsg(self,interaction: discord.Interaction,msg:str,force:Literal['T', 'F'] = "F",hide:Literal['T', 'F'] = "T"):  
        await interaction.response.send_message("ok")
        self.AllMsg.append({"type":"Cmsg","from":interaction.user.name,"msg":msg,"force":force,"hide":hide})
        self.bot.dispatch("msg_updated", self.AllMsg)

    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        if interaction.data.get("custom_id") == "pause":
            if self.player.is_playing:
                self.player.pause()
            else:
                self.player.unpause()
            await interaction.response.edit_message(view=self.get_view_forPlay(self.player.is_playing))
        
    @commands.Cog.listener()
    async def on_ENV_update(self,env):
        ENV = env
        self.player.change_devicename(ENV["DEVICE_NAME"])
        print("envvv")

async def setup(bot):
    await bot.add_cog(msg(bot))