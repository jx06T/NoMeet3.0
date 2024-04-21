import pyvirtualcam
import cv2
import numpy as np
import time
import threading

class VideoPlayer:
    def __init__(self):
        
        self.paused = False
        self.playback_thread = None

    def change_file(self,video_path):
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        if self.fps == 0:
            self.fps = 30

    def start_virtual_camera(self):
        self.playback_thread = threading.Thread(target=self.play_video)
        self.playback_thread.start()

    def play_video(self):
        # try:
        with pyvirtualcam.Camera(width=self.width, height=self.height, fps=self.fps) as cam:
            print(f'使用虚拟相机: {cam.device}')
            print(f'视频分辨率: {self.video_path}  {self.width}x{self.height}, FPS: {self.fps}')
            if self.width == 0:
                return
            while True:
                if not self.paused:
                    ret, frame = self.cap.read()
                    if ret:
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        cam.send(frame)
                    else:
                        black_frame = np.zeros((self.height, self.width, 3), dtype=np.uint8)
                        cam.send(black_frame)
                    time.sleep(1 / self.fps)

                if cv2.waitKey(1) == ord('q'):
                    break
                if self.paused == "D":
                    break
        # except:
        #     print("5555555555555555555555")
                    
    def pause(self):
        self.paused = True

    def resume(self):
        print("sssssssss")
        self.paused = False

    def done(self):
        self.paused = "D"

if __name__ == '__main__':
    video_player = VideoPlayer()
    video_player.change_file(r"py\video\IMG_7167.mov")
    video_player.start_virtual_camera()

    print(664)
    time.sleep(3)
    video_player.pause()
    time.sleep(3)
    video_player.resume()

    time.sleep(60)
    video_player.done()
    # 其他代码可以在此处添加