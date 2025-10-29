#reversing a string
s='amazon'
print(s[::-1])

#count frequency of elements in list
arr=[1,2,2,2,3,3,3,3,3]
freq={}
for i in arr:
    freq[i]=freq.get(i,0)+1
print(freq)

#palindrome
word='Madam'
print(word.lower()==word[::-1].lower())

#list comprehension practice
squares=[i**2 for i in range(10) if i%2==0]
print(squares)

#simple class demo
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show(self):
        print(f"employee={self.name}, salary={self.salary}")
e1=Employee("Balaji",1900000)
e1.show()