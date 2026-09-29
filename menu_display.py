# menu_display.py
# Functions responsible for displaying menus and collecting simple input.

from menu_data import names, prices, categories


def line():
    print("=" * 55)


def small_line():
    print("-" * 55)


def pause():
    input("\nPress Enter to continue...")


def get_number(message):
    while True:
        text = input(message)
        if text.isdigit():
            return int(text)
        print("Please enter a number only.")


def get_text(message):
    while True:
        text = input(message).strip()
        if text != "":
            return text
        print("This cannot be empty.")


def item_header():
    print(f"{'No.':<5}{'Item':<27}{'Price':>10}")
    small_line()


def item_row(i):
    print(f"{i:<5}{names[i]:<27}₹{prices[i]:>8}")


def welcome():
    line()
    print("                 SMART CANTEEN")
    print("             SMART CANTEEN SYSTEM")
    line()
    print("Welcome to Smart Canteen Ordering and Billing System!")
    print("Good food, great taste!")
    line()


def show_menu():
    print()
    line()
    print("                    FULL MENU")
    line()
    item_header()
    for i in names:
        item_row(i)
    line()


def show_categories():
    print()
    line()
    print("                    CATEGORIES")
    line()
    number = 1
    for category in categories:
        print(number, ".", category)
        number += 1
    print("0 . Back")
    line()


def category_menu():
    while True:
        show_categories()
        choice = get_number("Choose a category: ")

        if choice == 0:
            break

        category_names = list(categories.keys())
        if choice > len(category_names):
            print("Invalid category.")
            continue

        category = category_names[choice - 1]
        print()
        line()
        print(category.upper())
        line()
        item_header()

        for item in categories[category]:
            item_row(item)

        line()
        pause()


def search_food():
    print()
    line()
    print("                    SEARCH FOOD")
    line()

    search = input("Enter food name: ").lower()
    found = False

    print()
    for item in names:
        if search in names[item].lower():
            item_row(item)
            found = True

    if not found:
        print("No matching food item found.")

    line()
    pause()
