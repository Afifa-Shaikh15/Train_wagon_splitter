import tkinter as tk
from tkinter import filedialog, messagebox
import os
import json
from main import run_pipeline

def run_from_gui():
    video_path = video_entry.get().strip()
    train_number = train_entry.get().strip()

    if not video_path or not os.path.exists(video_path):
        messagebox.showerror("Error", "Please select a valid video file.")
        return
    if not train_number:
        messagebox.showerror("Error", "Please enter a train number.")
        return

    cfg = {
        "train_number": train_number,
        "video_path": video_path,
        "work_dir": "output",
        "min_coach_width_px": 150,
        "motion_threshold": 30,
        "projection_smooth_kernel": 15,
        "yolo_model": None,
        "frame_extract_rate": 10,   # every 10th frame
        "report_thumbnail_w": 400
    }

    try:
        report_file = run_pipeline(cfg)
        if report_file:
            messagebox.showinfo("Success", f"Processing complete!\nReport saved: {report_file}")
        else:
            messagebox.showwarning("No Output", "No frames extracted. Report not generated.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def browse_file():
    file_path = filedialog.askopenfilename(
        title="Select Train Video",
        filetypes=[("Video files", "*.mp4;*.avi;*.mov"), ("All files", "*.*")]
    )
    if file_path:
        video_entry.delete(0, tk.END)
        video_entry.insert(0, file_path)

# Tkinter GUI
root = tk.Tk()
root.title("🚆 Train Wagon Processor")

tk.Label(root, text="Train Number:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
train_entry = tk.Entry(root, width=40)
train_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Video Path:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
video_entry = tk.Entry(root, width=40)
video_entry.grid(row=1, column=1, padx=10, pady=5)
browse_btn = tk.Button(root, text="Browse", command=browse_file)
browse_btn.grid(row=1, column=2, padx=10, pady=5)

run_btn = tk.Button(root, text="Run Processing", command=run_from_gui, bg="green", fg="white")
run_btn.grid(row=2, column=1, pady=15)

root.mainloop()
