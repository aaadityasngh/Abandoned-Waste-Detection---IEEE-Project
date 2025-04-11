import cv2
import json
from datetime import datetime

def draw_segmented_labels(frame, result):
    names = result.names
    detections = []

    for seg, cls_id in zip(result.masks.xy, result.boxes.cls):
        cls_id = int(cls_id)
        label = names[cls_id]
        detections.append({
            "label": label,
            "time": datetime.now().strftime("%H:%M:%S")
        })
        color = (0, 255, 0)
        pts = seg.reshape((-1, 1, 2)).astype("int32")
        cv2.polylines(frame, [pts], isClosed=True, color=color, thickness=2)
        cv2.putText(frame, label, tuple(pts[0][0]), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    return frame, detections

def log_detection(file, detection, frame_no):
    log_entry = {
        "frame": frame_no,
        "label": detection['label'],
        "time": detection['time']
    }
    json.dump(log_entry, file)
    file.write(",\n")
