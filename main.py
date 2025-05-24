import cv2
import paho.mqtt.client as mqtt
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--emulation', action='store_true')
args = parser.parse_args()

client = mqtt.Client()
client.connect("localhost")

def process_frame(frame):
    # Логика обработки кадра
    pass

if args.emulation:
    # Генерация тестового изображения
    while True:
        frame = np.zeros((480,640,3), dtype=np.uint8)
        cv2.circle(frame, (320,240), 50, (0,0,255), -1)
        process_frame(frame)
else:
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            process_frame(frame)
