import pyvirtualcam
import cv2
import numpy as np
import time
import threading

class VideoPlayer:
    def __init__(self, width=1920, height=1080,device="Unity Video Capture"):
        self.device = device
        self.is_playing = True
        self.sound = False
        self.s = False
        self.VStype = "V"
        self.playback_thread = None
        self.audience = "else"

        try:
            self.virtual_camera = pyvirtualcam.Camera(device = self.device,width=width, height=height, fps=30)
        except:
            self.virtual_camera = pyvirtualcam.Camera(width=width, height=height, fps=30)

        self.file_path = None
        self.file_path0 = None

    def change_file(self, video_path):
        self.file_path = video_path
        self.file_path0 = video_path
        self.cap = cv2.VideoCapture(video_path)
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        if self.fps == 0:
            self.fps = 30
        print(f'视频分辨率: {self.file_path} , FPS: {self.fps}')

    def start_virtual_camera(self):
        if self.s:
            return
        print(f'使用虚拟相机: {self.virtual_camera.device}')
        print(f'视频分辨率: {self.file_path} {self.virtual_camera.width}x{self.virtual_camera.height}, FPS: {self.fps}')
        self.playback_thread = threading.Thread(target=self.play_video)
        self.playback_thread.start()
        self.s = True


    def play_video(self):
        last_frame = None
        while True:
            if self.is_playing:
                ret, frame = self.cap.read()
                if ret:
                    
                    last_frame = frame
                else:
                    frame = last_frame

                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                height, width = frame.shape[:2]
                scale = min(self.virtual_camera.width / width, self.virtual_camera.height / height)
                new_width = int(width * scale)
                new_height = int(height * scale)

                resized_frame = cv2.resize(frame, (new_width, new_height))

                canvas = np.zeros((self.virtual_camera.height, self.virtual_camera.width, 3), dtype=np.uint8)

                x = (self.virtual_camera.width - new_width) // 2
                y = (self.virtual_camera.height - new_height) // 2
                canvas[y:y+new_height, x:x+new_width] = resized_frame
                self.virtual_camera.send(canvas)

            time.sleep((1 / self.fps)*0.65)
            # time.sleep((1 / self.fps)-0.008)

            # if cv2.waitKey(1) == ord('q'):
            #     break

    def pause(self):
        self.is_playing = False

    def resume(self):
        self.is_playing = True

    def release_camera(self):
        if hasattr(self, 'cap'):
            self.cap.release()

if __name__ == '__main__':
    video_player = VideoPlayer(width=1280, height=720,device="OBS Virtual Camera")  # 設置初始虛擬攝像頭分辨率
    video_player.change_file(r"D:\Document_J\code\NoMeet\py\video\IMG_7174.JPG.mp4")
    video_player.start_virtual_camera()

    # time.sleep(3)
    # video_player.pause()
    # time.sleep(3)
    # video_player.resume()
    time.sleep(5)

    video_player.change_file(r"py\video\wdwf.mp4")
    # video_player.change_file(r"py\video\222.jpg")
    time.sleep(60)

    video_player.release_camera()
    print("d")
    # 保持虛擬攝像頭運行
    while True:
        pass