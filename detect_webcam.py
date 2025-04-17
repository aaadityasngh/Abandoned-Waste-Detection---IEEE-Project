import cv2
from ultralytics import YOLO
from utils import draw_segmentation_mask

model = YOLO("model/yolov8-trash.pt")
cap = cv2.VideoCapture(0)

print("🔴 Press 'q' to quit webcam stream.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    result = model.predict(frame, verbose=False)[0]
    masked_frame, _ = draw_segmentation_mask(frame.copy(), result)

    cv2.imshow("Real-time Waste Detection (Press 'q' to exit)", masked_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("🟢 Webcam stream stopped.")