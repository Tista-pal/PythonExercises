#Q1
s = input("Please enter a sentence: ")
words = s.split()
words.sort(key=str.lower)
print("The sorted words are: ")
for word in words:
    print(word)

#Q2
x = int(input("Please enter a number between 40 and 50: "))
y = int(input("Please enter a number between 80 and 100: "))
while (x >= 40 and x<=50) and (y >= 80 and y <= 100):
    x+= 1
    y+= 1
print(x,y)

#Q3
import random
rand_nums = [random.randint(1,100) for _ in range(10)]
print(f"Random numbers:{rand_nums}")
for num in rand_nums:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

#Q4
import math
check_prime= [26,39,51,7,53,57,79,85]
def prime_num(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
        return True
for i in check_prime:
    if prime_num(i):
        print(f"{i} is a prime number")
    else:
        print(f"{i} is NOT a prime number")

#Q5
def sum_of_numbers(num):
    sum = 0
    i = 1
    while i <= num:
        sum+=i
        i+=1
    return sum
result = sum_of_numbers(10)
print(f"The result should be {result}")