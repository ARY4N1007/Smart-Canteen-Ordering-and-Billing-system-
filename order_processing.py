# order_processing.py
# Customer details, cart operations and the new-order workflow.

from menu_data import names, prices
from menu_display import (
    line, small_line, pause, get_number, get_text,
    item_header, item_row, show_menu, category_menu, search_food
)
from billing_and_payment import (
    calculate_total, show_discount, payment_method, print_bill
)


def customer_details():
    print()
    line()
    print("                 CUSTOMER DETAILS")
    line()

    customer_name = get_text("Enter your name: ")

    while True:
        phone = input("Enter your phone number: ")
        if phone.isdigit() and len(phone) == 10:
            break
        print("Phone number must be 10 digits.")

    print()
    print("1. Dine-in")
    print("2. Takeaway")

    choice = get_number("Choose order type: ")

    if choice == 1:
        order_type = "Dine-in"
        table = get_text("Enter table number: ")
    elif choice == 2:
        order_type = "Takeaway"
        table = "N/A"
    else:
        print("Invalid choice. Takeaway selected.")
        order_type = "Takeaway"
        table = "N/A"

    return customer_name, phone, order_type, table


def add_item(cart):
    choice = get_number("Enter item number (0 to go back): ")

    if choice == 0:
        return

    if choice not in names:
        print("Invalid item number.")
        return

    print()
    print("Item :", names[choice])
    print("Price: ₹", prices[choice])

    quantity = get_number("Enter quantity: ")

    if quantity <= 0:
        print("Invalid quantity.")
        return

    if choice in cart:
        cart[choice] += quantity
    else:
        cart[choice] = quantity

    print()
    print(quantity, names[choice], "added to cart.")


def show_cart(cart):
    print()
    line()
    print("                    YOUR CART")
    line()

    if len(cart) == 0:
        print("Your cart is empty.")
        line()
        return

    print(f"{'No.':<5}{'Item':<22}{'Qty':>5}{'Price':>10}{'Amount':>10}")
    small_line()

    total = 0

    for item in cart:
        quantity = cart[item]
        amount = prices[item] * quantity
        total += amount

        print(
            f"{item:<5}"
            f"{names[item]:<22}"
            f"{quantity:>5}"
            f"{'₹' + str(prices[item]):>10}"
            f"{'₹' + str(amount):>10}"
        )

    small_line()
    print(f"{'Cart Total':<42}₹{total:>8.2f}")
    line()


def remove_item(cart):
    if len(cart) == 0:
        print("Your cart is empty.")
        return

    show_cart(cart)
    choice = get_number("Enter item number to remove: ")

    if choice not in cart:
        print("Item is not in your cart.")
        return

    del cart[choice]
    print("Item removed successfully.")


def change_quantity(cart):
    if len(cart) == 0:
        print("Your cart is empty.")
        return

    show_cart(cart)
    choice = get_number("Enter item number to change: ")

    if choice not in cart:
        print("Item is not in your cart.")
        return

    print("Current quantity:", cart[choice])
    new_quantity = get_number("Enter new quantity: ")

    if new_quantity <= 0:
        print("Invalid quantity. Use Remove Item instead.")
        return

    cart[choice] = new_quantity
    print("Quantity updated.")


def new_order():
    customer_name, phone, order_type, table = customer_details()
    cart = {}

    while True:
        print()
        line()
        print("                    ORDER MENU")
        line()
        print("1. Add Item")
        print("2. View Cart")
        print("3. Remove Item")
        print("4. Change Quantity")
        print("5. Search Food")
        print("6. View Categories")
        print("7. Finish Order")
        print("0. Cancel Order")
        line()

        choice = get_number("Enter your choice: ")

        if choice == 1:
            show_menu()
            add_item(cart)

        elif choice == 2:
            show_cart(cart)

        elif choice == 3:
            remove_item(cart)

        elif choice == 4:
            change_quantity(cart)

        elif choice == 5:
            search_food()

        elif choice == 6:
            category_menu()

        elif choice == 7:
            if len(cart) == 0:
                print("Your cart is empty.")
                continue

            show_cart(cart)
            show_discount(calculate_total(cart))
            confirm = input("Continue to billing? (y/n): ").lower()

            if confirm == "y":
                payment = payment_method()
                print_bill(
                    cart, customer_name, phone,
                    order_type, table, payment
                )
                break

        elif choice == 0:
            print("Order cancelled.")
            break

        else:
            print("Invalid choice.")
