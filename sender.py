import cv2
import io
import socket
import struct
import time
import pickle
import zlib
import sys
import threading

def recv_print():
    data = b''
    payload_size = struct.calcsize(">l")
    while 1:
        while len(data) < payload_size:
            data += client_socket.recv(4096)
        payload = data[:payload_size]
        data = data[payload_size:]
        payload = struct.unpack(">L", payload)[0]
        while len(data) < payload:
            data += client_socket.recv(4096)
        frac = data[:payload]
        data = data[payload:]
        frac = pickle.loads(frac, fix_imports=True, encoding="bytes")
        rtt = time.time() - frac['time']
        print(rtt) #, frac['result'])
        

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.5.41', 9000))
added_thread = threading.Thread(target=recv_print)
added_thread.deamon = True
added_thread.start()
connection = client_socket.makefile('wb')
cam = cv2.VideoCapture(0)

# encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
serialNum = 0
cnt=0
timeThen = time.time()
while True:
    ret, frame = cam.read()
    ret, frame = cv2.imencode('.jpg', frame)
    frac = {}
    frac['frame'] = frame
    frac['serialNum'] = serialNum
    frac['time'] = time.time()
    data = pickle.dumps(frac, 0)
    size = len(data)
    client_socket.sendall(struct.pack(">L", size) + data)
    print(size)#, serialNum, frac)
    serialNum += 1
    f = cv2.imdecode(frac['frame'], cv2.IMREAD_COLOR)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cnt += 1
    timeNow = time.time()
    if timeNow - timeThen > 1:
        print("FPS: ", cnt)
        timeThen = time.time()
        cnt = 0
