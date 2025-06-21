#Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

try:
    3/0
except ZeroDivisionError:
    print('deviding zero to the number is not true')
    
    

#Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
 

try:
    son=int(input('son kiriting'))
    print("sizni soniz-",son)   
except ValueError:
    print('xato qiymat kirgazildi')


#Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

try:
    i=input('enter the file name:')
    with open ('i') as file:
        data=file.read()
    data
except FileNotFoundError:
    print(f'file {i} is not found')

#Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.


try:
    num1=float(input('enter the 1 number:'))
    num2=float(input('enter the 2 number:'))
    print(f'number_1 = {num1} and number_2 = {num2}')
except TypeError:
    print('your netered value data type is not true')
    
#Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
try:
    file_name = input("Ochmoqchi bo'lgan fayl nomini kiriting: ")
    with open(file_name, 'r') as file:
        content = file.read()
        print("Fayl muvaffaqiyatli ochildi:\n")
        print(content)

except PermissionError:
    print(f"Xatolik: '{file_name}' faylini o'qishga ruxsat yo'q.")

#Write a Python program that executes an operation on a list and handles an IndexError exception
#  if the index is out of range.

l=[1,2,3,4,5,6,7,4,5,3,5,6,2,5,3,4,5,2,4,9]
try:
    num=l[25]
    print(num)
except IndexError:
    print('index is out of range')
#Write a Python program that prompts the user to input a number and handles 
# a KeyboardInterrupt exception if the user cancels the input


a=1

try:
    while a>0:
        print ("hello")
except KeyboardInterrupt:
    print('ERROR IS FOUND')
    print('user canceled the sikl')

#Write a Python program that executes division and handles 
# an ArithmeticError exception if there is an arithmetic error.


try:
    a = 1 / 0
except ArithmeticError as e:
    print(f"Xatolik yuz berdi: {e}")


#Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.

try:
    with open("example.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
except UnicodeDecodeError:
    print("Faylni UTF-8 kodlash bilan o‘qib bo‘lmadi. Kodlashda muammo bor.")
except FileNotFoundError:
    print("Fayl topilmadi. Iltimos, fayl nomini tekshiring.")
#Write a Python program that executes a list operation and handles 
#an AttributeError exception if the attribute does not exist.

l=[65465,5454,5454,48484,7124,7454,54,54,55,84,5,84,51,84,4,5,848,48,48,18,48,48,4,84,848]
try:
    l.keys()
    l.append(9)
except AttributeError:
    print('you got the wrong path')

#Write a Python program to read an entire text file.

with open('lesson_1.py') as file_reader:
    c=file_reader.read()
c

#Write a Python program to read first n lines of a file.
with open('lesson_1.py') as file_reader:
    c=file_reader.readline()
c


#Write a Python program to append text to a file and display the text.
with open('lesson_1.py','a') as file_reader:
    c=file_reader.write('qoshilgan yangi satr')
with open('lesson_1.py') as file_reader:
    c=file_reader.read()
c
#Write a Python program to read last n lines of a file.
name=input('enter the file name:')
n = int(input('Nechta oxirgi qatordan chiqaraylik? '))

def n_reader_function (name,n):
    try:
        with open( name, 'r') as o:
            c=o.readlines()
            lines=c[-n::]
        for i in lines:
            print(i)       
    except FileNotFoundError:
        print("Fayl topilmadi.")
    except Exception as e:
        print("Xatolik:", e)

n_reader_function(name, n)

#Write a Python program to read a file line by line and store it into a list.

line=input('enter the file name:')

def liner_functoion (line):
    l=[]
    with open (line,'r') as f:
        c=f.readline()
        l.append(c)
        for c in f:
            l.append(c)
        print(l)
        


    
liner_functoion(line)

#Write a Python program to read a file line by line and store it into a variable.



line=input('enter the file name:')
def liner_function(line):
    with open(line, 'r') as f:
        for c in f:
            a = ' '.join(c)  
            print(a)

filename = input('Enter the file name: ')
liner_function(filename)

#Write a Python program to read a file line by line and store it into an array.


line=input('enter the file name:')

def liner_functoion (line):
    array=[]
    with open (line,'r') as f:
        c=f.readline()
        array.append(c)
        for c in f:
            array.append(c)
        print(array)
        


    
liner_functoion(line)
#Write a Python program to find the longest words.


inputted_value=input('enter the file name:')

def longest_word_function (inputted_value):
    ml=[]
    with open (inputted_value,'r') as file_name:
        content=file_name.read()
        splitter=content.split()
        for i in splitter:
            ml.append(i)
        longest=max(ml,key=len)
        print('longest word is - ',longest)
        print('length of it=',len(longest))

longest_word_function (inputted_value)


#Write a Python program to count the number of lines in a text file.

inputted_value=input('enter the file name:')

def counter_function (inputted_value):
    with open (inputted_value,'r') as file_name:
        content=file_name.read()
        cnt=content.split()
        freq={}
        for i in cnt:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        print(freq)

counter_function (inputted_value)



#Write a Python program to count the frequency of words in a file.

inputted_value=input('enter the file name:')

def fr_function (inputted_value):
    with open (inputted_value,'r') as file_name:
        content=file_name.read()
        cnt=content.split()
        for i in cnt:
            print(i,'takrorlangan qiymati =',cnt.count(i))

fr_function (inputted_value)




inputted_value=input('enter the file name:')

def fr_function (inputted_value):
    with open (inputted_value,'r') as file_name:
        content=file_name.read()
        frq=0
        for i in content:
            if frq==frq[i]:
                frq+=1
        print(frq)

counter_function (inputted_value)


#Write a Python program to get the file size of a plain file.
inputted_value = input('enter the file name: ')

def fr_function(inputted_value):
    with open(inputted_value, 'r') as file_name:
        content = file_name.read()
        words = content.split()
        frq = {}  # so'zlar chastotasi uchun lug'at

        for i in words:
            if i in frq:
                frq[i] += 1
            else:
                frq[i] = 1

        print(frq)

fr_function(inputted_value)

#Write a Python program to write a list to a file.
my_list = ['apple', 'banana', 'cherry', 'date']

inputting=input('enter the file name:')

with open(inputting,'w') as f:
    for i in my_list:
        f.write(i+ '\n')
   


#Write a Python program to copy the contents of a file to another file.
 
e1=input('enter the source file name')
e2=input('enter the file name which you want to put/place')

with open (e1,'r') as f:
    copy=f.read()

with open(e2,'w') as f2:
    put=f2.write(copy)

    print('copied bruh')

    #Write a Python program to combine each line from the first file with the corresponding line in the second file.

f1=input('enter 1 file name:')
f2=input('enter 2 file name:')

with open (f1,'r') as f:
    con=f.readlines()
with open (f2,'r') as f:
    con2=f.readlines()

for c,c2 in zip(con,con2):
    combine=' '.join([c,c2])
    print(combine)
#Write a Python program to read a random line from a file.

f1=input('enter file name:')
n=int(input('which line you want to read'))

with open (f1,'r') as f:
    con=f.readlines()
    
    for i in con:
        if 1 <= n <= len(con):
            print(con[n-1])
        else:
            print('value is out of range')

#Write a Python program to assess if a file is closed or not.

# Foydalanuvchidan fayl nomini olish
filename = input("Enter file name: ")

# Faylni ochish
f = open(filename, 'r')

# Fayl ochiqmi?
print("Is the file closed?", f.closed)  # False bo'lishi kerak

# Faylni yopamiz
f.close()

# Fayl yopildimi?
print("Is the file closed now?", f.closed)  # True bo'lishi kerak

#Write a Python program to remove newline characters from a file.
# Write a Python program to remove newline characters from a file.

inputted = input('Input file name: ')

# Read lines and remove newline characters
with open(inputted, 'r') as files:
    lines = files.readlines()


cleaned = [line.strip() for line in lines]

print("Newline characters removed successfully.")


#Write a Python program that takes a text file as input 
# and returns the number of words in a given text file.

#Note: Some words can be separated by a comma with no space.

inputted=input('input file name:')

cnt=0
with open (inputted,'r') as files:
    con=files.read()
    cm=con.split() 
    for i in cm:
        cnt=cnt+1
       
print(cnt)

    #Write a Python program to extract characters from various text files and put them into a list.

characters=['@','#','%','^','&','*','!',')','(']
list=[]
inputting=input('input file name:')

with open (inputting,'r') as f:
    c=f.read()
    for i in c:
        if i in characters:
            a=list.append(i)
    input2=input('enter another file name')
    with open (input2,'r') as fi:
        c1=fi.read()
        for e in c1:
            if e in characters:
               a=list.append(e)
    
    print(list)
       

#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.


for i in range (65,91):

    file_name=chr(i)+'.txt'
    with open (file_name,'w') as f:
        f.write(f'this is file name {file_name}')


print("26 files created successfully")
#Write a Python program to create a file where all letters of the English alphabet
#  are listed with a specified number of letters on each line.


i=65


for i in range(65,90):
    c=chr(i)
    print(c)
    print(i)


   












    
    

















