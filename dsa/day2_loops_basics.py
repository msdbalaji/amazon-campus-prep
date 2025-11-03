#example 1 - print numbers from 1 to 5
for i in range(1, 6):
    print(i)

#example 2 - sum of numbers 1-n
n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    total = total + i
print("Sum =", total)

#example 3 - print squares of first 5 numbers
for i in range(1, 6):
    print(i, "square is", i*i)

#example 4 - reverse loop
for i in range(5, 0, -1):
    print(i)


#coding exercise for day 2 loops basics
'''
1️⃣ Print all numbers from 1 to 10.
2️⃣ Print all even numbers between 1 and 20.
3️⃣ Input n and print the sum of all odd numbers up to n.

answer and explanation in notes day2
'''