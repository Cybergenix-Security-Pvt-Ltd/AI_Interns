import cv2
import face_recognition
import os
import torch
import numpy as np

# Load YOLOv5 model
yolo_model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Load known faces
print("Loading known faces...")
known_encodings = []
known_names = []

known_dir = 'known_faces'

for filename in os.listdir(known_dir):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        path = os.path.join(known_dir, filename)
        image = face_recognition.load_image_file(path)
        encodings = face_recognition.face_encodings(image)

        if encodings:
            known_encodings.append(encodings[0])
            name = os.path.splitext(filename)[0]
            known_names.append(name)
            print(f"Loaded face for: {name}")
        else:
            print(f"Warning: No face found in {filename}")

# Start webcam
print("Starting camera...")
video_capture = cv2.VideoCapture(0)
TOLERANCE = 0.45

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Face recognition
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    recognized_faces = []  # Save recognized face boxes

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance=TOLERANCE)
        name = "Access Denied"

        face_distances = face_recognition.face_distance(known_encodings, face_encoding)
        if matches:
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = f"Access Granted: {known_names[best_match_index]}"

        # Scale face locations back up
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw rectangle and label
        color = (0, 255, 0) if "Granted" in name else (0, 0, 255)
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        # Save face box
        recognized_faces.append((left, top, right, bottom))

    # Object detection with YOLOv5
    results = yolo_model(frame)
    detections = results.pandas().xyxy[0]

    for _, row in detections.iterrows():
        x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
        label = row['name']
        conf = row['confidence']

        if conf > 0.25:
            # Skip drawing 'person' if overlaps with recognized face
            if label == 'person':
                skip = False
                for fx1, fy1, fx2, fy2 in recognized_faces:
                    if not (x2 < fx1 or x1 > fx2 or y2 < fy1 or y1 > fy2):
                        skip = True
                        break
                if skip:
                    continue

            # Draw object box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    # Show frame
    cv2.imshow("Face + Object Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
