import json
import os
from datetime import datetime, timedelta
import uuid

DATA_FILE = "active_bookings.json"
DONE_FILE = "completed_bookings.json"


def load_file(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return []


def save_file(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


class BookingManager:

    def __init__(self):
        self.active = load_file(DATA_FILE)
        self.completed = load_file(DONE_FILE)

    def create_booking(self):
        print("\n--- Create New Booking ---")
        name = input("Enter customer name: ").strip()
        phone = input("Enter phone number: ").strip()
        reason = input("Enter reason for booking: ").strip()
        time_input = input("Enter date & time (YYYY-MM-DD HH:MM): ").strip()

        try:
            slot_time = datetime.strptime(time_input, "%Y-%m-%d %H:%M")
            if slot_time <= datetime.now():
                print("Time must be in the future.")
                return
        except ValueError:
            print("Invalid date/time format.")
            return

        booking = {
            "id": str(uuid.uuid4())[:6],
            "name": name,
            "phone": phone,
            "reason": reason,
            "time": time_input
        }

        self.active.append(booking)
        save_file(DATA_FILE, self.active)
        print("Booking created successfully.")

    def show_bookings(self):
        print("\n--- Active Bookings ---")
        if not self.active:
            print("No bookings found.")
            return

        for b in self.active:
            print(f"ID: {b['id']} | Name: {b['name']} | Phone: {b['phone']} | "
                  f"Reason: {b['reason']} | Time: {b['time']}")

    def reminder_check(self):
        print("\n--- Reminder Check ---")
        now = datetime.now()
        found = False

        for b in self.active:
            booking_time = datetime.strptime(b["time"], "%Y-%m-%d %H:%M")
            diff = booking_time - now

            if timedelta(minutes=0) < diff <= timedelta(minutes=15):
                print(f"Reminder: {b['name']} | Reason: {b['reason']} | "
                      f"Time: {b['time']} | Phone: {b['phone']}")
                found = True

        if not found:
            print("No upcoming slots in next 15 minutes.")

    def complete_booking(self):
        self.show_bookings()
        bid = input("Enter Booking ID to mark as completed: ").strip()

        for b in self.active:
            if b["id"] == bid:
                self.completed.append(b)
                self.active.remove(b)
                save_file(DATA_FILE, self.active)
                save_file(DONE_FILE, self.completed)
                print("Booking marked as completed.")
                return

        print("Booking ID not found.")

    def delete_booking(self):
        self.show_bookings()
        bid = input("Enter Booking ID to delete: ").strip()

        for b in self.active:
            if b["id"] == bid:
                self.active.remove(b)
                save_file(DATA_FILE, self.active)
                print("Booking deleted.")
                return

        print("Booking ID not found.")

    def search_booking(self):
        key = input("Enter name / phone / reason to search: ").strip().lower()
        found = False

        for b in self.active:
            if (key in b["name"].lower() or 
                key in b["phone"] or 
                key in b["reason"].lower()):
                print(b)
                found = True

        if not found:
            print("No matching booking found.")

    def show_completed(self):
        print("\n--- Completed Bookings ---")
        if not self.completed:
            print("No completed slots yet.")
            return

        for b in self.completed:
            print(b)


def main():
    manager = BookingManager()

    while True:
        print("\n====== SLOT BOOKING SYSTEM ======")
        print("1. New Booking")
        print("2. View Bookings")
        print("3. Reminder Check")
        print("4. Complete Booking")
        print("5. Delete Booking")
        print("6. Search Booking")
        print("7. View Completed Bookings")
        print("8. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            manager.create_booking()
        elif choice == "2":
            manager.show_bookings()
        elif choice == "3":
            manager.reminder_check()
        elif choice == "4":
            manager.complete_booking()
        elif choice == "5":
            manager.delete_booking()
        elif choice == "6":
            manager.search_booking()
        elif choice == "7":
            manager.show_completed()
        elif choice == "8":
            print("Program terminated.")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()