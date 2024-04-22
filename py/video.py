import pyvirtualcam
import cv2
import numpy as np
import time
import threading

class VideoPlayer:
    def __init__(self, width=1920, height=1080,device="Unity Video Capture"):
        self.device = device
        self.paused = False
        self.playback_thread = None
        try:
            self.virtual_camera = pyvirtualcam.Camera(device = self.device,width=width, height=height, fps=30)
        except:
            self.virtual_camera = pyvirtualcam.Camera(width=width, height=height, fps=30)

        self.current_video_path = None

    def change_file(self, video_path):
        self.current_video_path = video_path
        self.cap = cv2.VideoCapture(video_path)
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        if self.fps == 0:
            self.fps = 30

    def start_virtual_camera(self):
        print(f'使用虚拟相机: {self.virtual_camera.device}')
        print(f'视频分辨率: {self.current_video_path} {self.virtual_camera.width}x{self.virtual_camera.height}, FPS: {self.fps}')
        self.playback_thread = threading.Thread(target=self.play_video)
        self.playback_thread.start()

    def play_video(self):
        while True:
            if not self.paused:
                ret, frame = self.cap.read()
                if ret:
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
                else:
                    black_frame = np.zeros((self.virtual_camera.height, self.virtual_camera.width, 3), dtype=np.uint8)
                    self.virtual_camera.send(black_frame)
                    self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Loop back to the start of the video

            time.sleep(1 / self.fps-0.008)

            # if cv2.waitKey(1) == ord('q'):
            #     break

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

if __name__ == '__main__':
    video_player = VideoPlayer(width=1280, height=720)  # 設置初始虛擬攝像頭分辨率
    video_player.change_file(r"py\video\IMG_7167.mov")
    video_player.start_virtual_camera()

    # time.sleep(3)
    # video_player.pause()
    # time.sleep(3)
    # video_player.resume()
    time.sleep(3)

    video_player.change_file(r"py\video\wdwf.mp4")
    time.sleep(60)

    # 保持虛擬攝像頭運行
    while True:
        pass