#Q1
age = int(input("Please enter your age:"))
if age == 21 or age > 21:
    print("You are legal drinking age")
else:
    print("You are a minor. You can't drink")

#Q2
banned_users = ["Andrew", "Carole", "David"]
user = "Marie"
if user not in banned_users:
    print("Marie, you can post a response if you wish.")

#Q3
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
i = 0
sum = 0
for x in num_list:
    if x % 2:
        sum+= x
        i+= 1
        print(sum)
    if i == 5:
        break

#Q4
news_ticker= ''
headlines = []
for headlines in headlines:
    news_ticker = news_ticker + headlines + ""
    print(len(news_ticker))
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break
    print(len(news_ticker))
    print(news_ticker)

#Q5
import math
check_prime = [174, 73, 92, 145, 43, 29, 189, 182, 61, 126]
def prime_num(num):
    if num < 2:
        print(f"{num} is not a prime number")

#Q6
days_num = int(input("Enter the number of days"))
def readable_timedelta(days_num):
    weeks_num = days_num // 7
    remainder = days_num % 7
    print(f"{weeks_num} week(s) and {remainder} day(s)")
readable_timedelta(days_num)

#Q7
for x in range (0,i):
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print ("The number is divisible by 2")
    else:
        print("The number of not divisible by 2")
    break

#Q8
num1 = int(input("Enter a number: "))
def show_plus_ten(num1):
    print(num1 + 10)
show_plus_ten(num1)

num2 = int(input("Enter a number: "))
def add_ten(num2):
    return num2+ 10
print(add_ten(num2))

#Q9
def gain_weight(weight, increase):
    for x in range(1,52):
        weight += increase
        print(f"Week {x} is {weight}")
#Had to use float variable to allow decimal input
weight = float(input("Please enter your initial weight: "))
increase =  float(input("Please enter your weekly weight gain: "))
gain_weight(weight, increase)