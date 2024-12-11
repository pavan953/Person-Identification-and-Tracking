import cv2
import numpy as np

# Initialize tracker
tracker = cv2.TrackerCSRT_create()

# Read video
cap = cv2.VideoCapture("video.mp4")

# Read first frame
success, img = cap.read()

# Select the bounding box on the first frame
bbox = cv2.selectROI("Tracking", img, False)

# Initialize the tracker
tracker.init(img, bbox)

while True:
    success, img = cap.read()

    # Update tracker
    success, bbox = tracker.update(img)

    # Draw the box
    if success:
        (x, y, w, h) = [int(i) for i in bbox]
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow("Tracking", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()