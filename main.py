# main.py
# Main entry point for the Smart Canteen Ordering and Billing System.

from menu_display import welcome, line, pause, show_menu, category_menu, search_food, get_number
from order_processing import new_order
from billing_and_payment import show_order_history, sales_summary


def main_menu():
    while True:
        print()
        line()
        print("                    MAIN MENU")
        line()
        print("1. New Order")
        print("2. View Full Menu")
        print("3. View Categories")
        print("4. Search Food")
        print("5. Order History")
        print("6. Sales Summary")
        print("0. Exit")
        line()

        choice = get_number("Enter your choice: ")

        if choice == 1:
            new_order()
        elif choice == 2:
            show_menu()
            pause()
        elif choice == 3:
            category_menu()
        elif choice == 4:
            search_food()
        elif choice == 5:
            show_order_history()
        elif choice == 6:
            sales_summary()
        elif choice == 0:
            print()
            line()
            print("Thank you for visiting MAYURI!")
            print("Have a great day!")
            line()
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    welcome()
    main_menu()
    input("\nPress enter to exit...")
