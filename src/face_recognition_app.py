# import cv2
# import face_recognition
# import numpy as np
# from database import get_all_persons, add_person, update_last_recognized
# from datetime import datetime

# # Load known face encodings and names from the database
# known_face_encodings = []
# known_face_names = []

# def load_known_faces():
#     global known_face_encodings, known_face_names
#     persons = get_all_persons()
#     known_face_encodings = [np.frombuffer(person[1], dtype=np.float64) for person in persons]
#     known_face_names = [person[0] for person in persons]

# load_known_faces()

# # Initialize video capture
# video_capture = cv2.VideoCapture(0)

# while True:
#     ret, frame = video_capture.read()
#     if not ret:
#         break

#     face_locations = face_recognition.face_locations(frame)
#     face_encodings = face_recognition.face_encodings(frame, face_locations)

#     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#         matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#         name = "Unknown"

#         face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
#         if face_distances.size > 0:
#             best_match_index = np.argmin(face_distances)
#             if matches[best_match_index]:
#                 name = known_face_names[best_match_index]
#                 face_image = cv2.imencode('.jpg', frame[top:bottom, left:right])[1].tobytes()
#                 update_last_recognized(name, face_image)

#         if name == "Unknown":
#             cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
#             cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
#             font = cv2.FONT_HERSHEY_DUPLEX
#             cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
#             cv2.imshow('Video', frame)
#             cv2.waitKey(1)
#             new_name = input("Enter the name for the new face: ")
#             face_image = cv2.imencode('.jpg', frame[top:bottom, left:right])[1].tobytes()
#             add_person(new_name, face_encoding.tobytes(), face_image)
#             load_known_faces()
#         else:
#             cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
#             cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
#             font = cv2.FONT_HERSHEY_DUPLEX
#             timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             cv2.putText(frame, f"{name} {timestamp}", (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

#     cv2.imshow('Video', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# video_capture.release()
# cv2.destroyAllWindows()

# import cv2
# import face_recognition
# import numpy as np
# from database import get_all_persons, add_person, update_last_recognized, update_tracking
# from datetime import datetime

# # Load known face encodings and names from the database
# known_face_encodings = []
# known_face_usns = []
# known_face_names = []

# def load_known_faces():
#     global known_face_encodings, known_face_usns, known_face_names
#     persons = get_all_persons()
#     known_face_encodings = [np.frombuffer(person[2], dtype=np.float64) for person in persons]
#     known_face_usns = [person[0] for person in persons]
#     known_face_names = [person[1] for person in persons]

# load_known_faces()

# # Initialize video capture
# video_capture = cv2.VideoCapture(0)

# while True:
#     ret, frame = video_capture.read()
#     if not ret:
#         break

#     face_locations = face_recognition.face_locations(frame)
#     face_encodings = face_recognition.face_encodings(frame, face_locations)

#     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#         matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#         name = "Unknown"
#         usn = "Unknown"

#         face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
#         if face_distances.size > 0:
#             best_match_index = np.argmin(face_distances)
#             if matches[best_match_index]:
#                 usn = known_face_usns[best_match_index]
#                 name = known_face_names[best_match_index]
#                 face_image = cv2.imencode('.jpg', frame[top:bottom, left:right])[1].tobytes()
#                 update_last_recognized(usn, face_image)
#                 update_tracking(usn, name, face_image)

#         if usn == "Unknown":
#             cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
#             cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
#             font = cv2.FONT_HERSHEY_DUPLEX
#             cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
#             cv2.imshow('Video', frame)
#             cv2.waitKey(1)
#             new_usn = input("Enter the USN for the new face: ")
#             new_name = input("Enter the name for the new face: ")
#             face_image = cv2.imencode('.jpg', frame[top:bottom, left:right])[1].tobytes()
#             add_person(new_usn, new_name, face_encoding.tobytes(), face_image)
#             load_known_faces()
#         else:
#             cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
#             cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
#             font = cv2.FONT_HERSHEY_DUPLEX
#             timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             cv2.putText(frame, f"{name} {timestamp}", (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

#     cv2.imshow('Video', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# video_capture.release()
# cv2.destroyAllWindows()



import cv2
import face_recognition
import numpy as np
from database import get_all_persons, update_last_recognized, update_tracking
from datetime import datetime
import sys

# Load known face encodings and names from the database
known_face_encodings = []
known_face_usns = []
known_face_names = []

def load_known_faces():
    global known_face_encodings, known_face_usns, known_face_names
    persons = get_all_persons()
    known_face_encodings = [np.frombuffer(person[2], dtype=np.float64) for person in persons]
    known_face_usns = [person[0] for person in persons]
    known_face_names = [person[1] for person in persons]

load_known_faces()

# Get the USN to track from the command line arguments
usn_to_track = sys.argv[1] if len(sys.argv) > 1 else None

# Initialize video capture
video_capture = cv2.VideoCapture(0)

found_usn = False

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        usn = "Unknown"

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        if face_distances.size > 0:
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                usn = known_face_usns[best_match_index]
                name = known_face_names[best_match_index]
                face_image = cv2.imencode('.jpg', frame[top:bottom, left:right])[1].tobytes()
                update_last_recognized(usn, face_image)
                update_tracking(usn, name, face_image)

        if usn == usn_to_track:
            found_usn = True
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cv2.putText(frame, f"{name} {timestamp}", (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        else:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, "Unknown", (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

if not found_usn:
    print("No one found")

video_capture.release()
cv2.destroyAllWindows()