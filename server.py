import cv2 
import time
import image_similarity_measures.quality_metrics  as q
import numpy as np
import tensorflow as tf

def ssim(img1, img2):
    ssim1 = tf.image.ssim(img1, img2, max_val=255, filter_size=11,
                    filter_sigma=1.5, k1=0.01, k2=0.03).
    return ssim1

cam = cv2.VideoCapture(0)#, cv2.CAP_V4L2)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
cam.set(cv2.CAP_PROP_FPS, 60)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cnt = 0
timeThen = time.time()
serialCnt = 0 
global lastframe 
ret, lastframe = cam.read()
while True:
    ret, frame = cam.read()
    print(ssim(frame, lastframe))
    # print(time.time() - timeNow)
    cv2.imshow('frame', frame)
    cnt = cnt + 1
    timeNow = time.time()
    if(timeNow - timeThen) > 1:
        print("FPS: ",cnt)
        timeThen = timeNow
        cnt = 0
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    lastframe = frame

    