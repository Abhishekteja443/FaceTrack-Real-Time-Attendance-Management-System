# Real-Time Attendance Management System

## Overview
This project implements a **Real-Time Attendance Management System** using **computer vision** techniques. The system detects and recognizes faces using **Haar Cascade Classifier** for face detection and **K-Nearest Neighbors (KNN)** for face classification. Additionally, a **GUI application** has been developed to provide a user-friendly interface for managing attendance records.

## Features
- **Real-Time Face Detection**: Uses Haar Cascade Classifier to detect faces in a live video feed.
- **Face Recognition**: KNN algorithm classifies faces based on a pre-stored dataset.
- **Attendance Logging**: Recognized faces are marked as present and stored in an attendance log.
- **Graphical User Interface (GUI)**: A user-friendly interface to interact with the system, view attendance records, and manage the database.

## Technologies Used
- **Python** (Primary Programming Language)
- **OpenCV** (For face detection and image processing)
- **NumPy & Pandas** (For data handling and manipulation)
- **Tkinter** (For GUI development)
- **scikit-learn** (For implementing the KNN classifier)

## Installation
### Prerequisites
Ensure you have Python installed. You can download it from [Python.org](https://www.python.org/downloads/).

### Clone the Repository
```bash
git clone https://github.com/your-username/real-time-attendance.git
cd real-time-attendance
```

### Install Required Dependencies
```bash
pip install opencv-python numpy pandas scikit-learn tkinter
```

## Usage
### Step 1: Train the Model
1. Collect face images of individuals and store them in a dataset folder.
2. Run the training script to process images and generate embeddings for classification.
```bash
python train_model.py
```

### Step 2: Start the Attendance System
Run the main application script:
```bash
python attendance_system.py
```

### Step 3: Interact with the GUI
- **Start Camera**: Detect and recognize faces in real-time.
- **View Attendance**: Display and export attendance records.
- **Add New Faces**: Register new individuals in the database.

## File Structure
```
real-time-attendance/
│── dataset/                 # Folder containing face images for training
│── models/                  # Trained models and face embeddings
│── attendance_logs/         # Stored attendance records
│── gui.py                   # GUI application
│── train_model.py           # Script for training the face classifier
│── attendance_system.py     # Main script for real-time attendance
│── requirements.txt         # Dependencies list
│── README.md                # Project documentation
```

## Future Improvements
- Integrate **Deep Learning models** (e.g., CNNs) for improved accuracy.
- Add **cloud storage** support for attendance records.
- Implement **RFID integration** for multi-factor authentication.

## License
This project is licensed under the MIT License.

## Author
**Your Name**  
Email: your.email@example.com  
LinkedIn: [Your Profile](https://www.linkedin.com/in/yourprofile)

---
Feel free to contribute to this project by opening pull requests and reporting issues!

