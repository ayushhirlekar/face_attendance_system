from sklearn.neighbors import KNeighborsClassifier
import cv2
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime
from win32com.client import Dispatch

def speak(text):
    speak_engine = Dispatch("SAPI.SpVoice")
    speak_engine.Speak(text)

# Initialize video capture
video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default .xml')

# Load face data and labels
with open('data/names.pkl', 'rb') as w:
    LABELS = pickle.load(w)
with open('data/faces_data.pkl', 'rb') as f:
    FACES = pickle.load(f)

print('Shape of Faces matrix --> ', FACES.shape)

# Train KNN model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)

# Load background image
imgBackground = cv2.imread(r"C:\Users\Admin\PycharmProjects\face_attendance\face attendance\bg.png")

# CSV column names
COL_NAMES = ['NAME', 'TIME']

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w]  # Cropped face
        gray_crop = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
        resized_img = cv2.resize(gray_crop, (50, 75)).flatten().reshape(1, -1)  # Resize to match model

        output = knn.predict(resized_img)

        # Timestamp
        ts = time.time()
        date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
        timestamp = datetime.fromtimestamp(ts).strftime("%H:%M-%S")

        # Attendance file path
        attendance_file = os.path.join("Attendance", f"Attendance_{date}.csv")
        file_exists = os.path.isfile(attendance_file)

        # Draw bounding box and label
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 1)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 2)
        cv2.rectangle(frame, (x, y-40), (x+w, y), (50, 50, 255), -1)
        cv2.putText(frame, str(output[0]), (x, y-15), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)

        # Store attendance
        attendance = [str(output[0]), str(timestamp)]

    # Display frame on background image
    imgBackground[250:250 + 480, 640:640 + 640] = frame  # Centered properly
    cv2.imshow("Frame", imgBackground)

    k = cv2.waitKey(1)
    if k == ord('o'):
        speak("Attendance Taken..")
        time.sleep(5)

        with open(attendance_file, "+a", newline='') as csvfile:
            writer = csv.writer(csvfile)
            if not file_exists:
                writer.writerow(COL_NAMES)  # Write column names if file is new
            writer.writerow(attendance)  # Write attendance entry

    if k == ord('q'):
        break

# Release resources
video.release()
cv2.destroyAllWindows()
