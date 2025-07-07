import json

# Task: JSON Parsing
# write a Python script that reads the students.jon 
# JSON file and prints details of each student.

with open('students.json','r',encoding="utf-8") as f:
    command = json.load(f)

for i in command:
    print(f'ID={i['name']}')
    print(f'AGE={i['age']}')

# # Task: Weather API
# # Use this url : https://openweathermap.org/
# # Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent)
# #  and print relevant information (temperature, humidity, etc.).
import requests
import json

city = 'Tashkent'
api_key = "5e0fc1d5b49e6414ccc19298c8e1a263"

# To'g'ri API manzili:
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

# So‘rov yuborish
response = requests.get(url)
data = response.json()

# Javob holatini tekshirish
if response.status_code == 200:
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    
    print(f"Weather in {city}:")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description}")
else:
    print("Xatolik yuz berdi:", data)

# Task: JSON Modification
# Write a program that allows users to add new books, 
# update existing book information, 
# and delete books from the books.json JSON file.

import json

books=[]

def adding_new_book():
    try:
        with open('book.json','r') as file:
            file=json.load(file)
    except FileNotFoundError:
        books=[]
    
    print("yangi kitob qo'shish:")
    new_book={
        "id":int(input('Id:')),
        "name":input('Kitob nomi:'),
        "published_year":input('Nashr yili:'),
        "genre":input("Janri")
        }
    books.append(new_book)

    with open ('book.json','w') as f1:
        json.dump(books,f1)


def updating():
    try:
        with open('book.json','r') as f:
            books=json.load(f)
    except FileNotFoundError:
        print("there is not any book to update")
        return 

    name_to_update = input("Qaysi kitobni yangilamoqchisiz? (nomini kiriting): ")
    found=False

    for i in books:
        if i['name'].lower()==name_to_update.lower():
            print("Yangi ma'lumotlarni kiriting:")
            i['name']=input('kitob nomi:')
            i['published_year']=int(input('nashr yili'))
            i['genre']=input('janri:')
            found=True
            break
    if found:
        with open('book.json','w') as f:
            json.dump(books,f)
            print(" Kitob muvaffaqiyatli yangilandi.")
    else:
        print(" Bunday nomdagi kitob topilmadi.")

def deleting():
    try:
        with open('book.json','r') as asi:
            kitob=json.load(asi)
    except FileNotFoundError:
        print('file mavjud emas')
        return
    
    find=False
    
    delete=input('qaysi kitobni o\'chirib tashlamoqchisiz')
    for i in kitob:
        i['name'].lower()==delete.lower()
        kitob.remove(i)
        find=True
        break 
    
    if find:
        with open('book.json','w') as f:
            json.dump(books,f)
            print(" Kitob muvaffaqiyatli o\'chirildi.")
    else:
        print(" Bunday nomdagi kitob topilmadi.")


while True:
    print('kitoblar ustidagi amlga xush kelibsiz:')
    print("1. Yangi kitob qo'shish")
    print("2. Kitob yangilash")
    print("3. o'chirish")
    print("4. chiqish")
     
    tanlov=input('Tanlang 1/2/3/4 : ')
    if tanlov=='1':
        adding_new_book()
    elif tanlov=='2':
        updating()
    elif tanlov=='3':
        deleting()
        print("Dastur yakunlandi.")
    elif tanlov=='4':
        print('dastur yakunlandi')
        break
    else:
        print("Noto\'g\'ri tanlov. Qaytadan urinib ko'ring.\n")

# Task: Movie Recommendation System
# Use this url http://www.omdbapi.com/ to fetch information about movies.
# Create a program that asks users for a movie genre and recommends a random movie from that genre.

import requests
import random

api_key = "875a1c0"
#url='http://www.omdbapi.com/?t={movie}&apikey={api_key}'


movie_list = [
    "Inception", "The Matrix", "The Godfather"
]
user_genre = input("Qanday janrdagi film tavsiya qilay? ... ").lower()

matching_movies=[]

for i in movie_list:
    url = f"http://www.omdbapi.com/?t={title}&apikey={api_key}"
    response=requests.get(url)
    data=response.json()

if data.get("Response") == "True":
    genres = data.get("Genre", "").lower()
    if user_genre in genres:
        matching_movies.append(data)

if matching_movies:
    chosen = random.choice(matching_movies)

    print(f"Title: {chosen['Title']}")
    print(f"Year: {chosen['Year']}")
    print(f"Genre: {chosen['Genre']}")
    print(f"IMDb Rating: {chosen['imdbRating']}")
    print(f"Plot: {chosen['Plot']}")
else:
    print(" Afsuski, bu janrga mos film topilmadi.")



