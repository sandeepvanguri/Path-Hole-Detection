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
├── app.py # Main Flask app
├── uploads/ # Folder for uploaded images (auto-created)
├── utils/
│ ├── yolov4_tiny.cfg # YOLOv4-Tiny config file
│ ├── yolov4_tiny.weights # YOLOv4-Tiny trained weights
│ └── obj.names # Class name file (e.g., 'pothole')
├── templates/
│ └── index.html # Frontend HTML page
└── README.md # This file

## For Running the app
python app.py

