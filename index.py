import math
from math import floor
from operator import truediv

# variables
my_variable = "Ines"
my_num= 1 + 1
array = [1,2,3,4]
my_object = {'name' : 'Ines'}
my_float = 1.5

# print(my_variable[-1])
# print(my_variable[0])
# print(my_num)
# print(len(array))

# functions
def sum_odd_numbers(items):
    result = 0

    for num in items :
        if num % 2 == 0 :
            result+=num
        else :
            result*=num
    return result

#console.log of python
print(sum_odd_numbers(array))

print(f"Hello {my_num}") #f for format

# object
myself = {
    "name": "Ines",
    "age": 32,
    "city": 'Marseille',
}

# desturation
name, age, city = myself["name"], myself["age"], myself["city"]

print(f"My name is {myself['name']}, I am {myself['age']} years old and I live in {myself['city']}")
print(f"My name is {name}, I am {age} years old and I live in {city}")


#if elseif else statement
if city == "Paris" or (age == 35 and name == 'Ines'):
    print("oui")
elif city == "Marseille" and name == 'Coucou':
    print("non")
else :
    print('this is a test')

#switch n'existe pas en Python
def switch(value):
    cases = {
        "Marseille": "C'est la ville où tu habites",
        "Paris": "C'est la capitale de la France",
        "Lyon": "Connue pour la µFête des Lumières"
    }
    return cases.get(value, "Ville inconnue")
print(switch(city))

# alert
#name = input('What is your name ?')
#age = input('What is your age ?')
#city = input('What is your city ?')

#input retourne toujours un string, pour convertir str(), int(), float(), bool()

#age = int(age) + 100


#print(f"Hello {name}, {age} years old, {city}")

friend = 0
is_friend = True

if is_friend:
    friend+=1
    friend +=3.5
    print(friend)

print(round(friend))
print(floor(friend))
print(math.ceil(friend))

operator = '+' #input('Enter an operator')
first = 1#input("first number")
second= 1#input("second")

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

# ternaire
message = "Plus grand que 5" if num > 5 else "Moins ou égal à 5"
print(message)

# String methods
my_string = 'Ines is learning Python'
print(len(my_string))
print(my_string.find("i")) # first occurence of i = 5
print(my_string.find("I")) # first occurence of I = 0
print(my_string.rfind("i")) # last occurence (r for reverse) of i = 13
print(my_string.rfind("q")) # -1 => not find
print(my_string.find("q")) # -1 => not find
print(my_string.upper()) # uppercase
print(my_string.lower()) # lowercase
print(my_string.capitalize()) # capitalize
print(my_string.split()) # split all word into array
print(list(my_string)) # split all characters into array
print(my_string.count('i')) # 2 i
print(my_string.replace('i', 'I')) # 1er parametre est remplacé par le second
print(help(str)) # savoir toutes les méthodes des str

# string indexing str
# start:end:step
print(my_string[:4]) # start 0, end 4 => Ines
print(my_string[:4:2]) # start 0, end 4, step 2 > Ie
print(my_string[::2]) # start 0, end 0, step 2 > Ie slann yhn


#format specifers
price1=2.25689
price2=-12.048
price3=4578

print(f"Price 1 is ${price1:.2f}") #Price 1 is $2.26
print(f"Price 2 is ${price2:.3f}") #Price 2 is $-12.048
print(f"Price 3 is ${price3:.5f}") #Price 3 is $4578.00000
print(f"Price 1 is ${price1:10}") #Price 1 is  $   2.25689
print(f"Price 2 is ${price2:010}") #Price 2 is $-00012.048 (0 patted)
print(f"Price 3 is ${price3:<10}") #Price 3 is $4578       (left justify)
print(f"Price 3 is ${price3:>10}") #Price 3 is $      4578 (right justify)
print(f"Price 3 is ${price3:^10}") #Price 3 is $   4578    (center)
print(f"Price 3 is ${price3:+10}") #Price 3 is $     +4578 (center)
print(f"Price 3 is ${price3:,}") #Price 3 is $4,578
print(f"Price 3 is ${price3:+,.2f}") #Price 3 is $+4,578.00

# LOOPS
for x in range(1,11):
    print(x)

#comment plusieurs lignes
'''
saeson = input('What is your favorite season ?')
while saeson == '':
    print('you did not enter your favorite season')
    saeson = input('What is your favorite season ?')

print(f'Your favorite season is {saeson}')
'''
'''

import time

time.sleep(3) # fonction bloquante. attendra pendant 3 secondes avant de continuer à exécuter le code suivant.
print("TIME'S UP")

for x in range(10, 0, -1):
    print(x)
    time.sleep(1)

print("TIME'S UP")
'''
# Collection (list, set, tuple)
# List = [] ordered and changeable. duplicate ok
# set = {} unordered and immutable, no duplicates
# tuple = () ordered and unchangeable, duplicate ok (faster)

# LIST
fruits = ["apple", "orange","banana", "strawberry"]

print(fruits[:2])
print(fruits.index('banana'))
print(fruits.pop(), fruits) #strawberry ['apple', 'orange', 'banana']
print(fruits.insert(0, 'coconut'), fruits) #None ['coconut', 'apple', 'orange', 'banana'] (insert ne retourne rien)
print(fruits.insert(2, 'ananas'), fruits) #None ['coconut', 'apple', 'ananas', 'orange', 'banana']
print(fruits.remove('ananas'), fruits) #None ['coconut', 'apple', 'orange', 'banana']
print(fruits.sort(), fruits) #None ['apple', 'banana', 'coconut', 'orange']
print(fruits.reverse(), fruits) #None ['orange', 'coconut', 'banana', 'apple']
#  print(fruits.clear(), fruits) #None []
upper = map(lambda fruit: fruit.upper(), fruits)
filtered_fruit = filter(lambda fruit: len(fruit) > 5, fruits)
print(fruits.append('banana')) #['orange', 'coconut', 'banana', 'banana']
print(fruits.count('banana')) # 2

print(upper) # <map object at 0x7f4d1ee64fd0>
print(list(upper)) # ['ORANGE', 'COCONUT', 'BANANA', 'APPLE']
print(list(filtered_fruit)) #['orange', 'coconut', 'banana']


# SET
fruits = {"apple", "orange", "banana", "strawberry"}

print(dir(fruits)) #liste all method
# ['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__',
# '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__',
# '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__',
# '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference',
# 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop',
# 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

print(fruits.add('pineapple'), fruits) #None {'banana', 'strawberry', 'orange', 'apple', 'pineapple'}
print(fruits.add('pineapple'), fruits) #None {'strawberry', 'orange', 'pineapple', 'apple', 'banana'}
print(fruits.remove('banana'), fruits) #None {'orange', 'apple', 'strawberry', 'pineapple'}

more_fruits = {"grape", "kiwi", "banana"}
print(fruits.update(more_fruits),fruits) #None {'kiwi', 'pineapple', 'orange', 'apple', 'banana', 'strawberry', 'grape'}

# TUPLES
# ordered and unchangeable
fruits_tuple = ("grape", "kiwi", "banana")

print(dir(fruits_tuple)) #liste all method
'''
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
'''

print(len(fruits_tuple)) # 3
print(help(fruits_tuple)) #liste all method
'''
Help on tuple object:

class tuple(object)
 |  tuple(iterable=(), /)
 |  
 |  Built-in immutable sequence.
 |  
 |  If no argument is given, the constructor returns an empty tuple.
 |  If iterable is specified the tuple is initialized from iterable's items.
 |  
 |  If the argument is a tuple, the return value is the same object.
 |  
 |  Built-in subclasses:
 |      asyncgen_hooks
 |      UnraisableHookArgs
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __class_getitem__(...)
 |      See PEP 585
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.

None
'''

print('kiwi' in fruits_tuple) #True
print(fruits_tuple.count('kiwi')) #1
print(fruits_tuple) # ('grape', 'kiwi', 'banana')

for fruits in fruits_tuple:
    print(fruits)

#2D List
fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries= [fruits, vegetables, meats]

print(groceries) #[['apple', 'orange', 'banana', 'coconut'], ['celery', 'carrots', 'potatoes'], ['chicken', 'fish', 'turkey']]
print(groceries[0]) #['apple', 'orange', 'banana', 'coconut']
print(groceries[0][0]) #apple

for collection in groceries:
    for food in collection:
        print(food, end=" ",) #apple orange banana coconut celery carrots potatoes chicken fish turkey


# Concession stand program

menu = {
    "pizza":3.00,
    "chips": 1.45,
    "popcorn": 4.00,
    "fries": 2.1,
}

cart = []
total = 0;

for key, value in menu.items():
    print(f"{key:10}: {value}")
    total+=value;
    print(floor(total))

# random numbers

import random

# Your list
my_list = ['ines', 'rafik', 'nassima']

# Generate a random integer
number = random.randint(1, 20)

# Generate a random float between 0 and 1
another = random.random()

# Choose a random element from the list
choice = random.choice(my_list)

# Choose two random elements from the list (with replacement)
choices = random.choices(my_list, k=2)

# Shuffle the list
random.shuffle(my_list)

print('Random integer:', number)
print('Random float:', another)
print('Random choice:', choice)
print('Random choices:', choices)
print('Shuffled list:', my_list)


