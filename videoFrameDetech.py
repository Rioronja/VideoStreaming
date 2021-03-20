import cv2 
import time
import numpy as np
import os
import matplotlib.pyplot as plt

path = os.getcwd()
videos = [i for i in os.listdir('DroneVideoDataset')]
for video in videos:
    if(video.find('.mp4') > 0):
        videoPath = os.path.join(path, 'DroneVideoDataset', f'{video.strip(".mp4")}')
        if os.path.exists(videoPath):
            continue
        os.mkdir(videoPath)
        cap = cv2.VideoCapture('./DroneVideoDataset/' + video)
        cnt = 0
        if(cap.isOpened()):
            while(1):
                ret, frame = cap.read()
                if ret:
                    cv2.imwrite(f'{videoPath}/frame{str(cnt).zfill(4)}.jpg', frame)
                    cnt += 1
                else:
                    break


            
            