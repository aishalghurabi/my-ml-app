from ultralytics import YOLO
import os

# Load model once
model = YOLO("model/best.pt")

def predict(image_path):
    results = model(image_path)

    output_path = os.path.join("static", "result.jpg")
    results[0].save(filename=output_path)

    return output_path