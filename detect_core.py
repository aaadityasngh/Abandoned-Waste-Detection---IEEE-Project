import cv2
import os
import time
from ultralytics import YOLO
from utils import draw_segmentation_mask, log_detection

def run_detection(video_path, output_path, frame_path, log_path):
    model = YOLO("model/yolov8-trash.pt")

    os.makedirs("runs/results", exist_ok=True)
    os.makedirs("assets", exist_ok=True)

    if os.path.exists(output_path): os.remove(output_path)
    if os.path.exists(log_path): os.remove(log_path)

    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS) or 20.0
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret or frame is None:
            break

        result = model.predict(frame, verbose=False)[0]
        labeled_frame, detected_items = draw_segmentation_mask(frame.copy(), result)

        if frame_count == 0:
            cv2.imwrite(frame_path, labeled_frame)

        log_detection(log_path, frame_count, detected_items)
        out.write(labeled_frame)
        frame_count += 1

    cap.release()
    out.release()
