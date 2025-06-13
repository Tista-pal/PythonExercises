variable = 8
if variable <10:
        print("This is true")
        soda = input("What's your favorite soda?")
        if soda == "Mountain Dew":
            print("you are correct")
            print("line 2")
            flavor = input("What flavor of mountain dew?")
            if flavor == "original":
                print("yup")
            else:
                print("nope")
        else:
            print("you are wrong")
else:
    print("this is not true")

####

age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote")
    if age >= 21:
        print("you can drink")
else:
    print("You are too young to drink or vote")

####

role = input("are you logging in as an admin or user?")
if role == "admin":
    password = input("Enter the password: ")
    if password == "Password1":
        print("Welcome to the admin portal")
    else:
        print("Print incorrect password")
else:
    print("Welcome to our application")

##### and or
if 8 == 10 or 10 == 15 or 10 == 10:
    print("True")

age = int(input("What is your age? "))
dl = input("Do you have a driver's license (y/n) ")

if age >= 25 and dl == 'y':
    print("You are eligible to rent this vehicle")
else:
    print("You are not eligible to rent this vehicle")

weekend = input("is it a weekend? (y/n)")
holiday = input("is it a holiday? (y/n)")

if weekend == "y" or holiday == 'y':
    print("You can sleep in")
else:
    print("WAKE UP")

cost = 5
print(cost)
cost = 10
print(cost)

cost = cost + 5
print(cost)

#hamburger = 5, soda = 2, fries = 3, ice cream = 4

cost = 0

hamburger = input("Would you like a hamburger? (y/n) ")
if hamburger == "y":
    cost = cost + 5
    print(f"Total cost is currently ${cost}")

fries = input("Would you like a fries? (y/n) ")
if fries == "y":
    cost = cost + 3
    print(f"Total cost is currently ${cost}")

soda = input("Would you like a soda? (y/n) ")
if soda == "y":
    cost = cost + 2
    print(f"Total cost is currently ${cost}")

ice_cream = input("Would you like a ice cream? (y/n) ")
if ice_cream == "y":
    cost = cost + 4
    print(f"Total cost is currently ${cost}")

#### alignment > < ^
name1 = "Alice"
name2 = "Bob"
phone1 = "1234556789"
phone2 = "987654321"
print(f"{name1:-<10},{phone1:->15}")
print(f"{name2:<10},{phone2:>15}")