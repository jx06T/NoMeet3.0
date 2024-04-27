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
from moviepy.editor import AudioFileClip
import os
class msg(cog_class):
    def __init__(self, bot):
        super().__init__(bot)
        self.playerS = SoundPlayer(ENV["DEVICE_NAME_S"])
        self.playerV = VideoPlayer(width=1280, height=720,device=ENV["DEVICE_NAME_V"])
        self.playerV.change_file(ENV["SCRIPT_DIRECTORY"]+"\\black.jpg")
        self.playerV.start_virtual_camera()
        self.AllMsg = []
        self.Lastfiles = ["",""]
        print("msg load",self.playerS.R)
        
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

    def get_view_forPlay(self,t,v,now):
        file_name = os.path.basename(now)
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
        directory  = r'py\video' if v=="V" else r'py\sound'
        view.add_item(
            discord.ui.Select(custom_id="media"+v, placeholder=file_name, options=
                [discord.SelectOption(label=D) for D in self.list_files(directory)]
            )
        )
        return view    

    @app_commands.command(name="sound", description="說話")
    @discord.app_commands.describe(audio_file=':')
    @discord.app_commands.describe(audio_text=':')
    @discord.app_commands.describe(audience=':')
    @discord.app_commands.describe(force=':')
    async def Csound(self,interaction: discord.Interaction,audio_file: discord.Attachment= None, audio_text:str ="",audience:Literal['else', 'me','both'] = "else",force:Literal['T', 'F'] = "F"):
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
            filename = "jxeeee"+str(math.floor(time.time()*10))[8:]+".wav"
            ok = self.download_file(self.Lastfiles[-1], ENV["SCRIPT_DIRECTORY"]+"\\sound\\"+filename)
            if not ok:
                filename = "蝦.txt"

        view = self.get_view_forPlay(False,"S",filename)
        await interaction.response.send_message(content=filename+"\n"+self.playerS.R, view=view)

        self.AllMsg.append({"type":"SV","FUN": "openMic", "from":interaction.user.name, "audience":audience, "file": filename, "force": force,"name":ENV["DEVICE_NAME_S"]})
        self.bot.dispatch("msg_updated", self.AllMsg)

        if ok:
            self.playerS.change_file(ENV["SCRIPT_DIRECTORY"]+"\\sound\\"+filename)
            self.playerS.play()
            self.playerS.pause()

    @app_commands.command(name="video", description="鏡頭")
    @discord.app_commands.describe(video_file=':')
    @discord.app_commands.describe(sound=':')
    @discord.app_commands.describe(audience=':')
    @discord.app_commands.describe(force=':')
    async def Cvideo(self,interaction: discord.Interaction,video_file: discord.Attachment= None,sound:Literal['T', 'F'] = "F",audience:Literal['else', 'me','both'] = "else",force:Literal['T', 'F'] = "F"):
        ok = True
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
                pass
            ok = self.download_file(self.Lastfiles[-1], ENV["SCRIPT_DIRECTORY"]+"\\video\\"+filename)
            if not ok:
                filename = "蝦.txt"
                
        view = self.get_view_forPlay(ok,"V",filename)
        await interaction.response.send_message(content=filename, view=view)
        
        if ok:
            self.playerV.change_file(ENV["SCRIPT_DIRECTORY"]+"\\video\\"+filename)
            # self.playerV.start_virtual_camera()
            
        self.playerV.sound = False
        self.AllMsg.append({"type":"SV","FUN": "openCam", "from":interaction.user.name, "audience":audience,"file": filename, "force": force,"name":ENV["DEVICE_NAME_V"]})
        if sound == 'T':
            if ok:
                filename2 = os.path.splitext(filename)[0]+".wav"
                print(filename2)
                self.convert_mp4_to_wav(ENV["SCRIPT_DIRECTORY"]+"\\video\\"+filename, ENV["SCRIPT_DIRECTORY"]+"\\sound\\"+filename2)
                self.AllMsg.append({"type":"SV","FUN": "openMic", "from":interaction.user.name, "audience":audience,"file": filename, "force": force,"name":ENV["DEVICE_NAME_S"]})
                # self.AllMsg.append({"type": "sound", "from":interaction.user.name, "file": filename2, "force": force,"name":ENV["DEVICE_NAME_S"]})

                self.playerS.change_file(ENV["SCRIPT_DIRECTORY"]+"\\sound\\"+filename2)
                self.playerS.play()
            self.playerV.sound = True

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
        IDD = interaction.data.get("custom_id") 
        if IDD == "pauseS":
            if self.playerS.is_playing:
                self.playerS.pause()
            else:
                self.playerS.unpause()
                self.AllMsg.append({"type": "sound", "from":interaction.user.name,"name":ENV["DEVICE_NAME_S"]})
                self.bot.dispatch("msg_updated", self.AllMsg)

            await interaction.response.edit_message(view=self.get_view_forPlay(self.playerS.is_playing,"S",self.playerS.file_path))
            
        elif IDD=="finishS":
            self.AllMsg.append({"type":"FUN","FUN":"closeMic","from":interaction.user.name})
            self.bot.dispatch("msg_updated", self.AllMsg)
            self.playerS.pause()
            await interaction.response.edit_message(content=interaction.message.content+"X")

        elif IDD == "pauseV":
            if not self.playerV.paused:
                self.playerV.pause()
                if self.playerV.sound:
                    self.playerS.pause()
            else:
                self.playerV.resume()
                self.AllMsg.append({"type": "video", "from":interaction.user.name,"name":ENV["DEVICE_NAME_V"]})
                if self.playerV.sound:
                    self.playerS.unpause()
                    self.AllMsg.append({"type": "sound", "from":interaction.user.name,"name":ENV["DEVICE_NAME_S"]})

                self.bot.dispatch("msg_updated", self.AllMsg)
                
            await interaction.response.edit_message(view=self.get_view_forPlay(not self.playerV.paused,"V",self.playerV.file_path))

        elif IDD=="finishV":
            self.bot.dispatch("msg_updated", self.AllMsg)
            # self.playerV.done()
            if self.playerV.sound:
                self.bot.dispatch("msg_updated", self.AllMsg)
                self.AllMsg.append({"type":"FUN","FUN":"closeAll","from":interaction.user.name})
                self.playerS.pause()
            else:
                self.AllMsg.append({"type":"FUN","FUN":"closeCam","from":interaction.user.name})
            await interaction.response.edit_message(content=interaction.message.content+"X")
            
        elif IDD == "mediaS":
            ff = interaction.data.get("values")[0]
            self.playerS.change_file(ENV["SCRIPT_DIRECTORY"]+"\\sound\\"+ff)
            self.playerS.play()
            await interaction.response.edit_message(content=ff,view=self.get_view_forPlay(not self.playerS.is_playing,"S",ff))
        elif IDD == "mediaV":
            ff = interaction.data.get("values")[0]
            print("ff",ff)
            self.playerV.change_file(ENV["SCRIPT_DIRECTORY"]+"\\video\\"+ff)
            # self.playerV.start_virtual_camera()
            await interaction.response.edit_message(content=ff,view=self.get_view_forPlay(not self.playerV.paused,"V",ff))
            self.AllMsg.append({"type": "video", "from":interaction.user.name,"name":ENV["DEVICE_NAME_V"]})

            if self.playerV.sound:
                filename2 = os.path.splitext(ff)[0]+".wav"
                print(filename2)
                self.convert_mp4_to_wav(ENV["SCRIPT_DIRECTORY"]+"\\video\\"+ff, ENV["SCRIPT_DIRECTORY"]+"\\sound\\"+filename2)
                self.playerS.change_file(ENV["SCRIPT_DIRECTORY"]+"\\sound\\"+filename2)
                self.playerS.play()
                self.playerS.unpause()
                self.AllMsg.append({"type": "sound", "from":interaction.user.name,"name":ENV["DEVICE_NAME_S"]})

            self.bot.dispatch("msg_updated", self.AllMsg)
                


    @commands.Cog.listener()
    async def on_ENV_update(self,env):
        ENV = env
        self.playerS.change_devicename(ENV["DEVICE_NAME_S"])
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
    
    # def unload(self):
    #     self.playerV.release_camera()

async def setup(bot):
    await bot.add_cog(msg(bot))