# 📸 Face Recognition & Attendance Management System

A **Python-based Face Recognition and Attendance Management System** that uses **OpenCV** for face detection and **K-Nearest Neighbors (KNN)** for face recognition. The system captures facial data, trains a lightweight model, and records attendance with timestamps in CSV format.

This project is designed as a **simple, explainable, and offline-ready prototype** for learning computer vision–based biometric systems.

---

## 🚀 Features

* 🎥 Real-time face detection using Haar Cascade classifiers
* 🧠 Face recognition using K-Nearest Neighbors (KNN)
* 🗃️ Facial data stored using `pickle` serialization
* 🕒 Attendance logging with timestamps in `.csv` files
* 🗣️ Voice feedback using Windows Text-to-Speech (SAPI)
* 📁 Structured dataset and attendance storage

---

## 📁 Project Structure

```
face_attendance_system/
│
├── data/
│   ├── names.pkl                  # Pickled list of registered user names
│   └── faces_data.pkl             # Pickled NumPy array of facial features
│
├── Attendance/
│   └── Attendance_dd-mm-yyyy.csv  # Daily attendance logs
│
├── Dataset.py                     # Script to collect and store face data
├── Attendance.py                  # Script for face recognition & attendance
├── haarcascade_frontalface_default.xml  # Haar cascade model
└── bg.png                         # Background image for UI display
```

---

## ⚙️ Requirements

* Python **3.8+**
* OpenCV
* NumPy
* scikit-learn
* pywin32 (for Windows text-to-speech)

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/face-attendance-system.git
cd face-attendance-system
```

---

### 2️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install opencv-python numpy scikit-learn pywin32
```

---

### 4️⃣ Verify Required Files

Ensure the following files exist before running:

* `haarcascade_frontalface_default.xml`
* `bg.png`

---

## 🧪 How the System Works

### 🔹 Face Dataset Collection (`Dataset.py`)

* Prompts the user to enter a name.
* Captures **50 facial samples** via webcam.
* Extracts and stores facial features.
* Saves data to:

  * `data/faces_data.pkl`
  * `data/names.pkl`

---

### 🔹 Attendance Recognition (`Attendance.py`)

* Loads stored face data.
* Uses **KNN** to classify detected faces.
* Displays the recognized name with a bounding box.
* Provides voice feedback on successful recognition.
* Logs attendance with timestamp into a CSV file.

---

## ▶️ Usage

### 1️⃣ Register a New User

```bash
python Dataset.py
```

📌 Follow on-screen instructions and ensure proper lighting.

---

### 2️⃣ Start Attendance System

```bash
python Attendance.py
```

#### Keyboard Controls

* Press **`o`** → Mark attendance
* Press **`q`** → Quit application

---

## 📝 Sample Attendance Output

Attendance files are created daily inside the `Attendance/` folder:

**File:** `Attendance/Attendance_27-04-2025.csv`

```csv
NAME,TIME
Ayush,14:33-25
```

---

## 🛡️ Limitations & Notes

* Uses **classical ML (KNN)**, not deep learning
* Sensitive to lighting and camera angle
* Designed for **small-scale usage**
* Text-to-speech works only on **Windows**
* No liveness detection (spoofing possible)

---

## 🔮 Future Enhancements

* Replace KNN with deep learning models (FaceNet, Dlib, ArcFace)
* Add liveness detection (blink / motion-based)
* Store attendance in SQLite or cloud databases
* Cross-platform voice feedback
* GUI-based interface (Tkinter / PyQt)
* Multi-camera and multi-user scalability


Just tell me 👍
