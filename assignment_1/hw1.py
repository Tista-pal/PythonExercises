#Q1
#a) Create a list call planets with ['Earth', 'Moon', 'Venus', 'Mars', 'Mercury']
planets = ['Earth', 'Moon', 'Venus', 'Mars', 'Mercury']
#b) Print the planet at location 4
print(planets[3])
#c) Print the planet at location 2 to 4
print(planets[1:4])
#d) Add Jupiter to the end of the list and print the list
planets.append('Jupiter')
print(planets)
#e) Sort the planets in alphabetical order and print the list
planets.sort()
print(planets)
#f) Determine if Sun is in the list
if "Sun" in planets:
    print("Sun exists in the list")
else:
    print("Sun does not exist in the list")
#g) Sort the planets in the reverse order and print the list
planets.reverse()
print(planets)
#h) Determine the length of the list
print(len(planets))
#i) Add Jupiter to the beginning of the list without replacing existing item and print the list
planets.insert(0,"Jupiter")
print(planets)
#j) Remove the last planet in the list using pop() and print the list
planets.pop(6)
print(planets)
#k) Remove 1st location item planets[0] using del
del planets[0]
print(planets)
#l) Remove Mars using remove()
planets.remove("Mars")
print(planets)

#Q2
checking_balance = 1000
saving_balance = 1500
if checking_balance < 2000:
    checking_balance += 500
    saving_balance -= 500
print(checking_balance)
print(saving_balance)

#Q3
age = int(input("Please enter your age:"))
if age < 21:
    print("Illegal drinking age")
elif age > 65:
    print("Eligible for Medicare")
else:
    print("Keep Working")

#Q4
number1 = int(input("Please enter one number:"))
number2 = int(input("Please enter another number:"))
if number1 < number2:
    print(str(number2) + " is larger")
elif number1 > number2:
    print(str(number1) + " is larger")
elif number1 == number2:
    print(str(number1) + " and " + str(number2) + " are equal")

#Q5
number = input("Please enter 1 or 2:")
if number == "1":
    print("Hello World")
elif number == "2":
    print ("Python Rocks")
elif number != "1" or number !="2":
    print("You did not enter a valid number")

#Q6
perfect_list = (6, 28, 496, 8128, 33550336)
p_number = int(input("Please enter number"))
if p_number == 6 or p_number == 28 or p_number ==496 or p_number ==8128 or p_number ==33550336:
    print("You have entered a perfect number")
else:
    print("You have not entered a perfect number")

#Q7
user_number = int(input("Please enter a number:"))
if user_number % 2 == 0:
    print("Number " + str(user_number) + " is even.")
else:
    print("Number " + str(user_number) + " is odd.")

#Q8
dictionary = {"Rick Sanchez": 70, "Morty Smith": 35, "Summer Smith": 82, "Jerry Smith": 23, "Beth Smith": 98}
passing_score = 65
for stu in dictionary:
    if dictionary[stu] >= 65:
        print(str(stu) + " has passed")