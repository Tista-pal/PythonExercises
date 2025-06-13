#Exercise 1 The Pizza Party
num_ppl = int(input("How many people are at the party?"))
num_pizza = int(input("How many pizzas have you order ordered?"))
num_slices = int(input("How many slices in each pizza?"))
total_slices = (num_pizza*num_slices)
slices_person = total_slices//num_ppl
leftovers = total_slices%num_ppl

print("There are", num_ppl, "at the party.")
print("You ordered", num_pizza, "pizzas with", num_slices, "slices each.")
print("Each person gets", slices_person)
print("There are", leftovers, "slices left over.")

#Exercise 2 The Travel Calculator
distance = int(input(print("How far are you traveling?")))
fuel = int(input(print("What is your car's fuel efficiency?")))
current_price = float(input(print("What is the current price of gas per gallon for your car?")))

trip_cost = (distance/fuel)*current_price

print("You are traveling", distance, "miles.")
print("Your car gets", fuel, "miles per gallon")
print("Gas costs $", current_price, "per gallon.")
print("Your trip will cost $", trip_cost, ".")

#Exercise 3 The Candy Store
price = float((input(print("What is the price of one piece of candy?"))))
num_candy = int(input(print("How many pieces of candy do you want to buy?")))
total_cost = price*num_candy

print("Each piece of candy costs $", price, ".")
print("You want to buy", num_candy, "pieces.")
print("The total cost is $", total_cost, ".")

#Exercise 4 Age in Dog Years
age = int(input(print("How old are you?")))
dog_years = 7*age

print("You are", age, "years old.")
print("In dog years, you are", dog_years, "years old")

#Exercise 5 The Discounted Price
orig_price = int(input(print("What is the original price of the item?")))
discount = int(input(print("What is the discount percentage?")))
final_price = orig_price - (orig_price*(discount/100))

print("The original price is $", orig_price, ".")
print("The discount is", discount ,"%.")
print("The discounted price is $", final_price, ".")