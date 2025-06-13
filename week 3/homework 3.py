# Exercise 1
name = input("Enter your name:")
hour = int(input("Enter the current hour (0-23):"))
if hour < 12:
    print(f"Good morning, {name}! Have a great day!")
elif hour >= 12 and hour <= 18:
    print(f"Good afternoon,{name}! Hope your day is going well!")
else:
    print("Good evening, {name}! Enjoy your evening!")

# Exercise 2
height = int(input("Enter your height in inches:"))
age = int(input("Enter your age:"))

if height >= 48 and age >= 10:
    print(f"You are {height} inches tall and {age} years old. you can ride!")
else:
    print("Sorry, you must be at least 48 inches tall and 10 years old to ride.")

# Exercise 3
temp= int(input("Do you want to convert (1) Fahrenheit to Celsius or (2) Celsius to Fahrenheit?"))
if temp == 1:
    degree_F = int(input("Enter temperature in Fahrenheit:"))
    Celsius = float((degree_F - 32) * (5/9))
    print(f"{degree_F} Fahrenheit is {Celsius:.2f} Celsius")
elif temp == 2:
    degree_C = int(input("Enter temperature in Celsius:"))
    Fahrenheit = (degree_C* 9/5) +32
    print(f"{degree_C} Celsius is {Fahrenheit:.2f} Fahrenheit")
else:
    print("Please enter 1 or 2")

# Exercise 4
total = int(input("Enter your total shopping amount:"))
if total >= 100:
    discount_total = total - (total * 0.1)
    print(f"Your discounted total is ${discount_total:.2f}.")
else:
    print(f"No discount applied. Your total shopping amount is ${total}.")

# Exercise 5
rent_day = int(input("Enter number of rental days:"))
daily_rent = 40
if rent_day >= 7:
    total_rent = (daily_rent * rent_day) - 50
    print(f"Your total rental cost is ${total_rent}.")
elif rent_day >= 3 and rent_day < 7:
    total_rent = (daily_rent* rent_day) - 20
    print(f"Your total rental cost is ${total_rent}.")
else:
    total_rent = (daily_rent * rent_day)
    print(f"Your total rental cost is ${total_rent}.")

# Exercise 6
age = int(input("Enter your age:"))
student = input("Are you a student? (y/n):")
membership = input("Do you want a month-to-month or annual membership?")

if (age < 18 or student == 'y') and membership == "month-to-month":
    print("You are eligible for a discounted membership of $20 per month")
elif (age < 18 or student == 'y') and membership == "annual":
    final_cost1 = 12*20*0.75
    print(f"Your discounted annual membership fee is ${final_cost1:.2f}")

elif (age >= 18 and student == 'n') and membership == "month-to-month":
    print("Your membership is $50 per month")

elif (age >= 18 and student == 'n') and membership == "annual":
    final_cost2 = 12*50*0.75
    print(f"Your discounted annual membership fee is ${final_cost2:.2f}")