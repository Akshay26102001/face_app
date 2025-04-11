import face_recognition
import cv2
import datetime

def recognize_face():
    video_capture = cv2.VideoCapture(0)
    known_image = face_recognition.load_image_file("known_face.jpg")  # Replace with actual path
    known_encoding = face_recognition.face_encodings(known_image)[0]

    while True:
        ret, frame = video_capture.read()
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for encoding in face_encodings:
            matches = face_recognition.compare_faces([known_encoding], encoding)
            if True in matches:
                video_capture.release()
                return datetime.datetime.now()

        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
