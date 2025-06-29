task-1

Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\Users\MIRZOBEK> pip install numpy
Requirement already satisfied: numpy in c:\users\mirzobek\appdata\local\programs\python\python312\lib\site-packages (2.3.1)

[notice] A new release of pip is available: 25.0.1 -> 25.1.1
[notice] To update, run: python.exe -m pip install --upgrade pip
PS C:\Users\MIRZOBEK>

i created my virtual environment and use,import some libraries to my venv



2-task 


def bolish(a,b):
    if b!=0: 
        return a/b
    else:
        print('this value is not allowed')
def kopaytirish(a,b):
    return a*b
def add (a,b):
    return a+b
def ayirish(a,b):
    return a-b
  
import math_operations as ma

print('bolish',ma.bolish(5,5))
print('kopaytirish',ma.kopaytirish(5,3))
print('qoshish',ma.add (14,52))
print('ayirish',ma.ayirish(44,22))



3-task 
Create string_utils.py module. 
Define reverse_string and count_vowels functions in it.
(All functions accept one argument in this task)


    #Create string_utils.py module. 
# Define reverse_string and count_vowels functions in it. (All functions accept one argument in this task)

def reverse_string(a):
    b=a[::-1]
    print(f'Teskarisi={b}')
    return b
def count_vowels(a):
    c="aioueAIOUE"
    cnt=0
    for i in a:
        if i in c:
            cnt+=1
    print(f'sanalgan wovellar soni-{cnt}')
    return cnt


import string_utils as f

print (f.reverse_string('Olma'))
print (f.count_vowels('olma'))

# geometry/circle.py

import math

def calculate_area(radius):
    """Calculate the area of a circle given the radius."""
    return math.pi * radius ** 2

def calculate_circumference(radius):
    """Calculate the circumference of a circle given the radius."""
    return 2 * math.pi * radius
# main.py
from circle import calculate_area, calculate_circumference

r = 5
print("Area:", calculate_area(r))
print("Circumference:", calculate_circumference(r))

# file_operations/file_reader.py

def read_file(file_path):
    """Reads the content of a file and returns it as a string."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"File not found: {file_path}"
    except Exception as e:
        return f"An error occurred while reading the file: {e}"


# file_operations/file_reader.py

def read_file(file_path):
    """Reads the content of a file and returns it as a string."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"File not found: {file_path}"
    except Exception as e:
        return f"An error occurred while reading the file: {e}"
  # main.py
from file import read_file, write_file

file_path = "sample.txt"

# Write content
write_file(file_path, "Hello, Mirzobek!\nThis is your custom package.")

# Read content
content = read_file(file_path)
print("File content:\n", content)
  
