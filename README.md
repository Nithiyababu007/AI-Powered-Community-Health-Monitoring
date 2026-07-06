# 🏥 AI-Powered Community Health Monitoring System

## 📖 Project Overview

The AI-Powered Community Health Monitoring System is an intelligent web-based healthcare application developed using Python Flask. The system is designed to assist healthcare professionals in monitoring patient health records, maintaining medical information, and predicting potential health risks at an early stage with the help of Artificial Intelligence.

The application provides separate dashboards for Admin, Doctor, and Nurse users. Each user role has specific permissions to manage patients and healthcare records efficiently. The AI engine analyzes patient health information and provides risk assessment, enabling early disease detection and better healthcare management.

---

# 🎯 Objectives

- Develop an intelligent healthcare monitoring platform.
- Maintain digital patient health records.
- Predict potential health risks using AI-based analysis.
- Improve healthcare management efficiency.
- Reduce manual record maintenance.
- Support doctors and nurses with quick patient information access.
- Provide secure role-based authentication for different users.

---

# ✨ Features

- 🔐 User Authentication System
- 👨‍⚕️ Admin Dashboard
- 🩺 Doctor Dashboard
- 👩‍⚕️ Nurse Dashboard
- 👤 Patient Registration
- 📝 Patient Record Management
- ✏️ Edit Patient Details
- 🗑 Delete Patient Records
- 🤖 AI-Based Health Risk Prediction
- 📊 Patient Health Analysis
- 💾 SQLite Database Integration
- 📱 Responsive User Interface

---

# 🛠 Technologies Used

### Programming Language
- Python 3

### Framework
- Flask

### Database
- SQLite
- SQLAlchemy ORM

### Frontend
- HTML5
- CSS3

### Development Tools
- Visual Studio Code
- Git
- GitHub

---

# 📂 Project Structure

```
AI-Powered-Community-Health-Monitoring
│
├── app.py
├── ai_engine.py
├── config.py
├── requirements.txt
├── README.md
│
├── database
│   ├── database.db
│   └── schema.sql
│
├── models
│   ├── __init__.py
│   ├── user.py
│   └── patient.py
│
├── static
│   └── css
│       └── style.css
│
├── templates
│   ├── login.html
│   ├── admin_dashboard.html
│   ├── doctor_dashboard.html
│   ├── nurse_dashboard.html
│   ├── register_patient.html
│   ├── patient_list.html
│   ├── edit_patient.html
│   ├── 404.html
│   └── 500.html
│
└── venv
```

---

# ⚙ Installation Guide

## Step 1: Clone the Repository

```bash
git clone https://github.com/Nithiyababu007/AI-Powered-Community-Health-Monitoring.git
```

---

## Step 2: Navigate to the Project Folder

```bash
cd AI-Powered-Community-Health-Monitoring
```

---

## Step 3: Create Virtual Environment

```bash
python -m venv venv
```

---

## Step 4: Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

## Step 5: Install Required Packages

```bash
pip install -r requirements.txt
```

---

## Step 6: Run the Application

```bash
python app.py
```

---

## Step 7: Open the Browser

```
http://127.0.0.1:5000
```

---

# 👥 User Roles

## Administrator

- Manage users
- View dashboard
- Monitor patient records
- Access complete system information

---

## Doctor

- View patients
- Analyze patient health
- Monitor disease prediction

---

## Nurse

- Register patients
- Update patient details
- Maintain health records

---

# 🤖 AI Module

The AI module analyzes patient health information including symptoms, age, and other medical parameters. Based on predefined healthcare rules, the system predicts potential health risks and assists healthcare professionals in identifying patients who require immediate medical attention.

---

# 📊 Database

The project uses SQLite as the backend database.

Database contains:

- User Information
- Patient Details
- Health Records
- AI Prediction Results

---

# 🔒 Security Features

- User Login Authentication
- Role-Based Access Control
- Session Management
- Protected Routes
- Database Security

---

# 🚀 Future Enhancements

- Machine Learning Disease Prediction
- Cloud Database Integration
- SMS & Email Notifications
- Patient Mobile Application
- Real-Time IoT Health Monitoring
- Electronic Health Record Integration
- Data Visualization Dashboard
- Medical Report Generation
- Appointment Booking System
- Multi-Hospital Support

---

# 📸 Screenshots

- Login Page
- Admin Dashboard
- Doctor Dashboard
- Nurse Dashboard
- Patient Registration
- Patient List
- AI Prediction Result

---

# 📄 License

This project is developed for educational purposes as a final year academic project.

---

# 👩‍💻 Author

**Nithiya Babu**

Pre Final Year B.Tech. Artificial Intelligence and Data Science

VSB Engineering College, Karur

---

# 🙏 Acknowledgement

This project was developed as part of the Bachelor of Engineering curriculum to demonstrate the practical implementation of Artificial Intelligence, Web Development, Database Management, and Healthcare Information Systems.

---

## ⭐ Support

If you find this project useful, please consider giving it a ⭐ on GitHub.