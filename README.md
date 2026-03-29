# Hackthon
# Smart Campus Resource Booking and Utilization Application

##  Project Title

Smart Campus Resource Booking and Utilization System

---

## Project Description

The Smart Campus Resource Booking and Utilization Application is a web-based system designed to help students, faculty, and administrators efficiently book and manage campus resources such as classrooms, labs, seminar halls, and equipment. The system prevents scheduling conflicts, improves transparency, and ensures optimal utilization of campus infrastructure.

This project is ideal for demonstrating full-stack development skills using Python, MySQL, HTML, and CSS.

---

##  Objectives

* Provide an easy platform for booking campus resources
* Avoid double-booking of rooms and equipment
* Enable administrators to manage resources efficiently
* Track resource utilization history
* Improve communication between users and administrators

---

##  Users of the System

1. Admin
2. Students
3. Faculty

Each user has different access permissions.

---

##  Features

### Admin Module

* Add new resources (labs, classrooms, seminar halls)
* Update resource availability
* Approve or reject booking requests
* View booking reports
* Manage users

###  Student Module

* Register/Login
* View available resources
* Book resources
* Cancel bookings
* View booking history

### Faculty Module

* Login
* Request resource booking
* View approval status
* Access booking reports

---

## Technologies Used

### Frontend

* HTML
* CSS

### Backend

* Python

### Database

* MySQL

### Tools

* VS Code
* GitHub

---

##  Database Tables

### Users Table

* user_id (Primary Key)
* name
* email
* password
* role

### Resources Table

* resource_id (Primary Key)
* resource_name
* resource_type
* availability_status

### Bookings Table

* booking_id (Primary Key)
* user_id (Foreign Key)
* resource_id (Foreign Key)
* booking_date
* time_slot
* status

---

##  System Workflow

1. User registers/logs into the system
2. User checks available resources
3. User selects date and time slot
4. Booking request submitted
5. Admin approves/rejects request
6. Booking confirmation shown to user

---

## Advantages

* Saves time
* Prevents manual booking errors
* Improves transparency
* Easy resource tracking
* Centralized management system

---

##  Future Enhancements

* Email notifications for booking confirmation
* Mobile application support
* AI-based smart scheduling suggestions
* QR-based resource access system
* Dashboard analytics for admins

---

##  Sample Screens 
WElcome page
<img width="800" height="404" alt="Screenshot 2026-03-28 035333" src="https://github.com/user-attachments/assets/ae553bac-173e-435e-89ed-9278081ea05f" />


Login Page
<img width="522" height="643" alt="Screenshot 2026-03-28 035358" src="https://github.com/user-attachments/assets/00798432-0529-4580-bc58-5a9aa126ed11" />

Dashboard Page
<img width="1860" height="896" alt="Screenshot 2026-03-28 035426" src="https://github.com/user-attachments/assets/41ab2e4e-6132-453c-bb96-500bf5c397ea" />


##  Installation Steps

### Step 1: Clone Repository

```
git clone https://github.com/your-username/smart-campus-booking.git
```

### Step 2: Navigate to Project Folder

```
cd smart-campus-booking
```

### Step 3: Install Dependencies

```
pip install -r requirements.txt
```

### Step 4: Setup Database

* Open MySQL
* Create database
* Import database.sql file

### Step 5: Run Application

```
python main.py
```

---

##
