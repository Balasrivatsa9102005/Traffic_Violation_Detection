from ultralytics import YOLO
import numpy as np

model = YOLO("yolov8n.pt")

# Update data path to your dataset
model.train(
    data=r"path/to/your/data.yaml",
    epochs=20,
    imgsz=640,
    batch=8,
    project="yolo_traffic",
    name="helmet_detection"
)

from ultralytics import YOLO

model = YOLO(r"yolo_traffic/helmet_detection3/weights/best.pt")
results = model.predict(r"path/to/your/test/image.jpg")
results[0].show()

with_helmet = 0
without_helmet = 0

for box in results[0].boxes:
    class_id = int(box.cls[0])
    if class_id == 0:
        with_helmet += 1
    elif class_id == 1:
        without_helmet += 1

if without_helmet > 0:
    print(f"PENALTY: {without_helmet} rider(s) without helmets detected")
else:
    print("SAFE: All riders have helmets")
