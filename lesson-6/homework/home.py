#1. Modify String with Underscores
#Given a string txt, insert an underscore (_) after every third character. If a character is a vowel or 
# already has an underscore after it, shift the underscore placement to the next character. 
# No underscore should be added at the end.

#Examples
#Input: hello Output: hel_lo

#Input: assalom Output: ass_alom

#Input: abcabcabcdeabcdefabcdefg Output: abc_abc_abcd_abcd_abcdef


txt = 'abcabcdabcdeabcdefabcdefg'
vowels = 'uiaeoAOIUE'
cnt = 2
while cnt < len(txt):
    if txt[cnt] not in vowels:
        txt = txt[:cnt+1] + '_' + txt[cnt +1:]
        vowels += txt[cnt]
        cnt = cnt + 4
        #continue
    cnt = cnt + 1
    
txt[:-1]



#2. Integer Squares Exercise
#Task
#The provided code stub reads an integer, n, from STDIN. For all non-negative integers i where 0 <= i < n, print i^2.

#Example Input
#5
#Example Output
#0
#1
#4
#9
#16
#Input Format
#The first and only line contains the integer, n.


n=int(input('n ning qiymatini kirgazing:'))
if n >=0:
    for n in range (0,n):
        n=n**2
        print(n)
else:
    print('your entered value cannot be accepted, it should obey to the n>0')


#3. Loop-Based Exercises
#Exercise 1: Print first 10 natural numbers using a while loop

n=0
for n in range (n,10):
    n+=1 
    print(n)
#Exercise 3: Calculate sum of all numbers from 1 to a given number
#Example:

#Enter number 10
#Sum is: 55

number=int(input('enter the number:'))
sum=0
for x in range (1,number+1):
    sum=sum+x
print(sum)
#Exercise 2: Print the following pattern
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5


rows = 5

for i in range (1,rows+1):
    for j in range (1,i+1):
        print(j,end=" ")
    print()
#Exercise 4: Print multiplication table of a given number
#Example:

#2
#4
#6
#8
#10
#12
#14
#16
#18
#20

n=2
for i in range(1,11):
    print(n*i)
            #Exercise 5: Display numbers from a list using a loop
#given:

numbers = [12, 75, 150, 180, 145, 525, 50]
#Expected Output:

#75
#150
#145

num=[75,150,145]
for numbers in num:
    print(numbers)
    #Exercise 6: Count the total number of digits in a number
#Example:

n=75869
#Output: 5
cnt=0
for i in str(n):
     cnt+=1
print(cnt)


#Exercise 7: Print reverse number pattern
#5 4 3 2 1
#4 3 2 1
#3 2 1
#2 1
#1

n=5
for i in range (n,0,-1):
    for j in range (i,0,-1):
        print(j, end=" ")
    print ()
#Exercise 8: Print list in reverse order using a loop
#Given:

list1 = [10, 20, 30, 40, 50]
#Expected Output:

#50
#40
#30
#20
#10



for item in list1[::-1]:
    print(item)




#Exercise 9: Display numbers from -10 to -1 using a for loop
n=-10
if n <0:
    for i in range(n,0):
        print(i)
else:
    print()
    #Exercise 10: Display message “Done” after successful loop execution

n=5

for i in range (1,n+1):
    if i==n:
        print('done!')
    print(i)

n = 5

for i in range(1, n+1):
    print(i)

print("Done!")

#Exercise 11: Print all prime numbers within a range
#example:

#Prime numbers between 25 and 50:
#29
#31
#37
#41
#43
#47

n1=25
n2=50

for i in range (n1,n2+1):
    if i % 2==0 and sqrt(i)=





#Exercise 12: Display Fibonacci series up to 10 terms
#Example:

#Fibonacci sequence:
#0  1  1  2  3  5  8  13  21  34

n1=0
n2=1

print(n1,n2,end=" ")
for i in range(8):
    yechim=n1+n2
    print(yechim,end=" ")
    n1=n2
    n2=yechim

    #Exercise 13: Find the factorial of a given number
#Example:

#5! = 120

n=5
factorial_uchun=1

for i in range(1,n+1):
    factorial_uchun=factorial_uchun*i
print(f"{n}!={factorial_uchun}")




#4. Return Uncommon Elements of Lists
#Task
#Return the elements that are not common between two lists. The order of elements does not matter.

#Examples
list1 = [1, 1, 2]
list2 = [2, 3, 4]
#Output: [1, 1, 3, 4]

list_umumiy=[]

for i in  list1:
    if i not in list2:
        list_umumiy.append(i)

for i in list2:
    if i not in list1:
        list_umumiy.append(i)

print(list_umumiy)



list1 = [1, 2, 3]
list2 = [4, 5, 6]

#Output: [1, 2, 3, 4, 5, 6]

list_umumiy=[]

for i in  list1:
    if i not in list2:
        list_umumiy.append(i)
    else:
        list_umumiy.append(i)

for i in list2:
    if i not in list1:
        list_umumiy.append(i)
    else:
        list_umumiy.append(i)
print(list_umumiy)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.append(list2)
print(list1)


list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]

#Output: [2, 2, 5]

list_umumiy=[]

for i in  list1:
    if i not in list2:
        list_umumiy.append(i)

for i in list2:
    if i not in list1:
        list_umumiy.append(i)

print(list_umumiy)
