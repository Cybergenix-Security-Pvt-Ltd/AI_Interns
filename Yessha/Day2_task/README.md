
# 🔒 Face + Object Detection System using YOLOv5 & Face Recognition

This project combines real-time **face recognition** and **object detection** using **YOLOv5**. The webcam feed is used to:
- ✅ Recognize known faces (e.g., "Access Granted: Yessha")
- ✅ Detect and label surrounding objects (e.g., bottle, phone, chair)
- ❌ Skip drawing a "person" box if the face is already recognized

---

## 🧠 Features

- Face recognition using the `face_recognition` library (built on dlib)
- Object detection using `YOLOv5` via PyTorch
- Works in real-time with bounding boxes and labels

---

## 🗂️ Folder Structure

```
day2/
├── main.py                # Final script
├── known_faces/           # Folder with reference face images
│   └── yessha.jpg
├── yolov5/                # Cloned YOLOv5 repo
│   ├── yolov5s.pt
│   └── (all YOLOv5 files)
└── README.md
```

---

## ⚙️ Setup Instructions

### ✅ 1. Install Python 3.8+ and pip

Download Python from: https://www.python.org/downloads/

During installation, check: ✅ "Add Python to PATH"

---

### ✅ 2. Clone YOLOv5 Repository

```bash
cd day2
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
```

---

### ✅ 3. Download YOLOv5 Pretrained Model

```bash
# While inside yolov5/ directory
wget https://github.com/ultralytics/yolov5/releases/download/v6.0/yolov5s.pt
```

Alternatively, it will auto-download when you first run the script.

---

### ✅ 4. Install Additional Required Libraries

```bash
pip install face_recognition opencv-python torch torchvision torchaudio numpy
```

> ⚠️ For Windows: You must have **CMake** and **Visual C++ Build Tools** installed for `dlib` to work.

---

## 🧩 Installing CMake & Build Tools (Windows only)

### 🔧 Install CMake

- Download: https://cmake.org/download/
- During install: ✅ check "Add CMake to system PATH"

### 🔧 Install Visual Studio C++ Build Tools

- Download: https://visualstudio.microsoft.com/visual-cpp-build-tools/
- During install, check:
  - ✅ "C++ build tools"
  - ✅ "Windows 10 SDK"
  - ✅ "C++ CMake tools for Windows"

---

## 🚀 Running the Project

```bash
python main.py
```

- 🟢 If a known face is detected → "Access Granted: Name"
- 🔴 If unknown → "Access Denied"
- 🔵 Objects like bottles, phones, etc. are detected with YOLO
- ❌ Person boxes from YOLO are **ignored** if the person is already recognized via face

---

## 🧪 Test YOLOv5 Object Detection Alone

```python
import torch, cv2

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    results = model(frame)
    results.render()
    cv2.imshow('YOLOv5 Only', results.ims[0])
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```

---

## 📄 License

This project is for educational/demo purposes. Credits to:
- [ultralytics/yolov5](https://github.com/ultralytics/yolov5)
- [face_recognition by Adam Geitgey](https://github.com/ageitgey/face_recognition)
