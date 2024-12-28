from flask import Flask, render_template, redirect, url_for, request, jsonify
from database import add_person, get_all_persons, get_person_by_usn, update_tracking
import cv2
import face_recognition
import subprocess
import signal
import os

app = Flask(__name__, template_folder='templates')

process = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/add_person', methods=['POST'])
def add_person_route():
    data = request.get_json()
    usn = data['usn']
    name = data['name']

    # Check if USN already exists
    existing_person = get_person_by_usn(usn)
    if existing_person:
        return jsonify({"message": "USN already exists in database"}), 400

    video_capture = cv2.VideoCapture(0)
    if not video_capture.isOpened():
        return jsonify({"message": "Failed to access camera"}), 500

    max_attempts = 5
    attempt = 0

    try:
        while attempt < max_attempts:
            ret, frame = video_capture.read()
            if not ret:
                attempt += 1
                continue

            # Detect faces
            face_locations = face_recognition.face_locations(frame)
            
            if len(face_locations) == 0:
                attempt += 1
                if attempt == max_attempts:
                    return jsonify({"message": "No face detected. Please try again"}), 400
                continue
            
            if len(face_locations) > 1:
                return jsonify({"message": "Multiple faces detected. Please ensure only one person is in frame"}), 400

            # Get face encodings
            face_encodings = face_recognition.face_encodings(frame, face_locations)
            if not face_encodings:
                attempt += 1
                continue

            # Crop and store face image
            top, right, bottom, left = face_locations[0]
            face_image = frame[top:bottom, left:right]
            face_image_encoded = cv2.imencode('.jpg', face_image)[1].tobytes()

            # Add to database
            add_person(usn, name, face_encodings[0].tobytes(), face_image_encoded)
            
            return jsonify({
                "message": "Person added successfully",
                "usn": usn,
                "name": name
            }), 200

        return jsonify({"message": "Failed to capture clear face image. Please try again"}), 400

    except Exception as e:
        return jsonify({"message": f"Error adding person: {str(e)}"}), 500
    
    finally:
        video_capture.release()

@app.route('/api/start_recognition', methods=['POST'])
def start_recognition():
    global process
    if process is None:
        process = subprocess.Popen(["python3", "src/face_recognition_app.py"])
        return jsonify({"message": "Face recognition started"}), 200
    return jsonify({"message": "Face recognition is already running"}), 400

@app.route('/api/stop_recognition', methods=['POST'])
def stop_recognition():
    global process
    if process is not None:
        os.kill(process.pid, signal.SIGINT)
        process = None
        return jsonify({"message": "Face recognition stopped"}), 200
    return jsonify({"message": "Face recognition is not running"}), 400

@app.route('/api/track_person', methods=['POST'])
def track_person():
    global process
    data = request.get_json()
    usn = data['usn']
    if process is None:
        process = subprocess.Popen(["python3", "src/person_tracking.py", usn])
        return jsonify({"message": "Tracking started"}), 200
    return jsonify({"message": "Tracking is already running"}), 400

@app.route('/api/persons', methods=['GET'])
def get_persons():
    persons = get_all_persons()
    return jsonify(persons), 200
    

if __name__ == '__main__':
    app.run(debug=True)

# from flask import Flask, render_template, redirect, url_for, request, jsonify
# from database import add_person, get_all_persons, get_person_by_usn, update_tracking
# import cv2
# import face_recognition
# import subprocess
# import signal
# import os

# app = Flask(__name__, template_folder='templates')

# process = None

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/api/add_person', methods=['POST'])
# def add_person_route():
#     data = request.get_json()
#     usn = data['usn']
#     name = data['name']

#     # Capture a single frame from the webcam
#     video_capture = cv2.VideoCapture(0)
#     try:
#         ret, frame = video_capture.read()
#         if ret:
#             face_encoding = face_recognition.face_encodings(frame)[0]
#             face_image = cv2.imencode('.jpg', frame)[1].tobytes()
#             add_person(usn, name, face_encoding.tobytes(), face_image)
#             return jsonify({"message": "Person added successfully"}), 200
#         return jsonify({"message": "Failed to capture image"}), 500
#     finally:
#         video_capture.release()

# @app.route('/api/start_recognition', methods=['POST'])
# def start_recognition():
#     global process
#     if process is None:
#         process = subprocess.Popen(["python3", "src/face_recognition_app.py"])
#         return jsonify({"message": "Face recognition started"}), 200
#     return jsonify({"message": "Face recognition is already running"}), 400

# @app.route('/api/stop_recognition', methods=['POST'])
# def stop_recognition():
#     global process
#     if process is not None:
#         os.kill(process.pid, signal.SIGINT)
#         process = None
#         return jsonify({"message": "Face recognition stopped"}), 200
#     return jsonify({"message": "Face recognition is not running"}), 400

# @app.route('/api/track_person', methods=['POST'])
# def track_person():
#     global process
#     data = request.get_json()
#     usn = data['usn']
#     if process is None:
#         process = subprocess.Popen(["python3", "src/face_recognition_app.py", usn])
#         return jsonify({"message": "Tracking started"}), 200
#     return jsonify({"message": "Tracking is already running"}), 400

# @app.route('/api/persons', methods=['GET'])
# def get_persons():
#     persons = get_all_persons()
#     return jsonify(persons), 200

# @app.route('/add_person', methods=['GET'])
# def add_person_page():
#     return render_template('add_person.html')

# if __name__ == '__main__':
#     app.run(debug=True)

