from ultralytics import YOLO

model = YOLO("yolo11n.pt")

# Update data path to your dataset
model.train(
    data="path/to/your/data.yaml",
    epochs=20,
    imgsz=640,
    batch=8,
    project="comparison",
    name="yolov11"
)

metrics = model.val()
print(metrics)

model.val(split="test")

from ultralytics import YOLO

model = YOLO("runs/detect/comparison/yolov11/weights/best.pt")
metrics = model.val(save=True)
