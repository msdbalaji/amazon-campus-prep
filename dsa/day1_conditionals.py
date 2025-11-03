#1.check if a number is odd or even
num=int(input("type a number"))
if num%2==0: 
    print("even") 
else: print("odd")

#2.Check if a year is a leap year
year = int(input("Enter a year: "))

if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
    print("Leap year")
else:
    print("Not a leap year")

#3.Input three numbers and print the largest
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Largest number is:", a)
elif b > c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)

#4.Take marks of 5 subjects and print grade
m1 = int(input("Enter mark 1: "))
m2 = int(input("Enter mark 2: "))
m3 = int(input("Enter mark 3: "))
m4 = int(input("Enter mark 4: "))
m5 = int(input("Enter mark 5: "))

avg = (m1 + m2 + m3 + m4 + m5) / 5

if avg >= 90:
    grade = 'A'
elif avg >= 75:
    grade = 'B'
elif avg >= 60:
    grade = 'C'
else:
    grade = 'Fail'

print("Average:", avg)
print("Grade:", grade)

#5.check vowel/consonant
ch = input("Enter a character: ").lower()

if ch in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")