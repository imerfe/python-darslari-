# Homework:

    # Exercise 1: Threaded Prime Number Checker

    # Write a Python program that checks whether a given range of numbers contains prime numbers.
    # Divide the range among multiple threads to parallelize the prime checking process.
    # Each thread should be responsible for checking a subset of the range, and 
    # the main program should print the list of prime numbers found.

import math
import threading
list=[]
def my_function(n):
    for i in range(n):
        if i<2:
            print(f'{i} is not prime number')
            continue

        b=round(math.sqrt(i))
        for c in range(2,b+1):
            if i%c==0:
                list.append(i)
                print(f'{i} is not prime')
                break 
        else:
            list.append(i)
            print(f'{i} is a prime number')

t2=threading.Thread(target=my_function,args=(100,))
t2.start()
t2.join()


# Exercise 2: Threaded File Processing

# Write a program that reads a large text file containing lines of text. 
# Implement a threaded solution to count the occurrence of each word in the file.
# Each thread should process a portion of the file, and 
# the main program should display a summary of word occurrences across all threads.

with open ('f1.csv','r') as f:
    l=[]
    c=f.read()
    b=c.split()
    icons=(",","!",')','(',"-","=")
    for i in b:
        if i in icons:
            c=c.replace(i,"")
        b=c.split()
        l.append(b)
    def cnt():
        count=0
        if i in l:
            count+=1
        
    for word, count in cnt.items():
        print(f"{word}: {count}")




