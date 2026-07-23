# 🎓 Student Management System on AWS

A cloud-based Student Management System deployed on AWS that allows users to manage student records through a web application. The project demonstrates how to host a web application on AWS using EC2 and connect it to a MySQL database.

---

## 📌 Project Overview

The Student Management System is a CRUD (Create, Read, Update, Delete) application that enables users to efficiently manage student information. It is deployed on an Amazon EC2 instance and uses a MySQL database to store student records.

This project demonstrates fundamental AWS cloud deployment concepts, including virtual servers, security groups, database connectivity, and web application hosting.

---

## 🚀 Features

- Add new student records
- View all student details
- Update existing student information
- Delete student records
- Responsive web interface
- Cloud deployment using AWS EC2
- MySQL database integration

---

## 🛠️ Tech Stack

- **Cloud Platform:** AWS
- **Compute Service:** Amazon EC2
- **Database:** MySQL
- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS, Bootstrap
- **Version Control:** Git & GitHub

---

## ☁️ AWS Services Used

- Amazon EC2
- Security Groups
- Elastic IP (optional)
- Amazon Linux / Ubuntu
- SSH for remote access

---

## 📂 Project Structure

```
Student-Management-System/
│
├── app.py
├── requirements.txt
├── database.sql
├── templates/
│   ├── index.html
│   ├── add_student.html
│   └── edit_student.html
├── static/
│   ├── css/
│   └── images/
├── README.md
└── screenshots/
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/student-management-system.git
```

### Navigate to the project

```bash
cd student-management-system
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure MySQL

Create a database and import the SQL file.

```sql
CREATE DATABASE studentdb;
```

Import:

```bash
mysql -u root -p studentdb < database.sql
```

### Run the application

```bash
python app.py
```

Visit:

```
http://localhost:5000
```

---

## ☁️ AWS Deployment Steps

1. Launch an EC2 instance.
2. Configure Security Groups (allow ports 22, 80, and 5000 if required).
3. Connect to EC2 using SSH.
4. Install Python, Flask, and MySQL.
5. Clone this repository.
6. Install project dependencies.
7. Configure the database connection.
8. Run the Flask application.
9. Access the application using the EC2 Public IP.

---

## 📸 Screenshots

Add screenshots here.

Example:

```
screenshots/
├── home.png
├── add-student.png
├── student-list.png
```

---

## 📖 Learning Outcomes

- AWS EC2 deployment
- Linux server management
- MySQL database connectivity
- Flask application hosting
- Security Group configuration
- GitHub version control
- CRUD application development

---

## 🔮 Future Enhancements

- Student authentication
- Admin dashboard
- Search and filter functionality
- File upload for student photos
- AWS RDS integration
- Docker containerization
- CI/CD pipeline using GitHub Actions

---

## 👩‍💻 Author

**Rakshitha M M**
---
