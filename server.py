import cv2 
import time

  
# cam = cv2.VideoCapture(0 + cv2.CAP_V4L2)
# cam.open(0, apiPreference=cv2.CAP_V4L2)
cam = cv2.VideoCapture(0)#, cv2.CAP_V4L2)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
cam.set(cv2.CAP_PROP_FPS, 60)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cnt = 0
timeThen = time.time()
serialCnt = 0 
while True:
    ret, frame = cam.read()
    cv2.imshow('frame', frame)
    cnt = cnt + 1
    timeNow = time.time()
    if(timeNow - timeThen) > 1:
        print("FPS: ",cnt)
        timeThen = timeNow
        cnt = 0
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break