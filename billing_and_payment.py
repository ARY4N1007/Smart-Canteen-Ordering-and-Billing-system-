# billing_and_payment.py
# Payment selection, billing, GST/discount calculation and sales reporting.

from menu_data import names, prices, order_history, item_sales
from menu_display import line, small_line, get_number, pause


def calculate_total(cart):
    total = 0
    for item in cart:
        total += prices[item] * cart[item]
    return total


def discount_percent(total):
    if total >= 3000:
        return 10
    elif total >= 2000:
        return 7
    elif total >= 1000:
        return 5
    return 0


def show_discount(total):
    percent = discount_percent(total)

    if percent > 0:
        print("You received a", percent, "% discount!")
    else:
        print("No discount available.")
        print("Order ₹", 1000 - total, "more to get a 5% discount.")


def payment_method():
    print()
    line()
    print("                 PAYMENT METHOD")
    line()
    print("1. Cash")
    print("2. UPI")
    print("3. Card")

    choice = get_number("Choose payment method: ")

    if choice == 2:
        return "UPI"
    elif choice == 3:
        return "Card"
    elif choice != 1:
        print("Invalid choice. Cash selected.")

    return "Cash"


def print_bill(cart, customer_name, phone, order_type, table, payment):
    total = calculate_total(cart)
    discount = total * discount_percent(total) / 100
    after_discount = total - discount
    gst = after_discount * 5 / 100
    grand_total = after_discount + gst
    order_id = 1001 + len(order_history)

    print()
    line()
    print("                 SMART CANTEEN")
    print("                      BILL")
    line()
    print("Order ID :", order_id)
    print("Customer :", customer_name)
    print("Phone    :", phone)
    print("Order    :", order_type)
    print("Table    :", table)
    small_line()
    print(f"{'Item':<22}{'Qty':>5}{'Price':>10}{'Amount':>12}")
    small_line()

    for item in cart:
        quantity = cart[item]
        amount = prices[item] * quantity

        print(
            f"{names[item]:<22}"
            f"{quantity:>5}"
            f"{'₹' + str(prices[item]):>10}"
            f"{'₹' + str(amount):>12}"
        )

        item_sales[item] = item_sales.get(item, 0) + quantity

    small_line()
    print(f"{'Subtotal':<37}₹{total:>10.2f}")
    print(f"{'Discount':<37}-₹{discount:>9.2f}")
    print(f"{'After Discount':<37}₹{after_discount:>10.2f}")
    print(f"{'GST (5%)':<37}₹{gst:>10.2f}")
    line()
    print(f"{'GRAND TOTAL':<37}₹{grand_total:>10.2f}")
    line()
    print("Payment Method:", payment)
    line()
    print("Thank you for visiting MAYURI!")
    print("Please visit again!")
    line()

    order_history.append({
        "order_id": order_id,
        "customer": customer_name,
        "type": order_type,
        "gst": gst,
        "total": grand_total,
        "payment": payment
    })


def show_order_history():
    print()
    line()
    print("                  ORDER HISTORY")
    line()

    if len(order_history) == 0:
        print("No orders have been placed yet.")
        line()
        pause()
        return

    print(f"{'Order ID':<11}{'Customer':<17}{'Type':<10}{'Payment':<9}{'Total':>8}")
    small_line()

    for order in order_history:
        print(
            f"{order['order_id']:<11}"
            f"{order['customer']:<17}"
            f"{order['type']:<10}"
            f"{order['payment']:<9}"
            f"₹{order['total']:>7.2f}"
        )

    line()
    pause()


def sales_summary():
    print()
    line()
    print("                   SALES SUMMARY")
    line()

    total_orders = len(order_history)
    total_sales = 0
    total_gst = 0

    for order in order_history:
        total_sales += order["total"]
        total_gst += order["gst"]

    print("Total Orders :", total_orders)
    print(f"Total Sales  : ₹{total_sales:.2f}")
    print(f"Total GST    : ₹{total_gst:.2f}")

    if total_orders > 0:
        print(f"Average Bill : ₹{total_sales / total_orders:.2f}")
        print()
        print("Payments received:")

        for method in ["Cash", "UPI", "Card"]:
            count = 0
            for order in order_history:
                if order["payment"] == method:
                    count += 1
            print(f"  {method:<5}:", count)

        best_item = 0
        best_quantity = 0

        for item in item_sales:
            if item_sales[item] > best_quantity:
                best_quantity = item_sales[item]
                best_item = item

        if best_item:
            print()
            print("Best seller  :", names[best_item])
            print("Sold         :", best_quantity)
    else:
        print("Average Bill : ₹0.00")

    line()
    pause()
