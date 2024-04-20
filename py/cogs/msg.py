import discord
from discord import app_commands
from discord.ext import commands
from _cog_class import cog_class
from typing import Literal,Optional
from sound import SoundPlayer
from Genv import ENV 
import requests
class msg(cog_class):
    def __init__(self, bot):
        super().__init__(bot)
        self.player = SoundPlayer(ENV["DEVICE_NAME"])
        self.AllMsg = []
        print("msg load",self.player.R)
        
    def download_file(self,url, save_path):
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
                print("文件下载成功！")
        else:
            print("下载失败，HTTP 状态码:", response.status_code)

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
    async def Csound(self,interaction: discord.Interaction,audio_file: discord.Attachment= None,force:Literal['T', 'F'] = "F"):
        view = self.get_view_forPlay(False)
        if audio_file:
            filename = audio_file.filename
            await interaction.response.send_message(content=filename+"\n"+self.player.R, view=view)
            with open(ENV["SCRIPT_DIRECTORY"]+"\\sound\\"+filename, "wb") as f:
                await audio_file.save(f)
        else:
            filename = "jxeeee.ogg"
            await interaction.response.send_message(content=filename+"\n"+self.player.R, view=view)
            self.download_file(self.Lastfiles[-1], ENV["SCRIPT_DIRECTORY"]+"\\sound\\"+filename)
            
        self.AllMsg.append({"type": "sound", "from":interaction.user.name, "file": filename, "force": force})
        self.bot.dispatch("msg_updated", self.AllMsg)

        self.player.change_file(ENV["SCRIPT_DIRECTORY"]+"\\sound\\"+filename)
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
        print("envvv",ENV)
        
    @commands.Cog.listener()
    async def on_lastfiles_update(self,Lastfiles):
        self.Lastfiles = Lastfiles.copy()
        print("Lastfiles",Lastfiles)

async def setup(bot):
    await bot.add_cog(msg(bot))