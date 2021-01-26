import socket
import sys
import cv2
import pickle
import numpy as np
import struct ## new
import zlib
import time


def reply(frac, conn):
    rep = {}
    rep['time'] = frac['time']
    rep['result'] = "result"
    rep_data = pickle.dumps(rep, 0)
    rep_size = len(rep_data)
    conn.sendall(struct.pack(">L", rep_size) + rep_data)

HOST=''
PORT=9000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print('Socket created')

s.bind((HOST,PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')

conn,addr=s.accept()
data = b''
payload_size = struct.calcsize(">L")
cnt = 0
timeThen = time.time()
while True:
    while len(data) < payload_size:
        data += conn.recv(4096)
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack(">L", packed_msg_size)[0]
    while len(data) < msg_size:
        data += conn.recv(4096)
    frac_data = data[:msg_size]
    data = data[msg_size:]
    frac = pickle.loads(frac_data, fix_imports=True, encoding="bytes")
    frame = cv2.imdecode(frac["frame"], cv2.IMREAD_COLOR)
    cv2.imshow("frame", frame)
    cnt += 1
    timeNow = time.time()
    if timeNow - timeThen > 1:
        print("FPS: ", cnt)
        print(" Frame Size: ", msg_size)
        cnt = 0
        timeThen = time.time()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    reply(frac, conn)