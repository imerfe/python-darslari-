#Dictionary Exercises
#1. Sort a Dictionary by Value
#Write a Python script to sort (ascending and descending) a dictionary by value.

dic={'number_1':12,'number_5':555,'number_6':6,'number_2':42,'number_3':73,'number_4':14}

asc=sorted(dic.values())
asc

desc=sorted(dic.values(),reverse=True)
print('ascending',asc)
print('descending',desc



      #2. Add a Key to a Dictionary
#Write a Python script to add a key to a dictionary.

Sample_Dictionary={0: 10, 1: 20}


Sample_Dictionary[2]=30
Sample_Dictionary


#3. Concatenate Multiple Dictionaries
#Write a Python script to concatenate the following dictionaries to create a new one.

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}


dic_new=dic1|dic2|dic3
dic_new

dic_new_2={**dic1,**dic2,**dic3}
dic_new_2


#4. Generate a Dictionary with Squares
#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

#Sample Dictionary (n = 5):
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#first path 

#n = 5
#square_dict={x:x*x for x in range(1,n+1)}
#square_dict

#second path 

n=5
square_dict={}
for i in range(1,n+1):
    square_dict[i]=i*i
square_dict

#5. Dictionary of Squares (1 to 15)
#Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) 
# and the values are the square of the keys.

#Expected Output:

#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121,
 
n=15 
square_dictionery={}

for n in range (1,n+1):
    square_dictionery[n]=n*n
square_dictionery


#Set Exercises
#1. Create a Set
#Write a Python program to create a set.


created_set={1,2,3,4,5,6,7,8,9}
created_set



#2. Iterate Over a Set
#Write a Python program to iterate over sets.

created_set={1,2,3,'jorbon',5,'xenok',7,8,9}

for i in created_set:
    print(i)

#4. Remove Item(s) from a Set
#Write a Python program to remove item(s) from a given set.


created_set={1,2,3,'jorbon',5,'xenok',7,8,9}
created_set.remove('jorbon')
created_set


#5. Remove an Item if Present in the Set
#Write a Python program to remove an item from a set if it is present in the set.


created_set.discard(90)
created_set











