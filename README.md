# Slot Booking and Reminder System

A console-based Python application for managing slot bookings and providing reminders for upcoming appointments.  
This project is developed as an academic/internship project to demonstrate file handling and date-time operations using Python.

---

## Features

- Create new bookings with name, phone number, reason for booking, date and time
- View all active bookings
- Reminder check for bookings within the next 15 minutes
- Mark bookings as completed
- Delete cancelled bookings
- Search bookings by name, phone number, or reason
- Data storage using JSON files
- Menu-driven console interface

---

## Technologies Used

- Python 3.x
- JSON (for data storage)
- datetime module
- UUID for unique booking IDs

---

## Project Structure

Slot-Booking-Reminder-System/  
├── src/  
│ └── booking_system.py  
├── data/  
│ ├── active_bookings.json  
│ └── completed_bookings.json  
├── docs/  
│ └── screenshots/  
├── README.md  
├── requirements.txt  
└── .gitignore

---

## How to Run the Project

1. Clone the repository:  
   git clone https://github.com/your-username/Slot-Booking-Reminder-System.git

2. Navigate to the project directory:  
   cd Slot-Booking-Reminder-System/src

3. Run the program:  
   python booking_system.py

---

## Sample Menu Output

====== SLOT BOOKING SYSTEM ======

1. New Booking
2. View Bookings
3. Reminder Check
4. Complete Booking
5. Delete Booking
6. Search Booking
7. View Completed Bookings
8. Exit

---

## How the System Works

1. The user creates a booking by entering name, phone number, reason for booking, and appointment time.
2. Booking information is saved in a JSON file for permanent storage.
3. The reminder system compares the current system time with the booking time.
4. If a booking is within the next 15 minutes, a reminder message is displayed.
5. Completed bookings are moved to a separate file for record keeping.
6. Cancelled bookings can be deleted from the system.
7. Users can search bookings using name, phone number, or reason.

---

## Future Enhancements

- Email or SMS reminder system
- Graphical User Interface (GUI) using Tkinter
- Database integration (MySQL)
- User authentication system
- Export booking reports to CSV or PDF

---

Developed by:Shreyash Sitaram Bobalade
Prn:246109065
