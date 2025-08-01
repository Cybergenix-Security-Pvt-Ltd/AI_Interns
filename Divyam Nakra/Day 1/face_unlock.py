import face_recognition
import cv2

# loading the known face
my_image = face_recognition.load_image_file("virat_kohli.jpg")
my_face_encoding = face_recognition.face_encodings(my_image)[0]

# Turning on the webcam
camera = cv2.VideoCapture(0)

while True:
    is_frame_read, current_frame = camera.read()
    rgb_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2RGB)

    all_face_positions = face_recognition.face_locations(rgb_frame)
    all_face_encodings = face_recognition.face_encodings(rgb_frame, all_face_positions)

    for i in range(len(all_face_encodings)):
        current_face_encoding = all_face_encodings[i]
        current_face_position = all_face_positions[i]

        match_result = face_recognition.compare_faces([my_face_encoding], current_face_encoding)

        top, right, bottom, left = current_face_position

        if match_result[0]:
            cv2.rectangle(current_frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(current_frame, "Access Granted: Welcome!", (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        else:
            cv2.rectangle(current_frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(current_frame, "Access Denied", (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    cv2.imshow("Face Unlock System", current_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
