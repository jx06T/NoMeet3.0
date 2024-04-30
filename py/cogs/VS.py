# from rich import print
import discord
from discord import app_commands
from discord.ext import commands
from _cog_class import cog_class
from typing import Literal,Optional
from Genv import ENV 
import requests
from gtts import gTTS
import re
import math
import time
from moviepy.editor import AudioFileClip
import os

class player():
    def __init__(self,v):
        self.v = v
        self.isplaying = False
        self.now = None
        self.sound = False
        self.audience = "_"

class msgM(cog_class):
    def __init__(self, bot):
        super().__init__(bot)
        self.AllMsg = []
        self.Lastfiles = ["",""]
        self.playerS = player("S")
        self.playerV = player("V")
        
    def list_files(self,directory):
        files = []
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                files.append(file)
        return files

    def convert_mp4_to_wav(self,mp4_file, wav_file):
        video_clip = AudioFileClip(mp4_file)
        video_clip.write_audiofile(wav_file)

    def download_file(self,url, save_path):
        try:
            response = requests.get(url)
        except:
            print("url錯誤",url)
            return False
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
                print("文件下载成功！")
            return True
        else:
            print("下载失败，HTTP 状态码:", response.status_code)
            return False

    def get_view_forPlay(self,player):
        v = player.v
        t = player.isplaying
        now = player.now
        file_name = os.path.basename(now)
        audience = player.audience
        print(v,t,now,audience)
        view = discord.ui.View()
        view.add_item(
            discord.ui.Button(
                label="▷" if not t else "▢",
                style=discord.ButtonStyle.blurple,
                custom_id="Mpause"+v
            )
        )
        view.add_item(
            discord.ui.Button(
                label="Finish"+v,
                style=discord.ButtonStyle.blurple,
                custom_id="Mfinish"+v
            )
        )
        directory  = r'py\video' if v=="V" else r'py\sound'
        view.add_item(
            discord.ui.Select(custom_id="Mmedia"+v, placeholder=file_name, options=
                [discord.SelectOption(label=D) for D in self.list_files(directory)]
            )
        )
        view.add_item(
            discord.ui.Select(custom_id="asnkjawn", placeholder=audience, options=
                [discord.SelectOption(label=audience)]
            )
        )
        return view    
    '''
    @app_commands.command(name="sound_me", description="說話")
    @discord.app_commands.describe(audio_file=':')
    @discord.app_commands.describe(link=':')
    @discord.app_commands.describe(audio_text=':')
    @discord.app_commands.describe(audience=':')
    @discord.app_commands.describe(force=':')
    async def CMsound(self,interaction: discord.Interaction,audio_file: discord.Attachment= None, link:str = "$",audio_text:str ="",audience:str="",force:Literal['T', 'F'] = "F"):
        ok = True
        if audio_text:
            tts = gTTS(audio_text, lang='zh-tw')
            filename = "tts"+str(math.floor(time.time()*10))[8:]+".mp3"
            tts.save(ENV["SCRIPT_DIRECTORY"]+"\\sound\\"+filename)

        elif audio_file:
            filename = audio_file.filename
            with open(ENV["SCRIPT_DIRECTORY"]+"\\sound\\"+filename, "wb") as f:
                await audio_file.save(f)
        else:
            if link == "$":
                link = self.Lastfiles[-1]
            filename = "jxeeee"+str(math.floor(time.time()*10))[8:]+".wav"
            ok = self.download_file(link, ENV["SCRIPT_DIRECTORY"]+"\\sound\\"+filename)
            if not ok:
                filename = "蝦.txt"
                if not link == "$"and not link == "":
                    filename = link
                    ok = check_file_in_folder(ENV["SCRIPT_DIRECTORY"]+"\\sound", filename)

        self.playerS.isplaying = ok
        self.playerS.now = filename
        view = self.get_view_forPlay(self.playerS)
        await interaction.response.send_message(content=filename, view=view)
        self.AllMsg.append({"type":"InsertSound" ,"FUN":"OPsound","from":interaction.user.name, "audience":audience, "file": filename, "force": force})
        self.bot.dispatch("msg_updated", self.AllMsg)
    '''
    @app_commands.command(name="video_me", description="鏡頭")
    @discord.app_commands.describe(video_file=':')
    @discord.app_commands.describe(link=':')
    @discord.app_commands.describe(sound=':')
    @discord.app_commands.describe(audience=':')
    @discord.app_commands.describe(force=':')
    async def CMvideo(self,interaction: discord.Interaction,video_file: discord.Attachment= None,link:str = "$",sound:Literal['T', 'F'] = "F",audience:str="",force:Literal['T', 'F'] = "F"):
        ok = True
        if video_file:
            filename = video_file.filename
            with open(ENV["SCRIPT_DIRECTORY"]+"\\video\\"+filename, "wb") as f:
                await video_file.save(f)
        else:
            if link == "$":
                link = self.Lastfiles[-1]
            filename = "jxeeee"+str(math.floor(time.time()*10))[8:]+".mp4"
            filename_match = re.search(r'/([^/]+(\.mp4|\.mov|\.mp3|\.jpg|\.png|\.jpeg|\.avi|\.mkv))\?', link)
            if filename_match:
                filename = filename_match.group(1)
            else:
                pass
            ok = self.download_file(link, ENV["SCRIPT_DIRECTORY"]+"\\video\\"+filename)
            if not ok:
                filename = "蝦.txt"
                if not link == "$" and not link == "":
                    filename = link
                    ok = check_file_in_folder(ENV["SCRIPT_DIRECTORY"]+"\\video", filename)

        self.playerV.isplaying = ok
        self.playerV.now = filename
        view = self.get_view_forPlay(self.playerV)
        await interaction.response.send_message(content=filename, view=view)
        self.AllMsg.append({"type":"InsertVideo","FUN":"OPvideo", "from":interaction.user.name, "audience":audience,"file": filename, "force": force})

        '''
        if sound == 'T':
            self.AllMsg.append({"type":"InsertSound", "FUN":"OPsound","from":interaction.user.name, "audience":audience,"file": filename, "force": force})
            if ok:
                filename2 = os.path.splitext(filename)[0]+".wav"
                self.convert_mp4_to_wav(ENV["SCRIPT_DIRECTORY"]+"\\video\\"+filename, ENV["SCRIPT_DIRECTORY"]+"\\sound\\"+filename2)
        '''

        self.bot.dispatch("msg_updated", self.AllMsg)
        
    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        IDD = interaction.data.get("custom_id") 
        '''
        if IDD == "MpauseS":
            self.playerS.isplaying = not self.playerS.isplaying
            await interaction.response.edit_message(view=self.get_view_forPlay(self.playerS))
            self.AllMsg.append({"type":"InsertSound", "FUN":"PPsound","from":interaction.user.name, "audience":self.playerS.isplaying})
            self.bot.dispatch("msg_updated", self.AllMsg)
            
        elif IDD=="MfinishS":
            self.playerS.isplaying = False
            await interaction.response.edit_message(content=interaction.message.content+"X")
            self.AllMsg.append({"type":"InsertSound", "FUN":"CLsound","from":interaction.user.name, "audience":self.playerS.audience})
            self.bot.dispatch("msg_updated", self.AllMsg)

        elif IDD == "MmediaS":
            ff = interaction.data.get("values")[0]
            self.playerS.now = ff
            await interaction.response.edit_message(content=ff,view=self.get_view_forPlay(self.playerS))
            self.AllMsg.append({"type":"InsertSound", "FUN":"OPsound","from":interaction.user.name, "audience":self.playerS.audience})
            self.bot.dispatch("msg_updated", self.AllMsg)
        '''
        if IDD == "MpauseV":
            self.playerV.isplaying = not self.playerV.isplaying
            await interaction.response.edit_message(view=self.get_view_forPlay(self.playerV))
            self.AllMsg.append({"type":"InsertVideo", "FUN":"PPvideo","from":interaction.user.name, "audience":self.playerV.audience,"file":self.playerV.isplaying})
            self.bot.dispatch("msg_updated", self.AllMsg)

        elif IDD=="MfinishV":
            self.playerV.isplaying = False
            await interaction.response.edit_message(content=interaction.message.content+"X")
            self.AllMsg.append({"type":"InsertVideo", "FUN":"CLvideo","from":interaction.user.name, "audience":self.playerV.audience,"file":self.playerV.now})
            self.bot.dispatch("msg_updated", self.AllMsg)
            
        elif IDD == "MmediaV":
            ff = interaction.data.get("values")[0]
            self.playerV.now = ff
            self.playerV.isplaying = True
            await interaction.response.edit_message(content=ff,view=self.get_view_forPlay(self.playerV))
            self.AllMsg.append({"type":"InsertVideo", "FUN":"OPvideo","from":interaction.user.name, "audience":self.playerV.audience,"file":self.playerV.now})
            self.bot.dispatch("msg_updated", self.AllMsg)

    @commands.Cog.listener()
    async def on_ENV_update(self,env):
        ENV = env
        print("envvv",ENV)
        
    @commands.Cog.listener()
    async def on_lastfiles_update(self,Lastfiles):
        self.Lastfiles = Lastfiles.copy()
        print("Lastfiles",Lastfiles)
  
def check_file_in_folder(folder_path, file_name):
    file_path = os.path.join(folder_path, file_name)
    if os.path.exists(file_path):
        print(f"File '{file_name}' exists in folder '{folder_path}'.")
        return True
    else:
        print(f"File '{file_name}' does not exist in folder '{folder_path}'.")
        return False

async def setup(bot):
    await bot.add_cog(msgM(bot))
