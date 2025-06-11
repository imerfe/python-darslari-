
#def is_leap(year): """ Determines whether a given year is a leap year.

#A year is a leap year if:
#- It is divisible by 4, and
#-It is NOT divisible by 100, unless it is also divisible by 400.

#Parameters:
#year (int): The year to be checked.

#returns:
#bool: True if the year is a leap year, False otherwise.
#"""
#if not isinstance(year, int):
#    raise ValueError("Year must be an integer.")

#return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


year=int(input('enter the year and you can know that your entered date is leap year or not:'))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('this year is leap year')
else:
    print('no, this year is not leap year')

 
 
#2. Conditional Statements Exercise
#Given an integer, n, perform the following conditional actions:

#If n is odd, print Weird
#If n is even and in the inclusive range of 2 to 5, print Not Weird
#If n is even and in the inclusive range of 6 to 20, print Weird
#If n is even and greater than 20, print Not Weird
#Input Format
#A single line containing a positive integer, n.

#Constraints
#1 <= n <= 100
#Output Format
#Print Weird if the number is weird. Otherwise, print Not Weird.

#Sample Input 0
#3
#Sample Output 0
#Weird

n=int(input('enter the number:'))

if n%2!=0:
    print('weird')
else:
    if n in range (2,5):
        print('not weird')
    else:
        if n in range(6,20):
            print('weird')
        else:
            n > 20
            print('not weird')


#Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.
#Give two solutions.

#Solution 1 with if-else statement.

a=int(input('enter the value of a:'))
b=int(input('enter the value of b:'))

if a // 2 != 0:
    a+=1 

number_even= list(range (a,b+1,2))
print(number_even)


#Solution 2 without if-else statement.

a=int(input('enter the value of a:'))
b=int(input('enter the value of b:'))

starting_position = a + (a % 2)

numbers=list(range(starting_position,b+1,2))
print(numbers)





  
