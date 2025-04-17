import cv2
import numpy as np
import json
import os
import time

CLASS_COLORS = {
    "cardboard": (255, 165, 0),
    "plastic bag": (0, 255, 255),
    "plastic bottle": (0, 255, 0),
    "trash": (255, 0, 0),
    "tree": (128, 0, 128)
}

def draw_segmentation_mask(frame, result):
    if result.masks is None or result.boxes is None:
        return frame, []

    masks = result.masks.data.cpu().numpy()
    classes = result.boxes.cls.cpu().numpy().astype(int)
    names = result.names
    detected_items = []

    for mask, cls in zip(masks, classes):
        name = names[cls]
        color = CLASS_COLORS.get(name, (255, 255, 255))

        # Create colored mask
        mask_resized = cv2.resize(mask, (frame.shape[1], frame.shape[0]))
        binary_mask = (mask_resized > 0.5).astype(np.uint8)
        colored_mask = np.stack([binary_mask * c for c in color], axis=-1)
        frame = cv2.addWeighted(frame, 1.0, colored_mask.astype(np.uint8), 0.5, 0)

        # Draw class name label
        moments = cv2.moments(binary_mask)
        if moments["m00"] != 0:
            cx = int(moments["m10"] / moments["m00"])
            cy = int(moments["m01"] / moments["m00"])
            cv2.putText(frame, name, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        detected_items.append(name)

    return frame, detected_items

def log_detection(path, frame_no, items):
    log_data = []
    if os.path.exists(path):
        with open(path) as f:
            try: log_data = json.load(f)
            except: log_data = []

    log_data.append({
        "frame": frame_no,
        "detected_items": items,
        "timestamp": time.time()
    })

    with open(path, "w") as f:
        json.dump(log_data, f, indent=2)
