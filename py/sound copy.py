import time
import pyglet

class SoundPlayer:
    def __init__(self, devicename=None):
        self.devicename = devicename
        self.player = None
        self.is_playing = False

    def play(self, file_path):
        self.player = pyglet.media.Player()
        if self.devicename:
            pyglet.options['audio'] = ('directsound', self.devicename)
        try:
            sound = pyglet.media.load(file_path)
            self.player.queue(sound)
            self.player.play()
            self.is_playing = True
        except pyglet.media.exceptions.MediaDecodeException:
            print(f"Error: Unable to decode media file '{file_path}'")

    def pause(self):
        if self.is_playing:
            self.player.pause()
            self.is_playing = False

    def unpause(self):
        if not self.is_playing:
            self.player.play()
            self.is_playing = True

    def stop(self):
        if self.player:
            self.player.pause()
            self.player.delete()
            self.is_playing = False

if __name__ == "__main__":
    # 使用範例
    player = SoundPlayer("Line 1 (Virtual Audio Cable)")
    player.play(r"D:\Document_J\code\NoMeet\py\sound\A84612B0B31C4AEECFAAD5DB6EEB2F35A61CAF1A.m4a")  # 播放音訊檔
    time.sleep(3)
    # 暫停播放
    player.pause()
    time.sleep(1)

    # 恢復播放
    player.unpause()
    time.sleep(3)

    # 更換音訊檔案
    player.play(r"D:\Music_J\testsound\15nothing 12  HDRyan B  AY楊佬叁   再也沒有 歌詞字幕完整高清音質 Ryan B  AY Yang Lao San    Never again.wav")  # 播放新的音訊檔案
    time.sleep(5)

    # 停止播放
    player.stop()
