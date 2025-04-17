import os
import time
import threading
from detect_core import run_detection

WATCH_FOLDER = "watch_folder"
PROCESSED_FOLDER = "watch_folder/processed"
OUTPUT_FOLDER = "runs/results"

def process_videos():
    os.makedirs(WATCH_FOLDER, exist_ok=True)
    os.makedirs(PROCESSED_FOLDER, exist_ok=True)
    print("🔁 Watching for new videos every 60 seconds...")

    while True:
        for file in os.listdir(WATCH_FOLDER):
            if file.endswith(".mp4"):
                input_path = os.path.join(WATCH_FOLDER, file)
                output_path = os.path.join(OUTPUT_FOLDER, f"auto_{file}")
                frame_path = os.path.join("assets", f"{file}_frame.png")
                log_path = os.path.join(OUTPUT_FOLDER, f"{file}.log.json")

                print(f"▶️ Processing {file}")
                run_detection(input_path, output_path, frame_path, log_path)
                os.rename(input_path, os.path.join(PROCESSED_FOLDER, file))
                print(f"✅ Processed and moved: {file}")
        time.sleep(60)  # check every 60 sec

def start_scheduler():
    t = threading.Thread(target=process_videos, daemon=True)
    t.start()
