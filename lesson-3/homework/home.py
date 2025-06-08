#1. Create and Access List Elements
#Create a list containing five different fruits and print the third fruit.

l=['anor','olma','uzum','bodring','qovun']

l[3]


#2. Concatenate Two Lists
#Create two lists of numbers and concatenate them into a single list.

list_1=[1,2,3,4,564,645]

list_2=[45,67,89,64]

list_1.append(list_2)

list_1
#3. Extract Elements from a List
#Given a list of numbers, extract the first, middle, and last elements and store them in a new list.

listed=[1,2,3,4,5,6,7,8,9]
first_list=listed[0]
middle_list=listed[len(listed)//2]
last_list=listed[-1]

new_list=[first_list,middle_list,last_list]

print(new_list)

#4. Convert List to Tuple
#Create a list of your five favorite movies and convert it into a tuple.

movie_list=['titanik','mister_bin','hobs and shou','love','home']
news_mvies=tuple(movie_list)
type(news_mvies)
#5. Check Element in a List
#Given a list of cities, check if "Paris" is in the list and print the result.

country_city='paris'
list_of_cities=['german','paris','america','uk','usa']

if country_city in list_of_cities:
    print('paris is in the list')
else:
    print('no')

#6. Duplicate a List Without Using Loops
#create a list of numbers and duplicate it without using loops.

numbers=[1,2,3,4,5,6,7,8,9]
numbers2=numbers.copy()

print(numbers)
print(numbers2)
#7. Swap First and Last Elements of a List
#Given a list of numbers, swap the first and last elements.

numbers_list=[10,20,30,40,50]

numbers_list[0],numbers_list[-1]=numbers_list[-1],numbers_list[0]

print(numbers_list)


#8. Slice a Tuple
#Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.

numbers_tuple=(1,2,3,4,5,6,7,8,9,10)
numbers_tuple[3:7]


#9. Count Occurrences in a List
#Create a list of colors and count how many times "blue" appears in the list.
list_of_colours=['black','white','red','blue','green']
list_of_colours.count('blue')

#10. Find the Index of an Element in a Tuple
#Given a tuple of animals, find the index of "lion".

animals = ("tiger", "lion", "elephant", "giraffe")

animals.index('lion')
#11. Merge Two Tuples
#Create two tuples of numbers and merge them into a single tuple.

tuple1=(1,2,3,4,5)
tuple2=(6,7,8,9,10)

tuple_merge=tuple1+tuple2

print(tuple_merge)
#12. Find the Length of a List and Tuple
#Given a list and a tuple, find and print their lengths.


animals = ("tiger", "lion", "elephant", "giraffe")

list_number=[1,2,3,4,5]

len_animal=len(animals)
list_len=len(list_number)

print(len_animal)
print(list_len) 

#13. Convert Tuple to List
#Create a tuple of five numbers and convert it into a list.

tuple1=(1,2,3,4,5)

list_tuple=[tuple1]

print(type(list_tuple))
#14. Find Maximum and Minimum in a Tuple
#Given a tuple of numbers, find and print the maximum and minimum values.

tuple1=(1,2,3,4,5)

print(max(tuple1))
print(min(tuple1))
    

#15. Reverse a Tuple
#Create a tuple of words and print it in reverse __rder.


animals = ("tiger", "lion", "elephant", "giraffe")

animals_1=animals[::-1]
animals_1




