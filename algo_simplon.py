
'''
EXERCICE 1
Afficher les nombres paire de 20 à 0

for i in range(20, -1, -2):
    print(i)
'''
from operator import contains

'''
Exercice 2
Dans une boucle, générer un nombre entier aléatoire compris entre 0 et 100. 
Lorsque le nombre vaut 42, vous quitterez la boucle et afficherez le nombre de tours qu'il aura fallu pour tirer le 
nombre 42.

Modifiez le programme pour tirer 100 fois le nombre 42. Vous afficherez la moyenne du nombre de tirage nécessaire pour 
afficher le nombre 42
'''

from random import *

min_nb = 0
max_nb = 100
round= 0
rounds_number = []

number = randint(min_nb, max_nb)
'''
# PART 1 
while True:
    my_number = randint(min_nb, max_nb)
    round+=1
    if my_number == 42:
        print(round)
        break
'''

#PART 2
num_trials = 100
for _ in range(num_trials):
    round_count = 0
    while True:
        my_number = randint(min_nb, max_nb)
        round_count += 1
        if my_number == 42:
            rounds_number.append(round_count)
            break

total = 0
for number in rounds_number:
    total += number

average = total / len(rounds_number)

#print(average)


'''
CODING DOJO
1 - Reverse a string
Write a function that will accept a string as parameter and return a reversed string

ex :

reverseString('hello')

should return 'olleh'
'''

def reverse_string(string):
    reverse = ''
    max_length= len(string) - 1
    while max_length >= 0:
        reverse+=string[max_length]
        max_length -= 1
    print(reverse)

reverse_string("hello")

'''
2 - Validate a palindrome
Write a function that will accept a string as parameter and return true if string is a palindrome (ex : 'ici'), false otherwise

ex :

isPalindrome('hello')

should return false
'''

def isPalindrome(string):
    reverse = ''
    max_length= len(string) - 1
    while max_length >= 0:
        reverse+=string[max_length]
        max_length -= 1
    print(True if reverse == string else False)

isPalindrome("ici")

'''
3 - Reverse an integer
Write a function that will accept an integer as parameter and return a reversed integer (taking into account negative integers)

ex :

reverseInt(-12345)

should return -54321
'''

def reverseInt(int):
    reverse = ''
    string = str(int)
    max_length= len(string) - 1
    while max_length >= 0:
        reverse+=string[max_length]
        max_length -= 1
    print(reverse)

reverseInt(-123)

'''
4 - Capitalize letters
Write a function that will accept a string as parameter and return a string with only the first letter 
of each word capitalized

ex :

capitalizeString('I love JavaScript')

should return 'I Love Javascript'
'''

def capitalizeString(string):
    list = string.split(' ')
    changed_string=''
    for word in list:
        charcode = ord(word[0]) - 32
        letter = chr(charcode)
        changed_string += letter + word[1:] + ' '
    print(changed_string)

capitalizeString("rafik le clochard")

'''
5 - Max character
Write a function that will accept a string as parameter and return the character with the most occurences

ex :

maxCharacter('Javascript')

should return 'a'
'''

def maxCharacter(string):
    frequence = {}
    max_count = 0
    char= ''

    for letter in string:
        if letter in frequence:
            frequence[letter] +=1
        else:
            frequence[letter] = 1

    for letter, count in frequence.items():
        if count > max_count:
            max_count = count
            char = letter

    print(f"La lettre apparaisant le plus ({max_count}) est la lettre de {char}")


maxCharacter('Javascript')


'''
6 - FizzBuzz
Write a function that will print all the integers between 1 and 100. For multiples of 3 it should print 'Fizz' instead 
of the actual integer, for multiples of 5 it should print 'Buzz', for multiples of 3 and 5 it should print 'Fizzbuzz'

ex :

fizzBuzz()

should return
1
2
'Fizz'
4
'Buzz'
'Fizz'
7
8
'Fizz'
'Fizzbuzz'
...
'''

def fizzBuzz():
    num_trials = 101
    result = ''
    for num in range(1, num_trials):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizzBuzz()

'''
7 - Longest word
Write a function that will accept a string as parameter and return the longest word in that string.
If more than one word are the same lenth and are longest, the function should return an array containing these words.
Returned word(s) should be lower case

ex :

longestWord('I love coding')

should return 'coding'

longestWord('Hello there, I love cakes')

should return ['hello', 'there', 'cakes']
'''

def longestWord(sentence):
    words = sentence.split(" ")
    frequences= {}
    max_count = 0
    longestWordList = []

    for word in words:
        word = word.replace(',', '')
        frequences[word] = len(word)

    for count in frequences.values():
        if count > max_count:
            max_count = count

    for word, count in frequences.items():
        if count == max_count:
            longestWordList.append(word)

    print(longestWordList)



longestWord("Hello there, I love cakes")
longestWord("I love coding")

'''
8 - Array chunking
Write a function that will accept an array (containing integers or strings) and an integer as parameters and split this 
array into arrays of the given integer length

ex :

chunkArray([1, 2, 3, 4, 5, 6, 7], 2)

should return [[1, 2], [3, 4], [5, 6], [7]]
'''





'''
10 - Anagram
Write a function that will accept 2 strings as parameters and return true if strings are anagrams, false otherwise.
Function should ignore spaces and special characters

ex :

isAnagram('elbow', 'below')

should return true

isAnagram('dormitory', 'Dirty rooms##')

should return true

isAnagram('hello', 'There')

should return false
'''

def isAnagram(one, two):
    target = 0
    one = ''.join([char.lower() for char in one if char.isalpha()])
    two = ''.join([char.lower() for char in two if char.isalpha()])

    if len(one) != len(two):
        return print(False)

    for letter in one:
        if letter in two:
            two = two.replace(letter, '', 1)
        else:
            return print(False)
    return print(True)

isAnagram('dormitory', 'Dirty room##')
isAnagram('elbow', 'below')
isAnagram('hello', 'There')

'''
11 - Letter changes
Write a function that will accept a string as parameter and return a lower case string in which each character of the 
original string will be replaced by the next character in the alphabet (ex: a will become b), and each vowel will be 
capitalized.
If there is a z in the original string, it should become a

ex :

letterChanges('Hello there')

should return 'Ifmmp Uifsf'

letterChanges('I love buzz')

should return 'J mPwF cVAA'
'''

def letterChanges(string):
    changes = ""
    string = string.lower()
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    for word in string:
        for letter in word:
            if letter.isalpha():
                if letter == 'z' :
                    changes += 'A'
                elif ord(letter) != 32:
                    new_letter = chr(ord(letter) + 1)

                    if new_letter in vowels:
                        new_letter = chr(ord(new_letter) - 32)
                        changes += new_letter
                    else:
                        changes += new_letter
            else:
                changes+= letter

    return print(changes)


letterChanges('Hello there')
letterChanges('I love buzz')