import cv2
import os
from utils import ensure_dir, coach_folder, coach_video_name

def split_video(video_path, train_number, work_dir, min_coach_width_px=150):
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Simple segmentation: split video into chunks every N frames (approx per coach)
    frames_per_coach = int((width / min_coach_width_px) * fps / 2)
    coach_idx = 1
    frame_idx = 0

    out = None
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    videos = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_idx % frames_per_coach == 0:
            if out:
                out.release()
            folder = coach_folder(work_dir, train_number, coach_idx)
            video_file = os.path.join(folder, coach_video_name(train_number, coach_idx))
            out = cv2.VideoWriter(video_file, fourcc, fps, (width, height))
            videos.append(video_file)
            coach_idx += 1
        out.write(frame)
        frame_idx += 1

    if out:
        out.release()
    cap.release()
    return videos
