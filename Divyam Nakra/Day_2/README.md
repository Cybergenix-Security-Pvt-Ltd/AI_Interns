# 🧠 Face Recognition + Object Detection System 🔒📦

This is a Python-based **face recognition and object detection system**. It uses your face to grant access and then detects real-world objects around you for 10 seconds using **YOLOv3**.

---

## 💡 Features
- 👤 Face Unlock using `face_recognition`
- 🎯 Real-time object detection using **YOLOv3**
- 🎥 Live webcam feed with object labels & FPS counter
- 🔁 Auto-switches between face verification and object detection every 10 seconds

---

## 🔧 Requirements

Install the required libraries:

```bash
pip install -r requirements.txt
```

Also, download the following files:

- `yolov3.cfg`: [Download here](https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg)
- `yolov3.weights`: [Download here (~250MB)](https://pjreddie.com/media/files/yolov3.weights)
- `coco.names`: [Download here](https://github.com/pjreddie/darknet/blob/master/data/coco.names)

Place all files in the same folder as your script.

---

## ▶️ How to Run

1. Add a clear photo named `virat_kohli.jpg` (or your own) to the folder.
2. Run the script:

```bash
python face_yolo_system.py
```

3. If your face matches, it will say **"Access Granted: Welcome!"**
4. YOLO will then detect objects around you for 10 seconds.

---

## 📂 Folder Contents

```
face-unlock-object-detection/
├── face_yolo_system.py
├── yolov3.cfg
├── yolov3.weights
├── coco.names
├── virat_kohli.jpg
├── requirements.txt
└── README.md
```

---

## 💬 Credits

- Face Recognition: [`face_recognition`](https://github.com/ageitgey/face_recognition)
- Object Detection: [`YOLOv3`](https://pjreddie.com/darknet/yolo/)
- Author: [Divyam Nakra](https://github.com/YOUR_GITHUB_USERNAME)
