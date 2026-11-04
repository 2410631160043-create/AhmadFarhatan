import os
from ultralytics import YOLO

PT = os.path.join(os.path.expanduser("~"), "Downloads", "best_webcam.pt")
model = YOLO(PT)
hasil = model.export(format="onnx", imgsz=480, opset=12, simplify=False, dynamic=False)
print("Selesai. File ONNX:", hasil)
