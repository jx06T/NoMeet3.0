import pygame
import time
from pydub import AudioSegment
class SoundPlayer:
    def __init__(self, devicename = None):
        self.file_path0 = None
        self.audience = "else"
        self.VStype = "S"
        self.is_playing = False

        self.file_path = None
        self.devicename = devicename
        self.R = ''

        try:
            pygame.mixer.init(devicename=self.devicename)
            self.R = "ok"
        except:
            pygame.mixer.init()
            self.R = "No such device"
            self.devicename = None

        self.channel = pygame.mixer.Channel(0)

    def play(self):
        if not self.is_playing:
            self.channel.play(self.sound, loops=-1)
            self.is_playing = True

    def pause(self):
        if self.is_playing:
            self.channel.pause()
            self.is_playing = False

    def unpause(self):
        if not self.is_playing:
            self.channel.unpause()
            self.is_playing = True

    def stop(self):
        self.channel.stop()
        self.is_playing = False
        pygame.mixer.quit()
        del self

    def change_file(self, new_file):
        self.stop()
        self.file_path = new_file
        self.file_path0 = new_file
        pygame.mixer.init(devicename=self.devicename)
        self.sound = pygame.mixer.Sound(self.file_path)
    def change_devicename(self, new_devicename):
        self.stop()
        temp = self.devicename
        self.devicename = new_devicename
        try:
            pygame.mixer.init(devicename=self.devicename)
            self.R = "ok"
        except:
            self.devicename = temp
            pygame.mixer.init(devicename=self.devicename)
                

if __name__=='__main__':
    # 使用範例
    # player = SoundPlayer()
    player = SoundPlayer(devicename='Line 1 (Virtual Audio Cable)')

    player.change_file(r"D:\Document_J\code\NoMeet\py\sound\15_12_HDRyan_B_AY_Ryan_B_AY_Yang_Lao_San_Never_again.wav")
    player.play()  # 播放音訊檔
    time.sleep(3)
    # 暫停播放
    player.pause()
    time.sleep(1)

    # 恢復播放
    player.unpause()
    time.sleep(3)

    # 更換音訊檔案
    player.change_file(r"D:\Music_J\testsound\15nothing 12  HDRyan B  AY楊佬叁   再也沒有 歌詞字幕完整高清音質 Ryan B  AY Yang Lao San    Never again.wav")
    player.play()  # 播放新的音訊檔案
    time.sleep(5)

    # 停止播放並銷毀實例
    player.stop()