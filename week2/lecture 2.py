#Paranthesis, Exponents, Multiplication, Division, Addition, Subtraction

((7+9)/2) * 3
print(75%7)

num1 = 7
num2 = 6
sum = num1 + num2

print(sum)

width = 5
height = 10
area = width + height
perimeter = width * 2 + height * 2
print("The area of the rectangle with a width of", width, "and a height of", height, "is", area)

print("The perimeter of the rectangle is: ", perimeter)

#Sarah buys 3 apples at $1.50 each and 2 bananas at $0.75 each. She also has to pay a flat bag fee of $1. Calculate her total cost.
apple_count = 3
apple_cost = 1.5
banana_count = 2
banana_cost = 0.75
bag_fee = 1

#total_apple_cost = apple_cost * apple_count
#total_banana_cost = banana_cost * banana_count
#total_cost = total_apple_cost + total_banana_cost + bag_fee

#print("Total cost is $", total_cost)

#Variables integer, float, string
#
#print(type(apple_cost))

#var = 1
#print(var,type(var))
# var = 2.1
# print(var, type(var))
# var = "5.1"
# print(var, type(var))

#name = input("Please tell me your name: ")
#print("Hello", name, ", nice to meet you")

#print(type(name))

#first_name = input("What's your first name: ")
#last_name = input("What's your last name: ")
#movie = input("What's your favorite movie? ")
#print("Hello", first_name, last_name, "I like the movie ", movie, "Also")

#int() # converts the inside to an integer
#float() # converts the inside of a float
#str() # converts the inside to a string

width = int(input("What's the width of your rectangle? "))
height = int(input("What's the height of your rectangle? "))
area = width * height
perimeter = width * 2 + height * 2
print("The area of the rectangle with a width of", width, "and a height of", height, "is", area)

print("The perimeter of the rectangle is: ", perimeter)

# Ask the user what's their name and age. The print back say "Hello <name> in 5 years you will be <age + 5>, years old"
name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name, "in 5 years you will be", age + 5, "years old")