import math
# 1. Store Discount with Multiple Conditions

total_price = int(input("Enter your total pruchase amount: "))
loyalty = input("Do you have a loyalty card? (y/n): ")

if total_price >= 100 and loyalty == 'y':
    final_price = total_price * 0.85
    print(f"Your final total after discounts is ${final_price}")

elif total_price < 100 and loyalty == 'n':
    final_price = (total_price)
    print(f"Your final total after discounts is ${final_price}")

elif total_price < 100 and loyalty == 'y':
    final_price = total_price * 0.95
    print(f"Your final total after discounts is ${final_price}")

elif total_price >= 100 and loyalty == 'n':
    final_price = total_price * 0.9
    print(f"Your final total after discounts is ${final_price}")

# 2. Employee Pay Calculation
hourly_wage = int(input("Enter hourly wage: "))
hours_worked = int(input("Enter hours worked: "))

if hours_worked > 40:
    regular_pay = round(hourly_wage * 40)
    overtime_pay = round((hours_worked - 40) * (1.5 * hourly_wage))
    total_pay = round(regular_pay + overtime_pay)
    print(f"Regular pay ${regular_pay:>5}")
    print(f"Overtime pay ${overtime_pay:>5}")
    print(f"Total pay ${total_pay:>5}")

elif hours_worked <= 40:
    regular_pay = round(hours_worked * hourly_wage)
    total_pay = round(regular_pay)
    print(f"Regular pay ${regular_pay:>5}")
    print(f"Total pay ${total_pay:>5}")

# 3. Restaurant Bill Calculator
bill_total = int(input("Enter your bill total: "))
tip = input("Would you like to leave a tip? (y/n): ")
if tip == 'y':
    tip_percent = int(input("Enter tip percentage: "))
    subtotal = round(bill_total)
    tip_amount = round(bill_total*(tip_percent/100))
    sales_tax = round(bill_total * 0.08)
    grand_total = round(subtotal + tip_amount + sales_tax)
    print(f"Subtotal ${subtotal:.>7}")
    print(f"Tip ({tip_percent}%) ${tip_amount:.>5}")
    print(f"Sales Tax (8%) ${sales_tax:.>3}")
    print(f"Grant Total ${grand_total:.>4}")
elif tip == 'n':
    subtotal = bill_total
    grand_total = subtotal
    print(f"Subtotal ${subtotal:.>7}")
    print(f"Grant Total ${grand_total:.>3}")

# 4. Product Purchase Calculator
apple = int(input("Enter quantity of apples: "))
banana = int(input("Enter quantity of bananas: "))
orange = int(input("Enter quantity of oranges: "))
grape = int(input("Enter quantity of grapes (lbs): "))

apple_price = int(apple * 1.5)
banana_price = int(banana * 0.75)
orange_price = int(orange * 1.25)
grape_price = int(grape * 3)

subtotal = round(apple_price + banana_price + orange_price + grape_price)
sales_tax = round(subtotal * 0.08)
grand_total = round(subtotal + sales_tax)

print(f"Apple {apple:.>7} ${apple_price:.>13}")
print(f"Banana {banana:.>7} ${banana_price:.>13}")
print(f"Orange {orange:.>7} ${orange_price:.>13}")
print(f"Grape {grape:.>7} ${grape_price:.>13}")

print(f"Subtotal ${subtotal:.>4}")
print(f"Sales Tax (8%) ${sales_tax:.>3}")
print(f"Grand Total ${grand_total:.>5}")