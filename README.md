# 🕳️ Pothole Detection System using YOLOv4-Tiny

A web-based Flask application that detects potholes in road images using the YOLOv4-Tiny model.

---

## 🚀 Features

- Upload road images from the browser.
- Real-time pothole detection using YOLOv4-Tiny.
- Severity classification: Low, Medium, High.
- Displays bounding boxes and confidence score.

---

## 🧠 Model

- YOLOv4-Tiny: Lightweight object detection.
- Config files stored in `utils/`:
  - `yolov4_tiny.cfg`
  - `yolov4_tiny.weights`
  - `obj.names` (e.g., "pothole")

---

## 📁 Project Structure
Pothole-Detection-System-using-YOLO-Tiny-v4/
│
├── app.py
├── README.md
├── uploads/                    # Auto-created folder for uploaded images
├── utils/
│   ├── yolov4_tiny.cfg         # YOLO model config
│   ├── yolov4_tiny.weights     # YOLO model weights
│   └── obj.names               # Class labels (e.g., "pothole")
└── templates/
    └── index.html              # HTML frontend

## For Running the app
python app.py

