from services.resource_service import *
from services.booking_service import *

while True:

    print("\n===== Smart Campus Resource Booking System =====")
    print("1. Add Resource")
    print("2. View Resources")
    print("3. Delete Resource")
    print("4. Book Resource")
    print("5. View Bookings")
    print("6. Delete Booking")
    print("7. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            name = input("Enter Resource Name: ")
            type = input("Enter Type: ")
            capacity = int(input("Enter Capacity: "))
            add_resource(name, type, capacity)

        elif choice == 2:
            view_resources()

        elif choice == 3:
            rid = int(input("Enter Resource ID: "))
            delete_resource_by_id(rid)

        elif choice == 4:
            user_id = int(input("Enter User ID: "))
            resource_id = int(input("Enter Resource ID: "))
            date = input("Enter Date (YYYY-MM-DD): ")
            time_slot = input("Enter Time Slot: ")
            book_resource(user_id, resource_id, date, time_slot)

        elif choice == 5:
            view_bookings()

        elif choice == 6:
            bid = int(input("Enter Booking ID: "))
            delete_booking_by_id(bid)

        elif choice == 7:
            print("Exiting...")
            break

        else:
            print("Invalid Choice")

    except ValueError:
        print("Please enter valid input")