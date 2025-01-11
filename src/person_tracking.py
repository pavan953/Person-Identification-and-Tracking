import cv2
import numpy as np
import face_recognition
from database import get_all_persons
from datetime import datetime
import sys
import threading
import requests
from database import add_tracking_event

# List of camera IP addresses
camera_ips = [
    "http://192.168.90.41:8080/video",
]

# Load known face encodings and names from the database
known_face_encodings = []
known_face_usns = []
known_face_names = []

def load_known_faces():
    """
    Load face encodings, USNs, and names from the database.
    """
    global known_face_encodings, known_face_usns, known_face_names
    persons = get_all_persons()
    known_face_encodings = [np.frombuffer(person[2], dtype=np.float64) for person in persons]
    known_face_usns = [person[0] for person in persons]
    known_face_names = [person[1] for person in persons]

# Load initial known faces
load_known_faces()

# Get the USN to track from the command line arguments
usn_to_track = sys.argv[1] if len(sys.argv) > 1 else None

# Validate if USN exists in database
if usn_to_track and usn_to_track not in known_face_usns:
    requests.post('http://localhost:8000/api/person_not_found', 
                 json={'message': f'USN {usn_to_track} not found in database'})
    print(f"Error: USN {usn_to_track} not found in database")
    sys.exit(1)

# Initialize video captures for each camera
caps = [cv2.VideoCapture(ip) for ip in camera_ips]
frames = [None] * len(caps)
lock = threading.Lock()

def capture_frames(index, cap):
    global frames
    while True:
        success, frame = cap.read()
        if success:
            with lock:
                frames[index] = frame

# Start threads to capture frames from each camera
threads = []
for i, cap in enumerate(caps):
    thread = threading.Thread(target=capture_frames, args=(i, cap))
    thread.daemon = True
    thread.start()
    threads.append(thread)

person_found = False

while True:
    for i, frame in enumerate(frames):
        if frame is None:
            continue

        # Detect faces and compute encodings
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            usn = "Unknown"
            name = "Unknown"

            # Check if the face matches any known encoding
            if face_distances.size > 0:
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index] and face_distances[best_match_index] < 0.6:  # Threshold for face distance
                    usn = known_face_usns[best_match_index]
                    name = known_face_names[best_match_index]

            # Highlight the detected face
            if usn == usn_to_track:
                color = (0, 255, 0)  # Green for the tracked person
                label = f"{name} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                if not person_found:
                    person_found = True
                    # Add tracking event to database
                    add_tracking_event(usn, f'Camera {i}')
                    # Send notification
                    requests.post('http://localhost:5000/api/person_found', 
                                 json={'camera': f'Camera {i}', 'name': name})
            else:
                color = (0, 0, 255)  # Red for others
                label = f"{name} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}" if usn != "Unknown" else "Unknown"
            
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), color, cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, label, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the video feed
        cv2.imshow(f"Camera {i}", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release all video captures and close windows
for cap in caps:
    cap.release()
cv2.destroyAllWindows()