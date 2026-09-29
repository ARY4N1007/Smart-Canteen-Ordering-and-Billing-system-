# menu_data.py
# All restaurant menu data and runtime order data.

names = {
    1: "Combo Shahi Thali", 2: "Samosa", 3: "Vada Pav",
    4: "Chicken 65", 5: "Paneer Tikka", 6: "Achari Paneer",
    7: "Paneer Butter Masala", 8: "Chole Bhature", 9: "Rajma",
    10: "Pav Bhaji", 11: "Dal Makhani", 12: "Malai Kofta",
    13: "Palak Paneer", 14: "Butter Chicken", 15: "Chicken Biryani",
    16: "Chicken Curry", 17: "Veg Biryani", 18: "Veg Fried Rice",
    19: "Tandoor Roti", 20: "Aloo Parantha", 21: "Masala Dosa",
    22: "Idli Sambhar", 23: "Gulab Jamun", 24: "Rasmalai",
    25: "Brownie", 26: "Ice Cream", 27: "Fresh Juice",
    28: "Cold Coffee", 29: "Masala Chai", 30: "Cold Drink"
}

prices = {
    1: 1200, 2: 55, 3: 60, 4: 220, 5: 180, 6: 380,
    7: 350, 8: 150, 9: 120, 10: 350, 11: 220, 12: 300,
    13: 270, 14: 420, 15: 350, 16: 380, 17: 280, 18: 200,
    19: 180, 20: 120, 21: 350, 22: 150, 23: 50, 24: 120,
    25: 150, 26: 100, 27: 100, 28: 130, 29: 50, 30: 60
}

categories = {
    "Combo": [1],
    "Starters": [2, 3, 4, 5],
    "Main Course": [6, 7, 8, 9, 10, 11, 12, 13, 14, 16],
    "Rice & Biryani": [15, 17, 18],
    "Breads": [19, 20],
    "South Indian": [21, 22],
    "Desserts": [23, 24, 25, 26],
    "Beverages": [27, 28, 29, 30]
}

# Runtime data. These remain in memory while the program is running.
order_history = []
item_sales = {}
