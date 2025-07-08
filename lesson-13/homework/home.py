
# Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.

#age in years, months, and days?

from datetime import date,datetime

birth=input('enter you birthdate(YYYY-MM-DD):')

birth_date=datetime.strptime(birth,'%Y-%m-%d').date()

current_date=date.today()

age=(current_date-birth_date)

year=(current_date.year-birth_date.year)
months=(current_date.month-birth_date.month)
days=(current_date.day-birth_date.day)

if days<0:
    months-=1
    days+=30
if months<0:
    months+=12
    year-=1





print(f'your full lived days are  {age}, since your birt you live {year} year,{months} months,{days} days')



# Days Until Next Birthday: Similar to the first exercise,
#  but this time, calculate and print the number of days remaining until the user's next birthday.

from datetime import datetime,date
inputted_value=input('enter your birthdate (MM-DD)')

converted=datetime.strptime(inputted_value,'%m-%d')
current_date=date.today()

days=abs(current_date.day-converted.day)
months=abs(current_date.month-converted.month)
print(f'kelasi tug\'ilgan kuninggacha {months} oy va {days} kun bor')


# Meeting Scheduler: Ask the user to enter the current date and time, 
# as well as the duration of a meeting in hours and minutes.
# Calculate and print the date and time when the meeting will end.

from datetime import date, datetime,timedelta
todays=input('enter the todays date (YYYY-MM-DD)and time (H:M):')
duration=input('enter the period of meeting in hours and minutes (H:M):')

converter=datetime.strptime(todays,'%Y-%m-%d %H:%M')
h,m=map(int, duration.split(":"))


delta=timedelta(hours=h,minutes=m)

print(f'hozirgi sana va vaqt {converter}')
print('siz ning uchrashuvingiz', converter+delta,'da tugaydi')

# Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, 
# and then convert and print the date and time in another timezone of their choice.

from datetime import datetime
import pytz

inputting=input('enter the date (YYYY-MM-DD) and time (H:M) according to your own timezone:')
region=input('enter where you are(America/New_York):')
converter=input('enter the zone which you want to convert the time:')

t=datetime.strptime(inputting,'%Y-%m-%d %H:%M')

tz_own=pytz.timezone(region)
local=tz_own.timezone(region)
tz_target = pytz.timezone(converter)
converted_t = local.astimezone(tz_target)

print(f"Time in your timezone ({region}): {local.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")
print(f"Time in target timezone ({converter}): {converted_t.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")





# from datetime import datetime
# import pytz

# # Foydalanuvchidan sanani, vaqtni va zonalarni olish
# inputting = input('Enter the date (YYYY-MM-DD) and time (H:M) according to your own timezone: ')
# region = input('Enter your current timezone (e.g., America/New_York): ')
# converter = input('Enter the timezone you want to convert to (e.g., Asia/Tashkent): ')

# # Stringni datetime formatiga aylantirish
# t = datetime.strptime(inputting, '%Y-%m-%d %H:%M')

# # Foydalanuvchi bergan zonani olish
# tz_own = pytz.timezone(region)

# # Naive datetime (ya'ni timezonedan xabarsiz) ni aware datetime ga aylantirish
# t_localized = tz_own.localize(t)

# # Target zonaga konvertatsiya
# tz_target = pytz.timezone(converter)
# converted_t = t_localized.astimezone(tz_target)

# # Natijani chiqarish
# print(f"\nTime in your timezone ({region}): {t_localized.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")
# print(f"Time in target timezone ({converter}): {converted_t.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")
# # Countdown Timer: Implement a countdown timer. 
# # Ask the user to input a future date and time,
# #  and then continuously print the time remaining until that point in regular intervals (e.g., every second).

from datetime import datetime, timedelta
import time

# Foydalanuvchidan vaqt + sana kiritishni so‘raymiz
inputting = input('Enter the future time and date (YYYY-MM-DD HH:MM:SS): ')

try:
    # Sana va vaqtni birga o‘qib olamiz
    future_time = datetime.strptime(inputting, '%Y-%m-%d %H:%M:%S')

    # Hozirgi vaqtni input'dan keyin olamiz
    now = datetime.now()
    print(f'Bugungi sana: {now.strftime("%Y-%m-%d %H:%M:%S")}')

    # Agar kelajak vaqti hozirdan oldin bo‘lsa, xatolik
    if future_time < now:
        print(" Siz o'tgan vaqtni kiritdingiz.")
    else:
        print("\n Countdown boshlangan...")
        while True:
            now = datetime.now()
            qolgan = future_time - now

            if qolgan.total_seconds() <= 0:
                print("\n Vaqt tugadi!")
                break

            print("Qolgan vaqt:", str(qolgan).split('.')[0], end='\r')
            time.sleep(1)

except ValueError:
    print(" Noto‘g‘ri format. To‘g‘ri kiriting: YYYY-MM-DD HH:MM:SS")
# Email Validator: Write a program that validates email addresses. 
# Ask the user to input an email address, and check if it follows a valid email format.


inp=input('enter your own email address')

a="@gmail.com"

if inp.endswith(a) and inp.count('@')==1:
    print("email is valid")
else:
    print('email is not valid')        
# Phone Number Formatter: Create a program that takes a phone number as input and 
# formats it according to a standard format. 
# For example, convert "1234567890" to "(123) 456-7890".

inp=input('enter your own phone number(contain 10 digits):')

if inp.isdigit() and len(inp)==10:
    code=inp[:3]
    area=inp[3:6]
    subs=inp[6:8]
    subs2=inp[8:10]

    print(f'formatted phone number is (+{code}) {area}-{subs}-{subs2}')
else:
    print('you are out of range or got the wrong path')

# Password Strength Checker: Implement a password strength checker.
#  Ask the user to input a password and check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).

inp=input('enter the pasword:')
symbols='!@#$%^&*()_+='
numbers='1234567890'
#the pasword length should be 10 

if len(inp)!=10:
    print('Your code should contain 10 character:')
else:
    upper=any(i.isupper() for i in inp)
    lower=any(i.islower() for i in inp)
    digit=any(i.isdigit() for i in inp)
    sym=any( i for i in symbols)

if upper and lower and digit and sym:
    print(" Password is strong and successfully created!")
else:
    if not upper:
        print('there is not any upper case word')
    if not lower:
        print('there is not any lower case word')
    if not digit:
        print('there is not any digit')
    if not sym:
        print('there is not any symbol')
    
print(f'your pasword is { inp }')

txt = input('enter the text:')
inputting = input('enter the specific word which you want to search:')

a = txt.split(' ')
sym = "!@#$%^&*()_+><,./\\'=`"
l = []

for i in a:
    c = i 
    for j in i:
        if j in sym:
            c = c.replace(j, "") 
    l.append(c) 

print('tozasi', l)

cnt=1

for inputting in l:
    cnt+=1


print(f'the occurence of {inputting} is {cnt} in given text ')
# Date Extractor: Write a program that extracts dates from a given text.
#  Ask the user to input a text, and then identify and print all the dates present in the text.



import re
import datetime
list=[]
txt=input('enter the text:')
patterns = [
    r'\d{2}-\d{2}-\d{4}',  
    r'\d{2} \d{2} \d{4}',  
    r'\d{2}/\d{2}/\d{4}']

for i in patterns:
    list+=re.findall(i,txt)
    


print(f'textda berilgan sanalar {list}')


