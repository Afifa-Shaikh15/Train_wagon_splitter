import cv2
import os
from utils import coach_frame_name

def extract_frames(video_path, train_number, coach_idx, folder, rate=1):
    cap = cv2.VideoCapture(video_path)
    frames = []
    frame_no = 0
    saved_no = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_no % rate == 0:
            fname = coach_frame_name(train_number, coach_idx, saved_no)
            out_path = os.path.join(folder, fname)
            cv2.imwrite(out_path, frame)
            frames.append(out_path)
            saved_no += 1
        frame_no += 1
    cap.release()
    return frames
