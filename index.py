from math import floor
from operator import truediv

my_variable = "Ines"
my_num= 1 + 1
array = [1,2,3,4]
my_object = {'name' : 'Ines'}
my_float = 1.5

# print(my_variable[-1])
# print(my_variable[0])
# print(my_num)
# print(len(array))

def sum_odd_numbers(items):
    result = 0

    for num in items :
        if num % 2 == 0 :
            result+=num
        else :
            result*=num
    return result

print(sum_odd_numbers(array))

print(f"Hello {my_num}") #f for format

myself = {
    "name": "Ines",
    "age": 32,
    "city": 'Marseille',
}

name, age, city = myself["name"], myself["age"], myself["city"]


print(f"My name is {myself['name']}, I am {myself['age']} years old and I live in {myself['city']}")
print(f"My name is {name}, I am {age} years old and I live in {city}")

if city == "Paris" or (age == 35 and name == 'Ines'):
    print("oui")
elif city == "Marseille" and name == 'Coucou':
    print("non")
else :
    print('this is a test')


def switch(value):
    cases = {
        "Marseille": "C'est la ville où tu habites",
        "Paris": "C'est la capitale de la France",
        "Lyon": "Connue pour la µFête des Lumières"
    }
    return cases.get(value, "Ville inconnue")
print(switch(city)) #switch n'existe pas en Python

#name = input('What is your name ?')  #alert?
#age = input('What is your age ?')  #alert?
#city = input('What is your city ?')
#input retourne toujours un string, pour convertir str(), int(), float(), bool()
#age = int(age) + 100


#print(f"Hello {name}, {age} years old, {city}")

import math

friend = 0
is_friend = True

if is_friend:
    friend+=1
    friend +=3.5
    print(friend)

print(round(friend))
print(floor(friend))
print(math.ceil(friend))

operator = input('Enter an operator')
first = input("first number")
second= input("second")

if operator == '+':
    num = int(first) + int(second)
    print(num)
elif operator == '-':
    num = int(first) - int(second)
    print(num)
elif operator == '*':
    num = int(first) * int(second)
    print(num)
else :
    num = int(first) / int(second)
    print(num)


if num != 5:
    print('probleme')

message = "Plus grand que 5" if num > 5 else "Moins ou égal à 5"
print(message)
