
# 📸 Face Recognition & Attendance Management System

A Python-based project that uses **OpenCV** and **K-Nearest Neighbors (KNN)** for real-time face recognition and **CSV-based attendance tracking**. This system captures facial data, trains a model, and logs attendance with timestamps.

---

## 🚀 Features

- 🎥 Real-time face detection using Haar cascades
- 🧠 KNN-based face recognition
- 🗃️ Face data saved using `pickle`
- 🕒 Attendance stored with timestamps in `.csv` files
- 🗣️ Voice feedback using Windows SAPI
- 📁 Organized data and attendance folder structure

---

## 📁 Project Structure

```
face_attendance_system/
│
├── data/
│   ├── names.pkl             # Pickled list of user names
│   └── faces_data.pkl        # Pickled NumPy array of facial data
│
├── Attendance/
│   └── Attendance_dd-mm-yyyy.csv   # Daily attendance records
│
├── Dataset.py               # Script to register new face data
├── Attendance.py            # Script to recognize faces and log attendance
├── haarcascade_frontalface_default.xml  # Face detection model
└── bg.png                   # Background image for display
```

---

## ⚙️ Requirements

- Python 3.x  
- OpenCV  
- NumPy  
- scikit-learn  
- pywin32 (for text-to-speech on Windows)

Install dependencies with:

```bash
pip install opencv-python numpy scikit-learn pywin32
```

---

## 🧪 How It Works

1. **Dataset Collection (`Dataset.py`)**
   - Prompts for a name and captures 50 face samples.
   - Saves data into `faces_data.pkl` and `names.pkl`.

2. **Attendance Recognition (`Attendance.py`)**
   - Loads trained face data and uses KNN for recognition.
   - Displays the recognized name with a bounding box.
   - Press `'o'` to log attendance with time.
   - Press `'q'` to quit.

---

## 📌 Usage

### 1. Register a New Face
```bash
python Dataset.py
```

### 2. Start Attendance System
```bash
python Attendance.py
```

---

## 📝 Sample Output

- Attendance is logged in:  
  `Attendance/Attendance_27-04-2025.csv`

```csv
NAME,TIME
Ayush,14:33-25
```

---

## 🛡️ Limitations & Notes

- Currently stores data in `.pkl` files and `.csv` for simplicity.
- Works best under good lighting conditions.
- Windows-only (due to `win32com.client` for speech).

---

## 🧠 Future Enhancements

- Replace KNN with deep learning (e.g., FaceNet, Dlib).
- Use SQLite or Firebase instead of CSV.
- Add GUI with Tkinter or PyQt.
- Enable cloud-based attendance syncing.

---

## 📸 Screenshots

> *(Add screenshots or screen recordings here to enhance your repo.)*

---

## 👤 Author

**Ayush**  
Feel free to ⭐ the repo or suggest improvements!
