from flask import Flask, render_template, request, jsonify
import cv2 as cv
import numpy as np
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load YOLO model
class_name = []
with open('utils/obj.names', 'r') as f:
    class_name = [cname.strip() for cname in f.readlines()]
net1 = cv.dnn.readNet('utils/yolov4_tiny.weights', 'utils/yolov4_tiny.cfg')
net1.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
net1.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)
model1 = cv.dnn_DetectionModel(net1)
model1.setInputParams(size=(640, 480), scale=1/255, swapRB=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})
    file = request.files['file']
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    img = cv.imread(filepath)
    if img is None:
        return jsonify({'error': 'Invalid image'})
    height, width = img.shape[:2]
    mask = np.zeros_like(img)
    mask[0:int(0.85*height), :] = 255
    masked_img = cv.bitwise_and(img, mask)
    Conf_threshold = 0.5
    NMS_threshold = 0.4
    classes, scores, boxes = model1.detect(masked_img, Conf_threshold, NMS_threshold)
    potholes = []
    for (classid, score, box) in zip(classes, scores, boxes):
        x, y, w, h = box
        recarea = w * h
        area = width * height
        severity = ""
        severity_threshold_low = 0.007
        severity_threshold_medium = 0.020
        if score >= 0.7:
            if (recarea / area) <= severity_threshold_low:
                severity = "Low"
            elif (recarea / area) <= severity_threshold_medium:
                severity = "Medium"
            else:
                severity = "High"
            potholes.append({
                'severity': severity,
                'score': float(score),
                'size': int(recarea),
                'box': [int(x), int(y), int(w), int(h)]
            })
            # Draw bounding box and label on image
            cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            label_text = f"pothole {round(score, 2)} ({severity})"
            cv.putText(img, label_text, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    # Encode image to base64
    import base64
    _, buffer = cv.imencode('.jpg', img)
    img_base64 = base64.b64encode(buffer).decode('utf-8')
    return jsonify({'potholes': potholes, 'image': img_base64})

if __name__ == '__main__':
    app.run(debug=True)
