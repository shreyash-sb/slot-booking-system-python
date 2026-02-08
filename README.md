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
├── booking_system.py  
├── active_bookings.json  
├── completed_bookings.json  
├── Screenshots/  
└── README.md

---

## How to Run the Project

1. Clone the repository:  
   git clone https://github.com/your-username/Slot-Booking-Reminder-System.git

2. Navigate to the project directory:  
   cd Slot-Booking-Reminder-System

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

## Sample Program Output

--- Create New Booking ---  
Enter customer name: Shri  
Enter phone number: 123456789  
Enter reason for booking: Servicing  
Enter date & time (YYYY-MM-DD HH:MM): 2026-02-08 09:45  
Booking created successfully.

--- Active Bookings ---  
ID: 5caaac | Name: Shri | Phone: 123456789 | Reason: Servicing | Time: 2026-02-08 09:45

--- Reminder Check ---  
Reminder: Shri | Reason: Servicing | Time: 2026-02-08 09:45 | Phone: 123456789

--- Completed Bookings ---  
ID: 5caaac | Name: Shri | Phone: 123456789 | Reason: Servicing | Time: 2026-02-08 09:45

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

Developed by: Shreyash Sitaram Bobalade  
PRN: 246109065
