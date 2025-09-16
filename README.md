# Train_wagon_splitter
Train_wagon_splitter_full is a Python-based video processing pipeline designed to analyze train videos (typically bottom or side views) and automatically split them into smaller segments corresponding to individual coaches/wagons. 

Key Features

Coach Detection & Splitting

Processes a full train video.

Detects coach boundaries using motion and visual features (e.g., vertical gradients, structural differences).

Splits the video into smaller clips, each containing exactly one coach.

Coach Counting

Automatically counts the number of wagons in the train.

Coverage Report Generation

Extracts a minimal set of frames covering the full length of the train (nose to tail).

Compiles the selected frames into a PDF/HTML report for quick review.

Organized Output Folder Structure

output/coach_1/ → Video and images of coach 1

output/coach_2/ → Video and images of coach 2

output/report.pdf → Coverage report

Configurable Options

Frame sampling rate (--sample-rate)

Debug visualization (--show-debug)

Output format (--make-pdf or --make-html)

Technologies

Python 3.x – Core programming language

OpenCV (cv2) – Video processing, frame extraction, image stitching, boundary detection

NumPy – Numerical computations, frame matrix operations

Matplotlib / Seaborn – Debug visualization & plotting (optional)

ReportLab / WeasyPrint – PDF/HTML coverage report generation

OS / Pathlib – File and folder management

Argparse – Command-line interface for configurable options
