# 🍽️ Smart Canteen Ordering and Billing System

A modular Python-based restaurant/canteen management system created from the original single-file program.

## 📁 Project Structure

```text
smart-canteen-ordering-and-billing-system/
│
├── main.py
├── menu_data.py
├── menu_display.py
├── order_processing.py
├── billing_and_payment.py
├── requirements.txt
├── README.md
└── statement.md
```

## ▶️ How to Run

Make sure Python 3 is installed.

```bash
python main.py
```

## ✨ Features

- New customer orders
- Dine-in and takeaway orders
- Full restaurant menu
- Menu categories
- Food search
- Shopping cart
- Add, remove and change item quantities
- Automatic discount calculation
- 5% GST calculation
- Cash, UPI and Card payment selection
- Automatic bill generation
- Order history
- Sales summary
- Payment-method statistics
- Best-selling item tracking

## 🧩 Module Responsibilities

| File | Purpose |
|---|---|
| `main.py` | Starts the program and controls the main menu |
| `menu_data.py` | Stores food names, prices, categories and runtime sales data |
| `menu_display.py` | Displays menus, categories and search results |
| `order_processing.py` | Handles customers, carts and order workflow |
| `billing_and_payment.py` | Handles billing, discounts, GST, payments and sales reports |
| `requirements.txt` | Lists project dependencies |
| `statement.md` | Project statement and module overview |

## 💰 Billing Logic

- ₹1000 or more → 5% discount
- ₹2000 or more → 7% discount
- ₹3000 or more → 10% discount
- GST → 5% after discount

## 🛠️ Technologies

- Python 3
- Dictionaries
- Lists
- Functions
- Loops
- Conditional statements
- Modular programming
- Basic input validation

## 👨‍💻 Project

**Smart Canteen Ordering and Billing System**

This project demonstrates how a larger Python program can be separated into logical modules while keeping the same core functionality.
