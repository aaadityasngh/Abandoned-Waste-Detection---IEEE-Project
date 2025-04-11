from ultralytics import YOLO
import cv2
import os
import json
from datetime import datetime
from utils import draw_segmented_labels, log_detection

# Load YOLOv8 segmentation model (pretrained on trash or COCO)
model = YOLO("yolov8n-seg.pt") 

# Input video
video_path = "sample_video.mp4"  
cap = cv2.VideoCapture(video_path)

# Output video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
os.makedirs("runs/results", exist_ok=True)
out = cv2.VideoWriter("runs/results/output.mp4", fourcc, 30.0, (640, 480))

frame_no = 0
log_file = open("runs/results/log.json", "w")
log_file.write("[\n")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.resize(frame, (640, 480))
    results = model.predict(frame, imgsz=640, conf=0.4)

    annotated_frame, detections = draw_segmented_labels(frame, results[0])
    for det in detections:
        log_detection(log_file, det, frame_no)

    out.write(annotated_frame)
    frame_no += 1

    cv2.imshow("Segmented Trash Detection", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

log_file.write("\n]")
log_file.close()
cap.release()
out.release()
cv2.destroyAllWindows()
