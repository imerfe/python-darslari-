#1. Age Calculator
#Write a Python program to ask for a user's name and year of birth, then calculate and display their age.

name=input("hello, what is your name:")
age=int(input('when you born(in year)='))
from datetime import datetime
current_year= datetime.now().year
counted=current_year-age
result=f'My name is {name}. now, i  am {counted} years old'
result 


#2. Extract Car Names
#Extract car names from the following text:

txt = 'LMaasleitbtui'

print('c1',txt[0:13:2])
print('c2',txt[1::2])


#3. Extract Car Names
#Extract car names from the following text:

txt = 'MsaatmiazD'

print('c',txt[::2])
print('c1',txt[::-2])

#4. Extract Residence Area
#Extract the residence area from the following text:

txt = "I'am John. I am from London"

txt2=txt.split(" ")[-1]
print(txt2)

#5. Reverse String
#Write a Python program that takes a user input string and prints it in reverse order.

inputted=input('enter word which you want')
txt=inputted[::-1]
print(txt)

#6. Count Vowels
#Write a Python program that counts the number of vowels in a given string.

vowels=("aiouoe")
entering=input('enter the word and you can get the nubmer of vowels in your entered word:')

cnt = 0 

for i in entering:
    if i.lower() in vowels :
        cnt=cnt+1

print ( 'vowels numbers=' , cnt )


#7. Find Maximum Value
#Write a Python program that takes a list of numbers as input and prints the maximum value.

inputted_strings=input('enter the numbers which are seperated by spaces:')

numbers=inputted_strings.split()

numbers_1=list(map(float,numbers))

if numbers_1:
    max_value=max(numbers_1)
    print("the max value is:", max_value)
else:
    print('please enter another number blok')

if numbers_1:
    min_value=min(numbers_1)
    print("the min value is:", min_value)
else:
    print('please enter another number blok')

#8. Check Palindrome
#Write a Python program that checks if a given word is a palindrome 
#(reads the same forward and backward).

inputted=input ('input the word:')

inputted=inputted.lower()

reversed=inputted[::-1]

if reversed == inputted:
    print('true')
else:
    print('false')


#9. Extract Email Domain.
#Write a Python program that extracts and prints 
#the domain from an email address provided by the user.

input_value=input('Email manzilingizni kiriting')

txt=input_value.split('@')[-1]
txt


#10. Generate Random Password
#Write a Python program to generate a random password containing letters, digits, and special characters.

import random
import string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

all_chars = letters + digits + special_chars

password_length = 12

password = ''.join(random.choice(all_chars) for _ in range(password_length))

print("Yaratilgan parol:", password)
