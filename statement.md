# Project Statement

## Title
**Smart Canteen Ordering and Billing System**

## Objective
The objective of this project is to develop a menu-driven restaurant management system in Python that can handle food selection, customer details, cart operations, billing, payment selection and basic sales reporting.

## Main Modules

### 1. Menu Data
Stores:
- Food names
- Prices
- Categories
- Order history
- Item sales data

### 2. Menu Display
Handles:
- Welcome screen
- Full menu
- Category display
- Food search
- Input validation helpers

### 3. Order Processing
Handles:
- Customer details
- Dine-in/takeaway selection
- Adding items
- Removing items
- Changing quantities
- Viewing the cart
- Completing or cancelling orders

### 4. Billing and Payment
Handles:
- Discount calculation
- GST calculation
- Payment method
- Bill generation
- Order history
- Sales summary

## Program Flow

```text
Start
  ↓
Welcome Screen
  ↓
Main Menu
  ├── New Order
  │     ├── Customer Details
  │     ├── Add / Remove / Change Items
  │     ├── Search / Categories
  │     └── Billing & Payment
  │
  ├── View Full Menu
  ├── View Categories
  ├── Search Food
  ├── Order History
  ├── Sales Summary
  └── Exit
```

## Conclusion

The original restaurant program has been organized into separate Python modules so that the project is easier to read, maintain, test and present on GitHub. The modules communicate through imports while the overall menu-driven functionality remains intact.
