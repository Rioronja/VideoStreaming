import cv2 
import time
import image_similarity_measures.quality_metrics  as q
import numpy as np
import tensorflow as tf
import os
import matplotlib.pyplot as plt

def ssim(img1, img2):
    ssim1 = tf.image.ssim(img1, img2, max_val=255, filter_size=11,
                    filter_sigma=1.5, k1=0.01, k2=0.03)
    print(f'\rssim: {ssim1}', end='')
    return ssim1
videos = [i for i in os.listdir('DroneVideoDataset')]
for video in videos:
    if(video.find('.mp4') > 0):
        ssimValue = [] 
        cap = cv2.VideoCapture('./DroneVideoDataset/' + video)
        f = open(f'./DroneVideoDataset/{video.strip(".mp4")}_ssim.txt', 'w')
        if(cap.isOpened()):
            ret, frame = cap.read()
            lastframe = frame
            while(1):
                ret, frame = cap.read()
                if(ret):
                    s = ssim(lastframe, frame)
                    f.write(f'{s}\n')
                    ssimValue.append(s)
                    lastframe = frame
                else:
                    break
        x_axis = [i for i in range(0, len(ssimValue))]
        plt.plot(x_axis, ssimValue, 'r')
        plt.savefig(f'./DroneVideoDataset/{video.strip(".mp4")}_ssim.jpg')
        plt.close()
        f.close()
