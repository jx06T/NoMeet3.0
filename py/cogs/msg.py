import discord
from discord import app_commands
from discord.ext import commands
from _cog_class import cog_class
from typing import Literal,Optional
from sound import SoundPlayer
from video import VideoPlayer
from Genv import ENV 
import requests
from gtts import gTTS
import re
import math
import time
class msg(cog_class):
    def __init__(self, bot):
        super().__init__(bot)
        self.player = SoundPlayer(ENV["DEVICE_NAME_S"])
        self.playerV = VideoPlayer(width=1280, height=720,device=ENV["DEVICE_NAME_V"])
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

    def get_view_forPlay(self,t,v):
        view = discord.ui.View()
        view.add_item(
            discord.ui.Button(
                label="▷" if not t else "▢",
                style=discord.ButtonStyle.blurple,
                custom_id="pause"+v
            )
        )
        view.add_item(
            discord.ui.Button(
                label="Finish"+v,
                style=discord.ButtonStyle.blurple,
                custom_id="finish"+v
            )
        )
        return view    

    @app_commands.command(name="sound", description="說話")
    @discord.app_commands.describe(audio_file=':')
    @discord.app_commands.describe(audio_text=':')
    @discord.app_commands.describe(force=':')
    async def Csound(self,interaction: discord.Interaction,audio_file: discord.Attachment= None, audio_text:str ="",force:Literal['T', 'F'] = "F"):
        view = self.get_view_forPlay(False,"S")
        if audio_text:
            tts = gTTS(audio_text, lang='zh-tw')
            filename = "tts"+str(math.floor(time.time()*10))[8:]+".mp3"
            tts.save(ENV["SCRIPT_DIRECTORY"]+"\\sound\\"+filename)

        elif audio_file:
            filename = audio_file.filename
            with open(ENV["SCRIPT_DIRECTORY"]+"\\sound\\"+filename, "wb") as f:
                await audio_file.save(f)
        else:
            filename = "jxeeee"+str(math.floor(time.time()*10))[8:]+".wav"
            self.download_file(self.Lastfiles[-1], ENV["SCRIPT_DIRECTORY"]+"\\sound\\"+filename)
            
        await interaction.response.send_message(content=filename+"\n"+self.player.R, view=view)
        self.AllMsg.append({"type": "sound", "from":interaction.user.name, "file": filename, "force": force,"name":ENV["DEVICE_NAME_S"]})
        self.bot.dispatch("msg_updated", self.AllMsg)

        self.player.change_file(ENV["SCRIPT_DIRECTORY"]+"\\sound\\"+filename)
        self.player.play()
        self.player.pause()

    @app_commands.command(name="video", description="鏡頭")
    @discord.app_commands.describe(video_file=':')
    @discord.app_commands.describe(force=':')
    async def Cvideo(self,interaction: discord.Interaction,video_file: discord.Attachment= None,force:Literal['T', 'F'] = "F"):
        view = self.get_view_forPlay(False,"V")
        if video_file:
            filename = video_file.filename
            with open(ENV["SCRIPT_DIRECTORY"]+"\\video\\"+filename, "wb") as f:
                await video_file.save(f)
        else:
            filename = "jxeeee"+str(math.floor(time.time()*10))[8:]+".mp4"
            filename_match = re.search(r'/([^/]+(\.mp4|\.mov|\.mp3|\.avi|\.mkv))\?', self.Lastfiles[-1])
            if filename_match:
                filename = filename_match.group(1)
            else:
                return
            self.download_file(self.Lastfiles[-1], ENV["SCRIPT_DIRECTORY"]+"\\video\\"+filename)
            print(filename)
            
        await interaction.response.send_message(content=filename, view=view)
        self.playerV.change_file(ENV["SCRIPT_DIRECTORY"]+"\\video\\"+filename)
        self.playerV.start_virtual_camera()

        self.AllMsg.append({"type": "video", "from":interaction.user.name, "file": filename, "force": force,"name":ENV["DEVICE_NAME_V"]})
        self.bot.dispatch("msg_updated", self.AllMsg)
        

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
        if interaction.data.get("custom_id") == "pauseS":
            if self.player.is_playing:
                self.player.pause()
            else:
                self.player.unpause()
                self.AllMsg.append({"type": "sound", "from":interaction.user.name,"name":ENV["DEVICE_NAME_S"]})
                self.bot.dispatch("msg_updated", self.AllMsg)

            await interaction.response.edit_message(view=self.get_view_forPlay(self.player.is_playing,"S"))
            
        elif interaction.data.get("custom_id")=="finishS":
            self.AllMsg.append({"type":"FUN","FUN":"closeMic","from":interaction.user.name})
            self.bot.dispatch("msg_updated", self.AllMsg)
            await interaction.response.edit_message(content="X")

        elif interaction.data.get("custom_id") == "pauseV":
            if not self.playerV.paused:
                self.playerV.pause()
            else:
                self.playerV.resume()
                self.AllMsg.append({"type": "video", "from":interaction.user.name,"name":ENV["DEVICE_NAME_V"]})
                self.bot.dispatch
            await interaction.response.edit_message(view=self.get_view_forPlay(not self.playerV.paused,"V"))

        elif interaction.data.get("custom_id")=="finishV":
            self.AllMsg.append({"type":"FUN","FUN":"closeCam","from":interaction.user.name})
            self.bot.dispatch("msg_updated", self.AllMsg)
            # self.playerV.done()
            await interaction.response.edit_message(content="X")

        
    @commands.Cog.listener()
    async def on_ENV_update(self,env):
        ENV = env
        self.player.change_devicename(ENV["DEVICE_NAME_S"])
        print("envvv",ENV)
        
    @commands.Cog.listener()
    async def on_lastfiles_update(self,Lastfiles):
        self.Lastfiles = Lastfiles.copy()
        print("Lastfiles",Lastfiles)

    @commands.Cog.listener()
    async def on_device_update(self,d):
        time.sleep(0.2)
        del self.playerV
        self.playerV = VideoPlayer(width=1280, height=720,device=ENV["DEVICE_NAME_V"])
    

async def setup(bot):
    await bot.add_cog(msg(bot))