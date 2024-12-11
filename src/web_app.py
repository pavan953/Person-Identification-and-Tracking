# from flask import Flask, render_template, redirect, url_for, request, jsonify
# from database import add_person, get_all_persons
# import cv2
# import face_recognition

# app = Flask(__name__, template_folder='templates')

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
#     import subprocess
#     subprocess.Popen(["python3", "src/face_recognition_app.py"])
#     return jsonify({"message": "Face recognition started"}), 200

# @app.route('/api/persons', methods=['GET'])
# def get_persons():
#     persons = get_all_persons()
#     return jsonify(persons), 200

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, redirect, url_for, request, jsonify
# from database import add_person, get_all_persons, get_person_by_usn, update_tracking
# import cv2
# import face_recognition

# app = Flask(__name__, template_folder='templates')

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
#     import subprocess
#     subprocess.Popen(["python3", "src/face_recognition_app.py"])
#     return jsonify({"message": "Face recognition started"}), 200

# @app.route('/api/persons', methods=['GET'])
# def get_persons():
#     persons = get_all_persons()
#     return jsonify(persons), 200

# @app.route('/api/track_person', methods=['POST'])
# def track_person():
#     data = request.get_json()
#     usn = data['usn']
#     person = get_person_by_usn(usn)
#     if person:
#         return jsonify({
#             "usn": person[0],
#             "name": person[1],
#             "face_image": person[4].decode('latin1')  # Convert BLOB to string
#         }), 200
#     return jsonify({"message": "Person not found"}), 404

# if __name__ == '__main__':
#     app.run(debug=True)


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

# if __name__ == '__main__':
#     app.run(debug=True)

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

    # Capture a single frame from the webcam
    video_capture = cv2.VideoCapture(0)
    try:
        ret, frame = video_capture.read()
        if ret:
            face_encoding = face_recognition.face_encodings(frame)[0]
            face_image = cv2.imencode('.jpg', frame)[1].tobytes()
            add_person(usn, name, face_encoding.tobytes(), face_image)
            return jsonify({"message": "Person added successfully"}), 200
        return jsonify({"message": "Failed to capture image"}), 500
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
        process = subprocess.Popen(["python3", "src/face_recognition_app.py", usn])
        return jsonify({"message": "Tracking started"}), 200
    return jsonify({"message": "Tracking is already running"}), 400

@app.route('/api/persons', methods=['GET'])
def get_persons():
    persons = get_all_persons()
    return jsonify(persons), 200

if __name__ == '__main__':
    app.run(debug=True)