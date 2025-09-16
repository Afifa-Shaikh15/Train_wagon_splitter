import os
from pathlib import Path

def ensure_dir(path):
    Path(path).mkdir(parents=True, exist_ok=True)

def coach_folder(work_dir, train_number, idx):
    name = f"{train_number}_{idx}"
    full = os.path.join(work_dir, name)
    ensure_dir(full)
    return full

def coach_video_name(train_number, idx):
    return f"{train_number}_{idx}.mp4"

def coach_frame_name(train_number, idx, frame_no):
    return f"{train_number}_{idx}_{frame_no}.jpg"
