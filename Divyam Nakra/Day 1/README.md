# Face Recognition Unlock System 🔐

A simple real-time face recognition system using OpenCV and the `face_recognition` library. It uses your webcam to detect and identify a known face (e.g., Virat Kohli) and grants or denies access accordingly.

## 🚀 Features

- Real-time face detection
- Face matching with known image
- Access granted or denied overlay
- Press `Q` to exit the app

## 📂 File Structure

```
face-recognition-unlock/
├── face_unlock.py
├── virat_kohli.jpg
├── requirements.txt
├── README.md
└── .gitignore
```

## 🧠 Requirements

- Python 3.x
- OpenCV (`cv2`)
- face_recognition

Install them using:

```bash
pip install -r requirements.txt
```

## 🖼️ Setup

1. Place a known face image (e.g., `virat_kohli.jpg`) in the project folder.
2. Run the program:

```bash
python face_unlock.py
```

3. Look into your webcam — if the face matches the reference image, access is granted.

## ❌ To Quit

Press `Q` to exit the webcam interface.

---

## 📸 Screenshot

Coming soon...

## 📄 License

This project is open-source and free to use under the MIT license.
