import json
import os
from video_splitter import split_video
from frame_extractor import extract_frames
from detector import detect_components
from report_generator import generate_report
from utils import ensure_dir

def run_pipeline(cfg):
    """
    Run the full pipeline with a given config dictionary.
    """
    train_number = cfg["train_number"]
    video_path = cfg["video_path"]
    work_dir = cfg["work_dir"]
    frame_rate = cfg["frame_extract_rate"]
    ensure_dir(work_dir)

    print("Splitting video...")
    videos = split_video(video_path, train_number, work_dir, cfg["min_coach_width_px"])
    print(f"Detected {len(videos)} coaches.")

    all_images = []
    for idx, v in enumerate(videos, 1):
        folder = os.path.dirname(v)
        print(f"Extracting frames for coach {idx}...")
        frames = extract_frames(v, train_number, idx, folder, rate=frame_rate)
        print(f"Annotating frames for coach {idx}...")
        for img in frames:
            detect_components(img)
        all_images.extend(frames[:2])  # pick minimal 2 images per coach

    if not all_images:
        print("⚠️ No frames extracted. Skipping report.")
        return None

    report_file = os.path.join(work_dir, f"{train_number}_report.pdf")
    print("Generating report...")
    generate_report(all_images, report_file)
    print(f"Report saved at {report_file}")
    return report_file

def main(config_file="sample_config.json"):
    with open(config_file, "r") as f:
        cfg = json.load(f)
    return run_pipeline(cfg)

if __name__ == "__main__":
    main()
