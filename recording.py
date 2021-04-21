import cv2
import sys
import os

STD_DIMENSIONS = {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4K": (3840, 2160)
}

VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID')
}

def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
        return VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']

def change_res(cap, width, height):
     cap.set(3,width)
     cap.set(4,height)

def get_dims(cap, res='1080p'):
    width, height = STD_DIMENSIONS['480p']
    if res in STD_DIMENSIONS:
        width, height = STD_DIMENSIONS[res]
    change_res(cap, width, height)
    return width, height

if len(sys.argv) < 2:
    print("need a filename!")
    exit()

filename = str(sys.argv[1]) 
my_res = '1080p'

cap = cv2.VideoCapture(0)
dim = get_dims(cap, res=my_res)
video_type_cv2 = get_video_type(filename)
fps = cap.get(cv2.CAP_PROP_FPS)

filename = f'{filename}_{fps}_{dim}.avi'

out = cv2.VideoWriter(filename, video_type_cv2, fps, dim)

while(1):
    ret, frame = cap.read()
    out.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
