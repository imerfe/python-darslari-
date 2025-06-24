#Circle Class
#Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

class circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def yuza(self):
        return circle.pi*(self.radius**2)
    def perimetr(self):
        return 2*circle.pi*self.radius
    def __str__(self):
        return f'doira radiuse:{self.radius}'

circle1=circle(12)
print(circle1)
print(f'yuza:{circle1.yuza()}')
print(f'perimetr:{circle1.perimetr()}')

  
#Person Class
#Write a Python program to create a Person class. 
# Include attributes like name, country, and date of birth. 
# Implement a method to determine the person's age.
from datetime import date
class PERSON:
    today=date.today()
    c_year=today.year

    def __init__(self,name,country,date_of_birth):
        self.name=name
        self.country=country
        self.date_of_birth=date_of_birth 

    def age(self):
        return PERSON.c_year-self.date_of_birth
    
    def __str__(self):
        return f"{self.name} from {self.country}.Age={self.age()}" 
    
person_1=PERSON('mirzobek','uzb',2004)
print(person_1)


#Calculator Class
#Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.

class Calculator:
    def __init__(self,value):
        self.value=value
    def k(self):
        return self.value**2
    def b(self):
        return self.value//self.value**0.5
    def ildiz(self):
        return self.value**0.5
    def __str__(self):
        return f'{self.value} kvadrati={self.k()},bolinmasi={self.b()},ildiz_chiqarilsa={self.ildiz()}'
    
cal1=Calculator(100)
print(cal1)



#Shape and Subclasses
#Write a Python program to create a class that represents a shape.
#  Include methods to calculate its area and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.

class shape:
    pi=3.14
    def area(self):
        return 0
    def perimetr(self):
        return 0
    def __str__ (self):
        return 'bu shakllar uchun umumiy shablon ekan'
    

class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return shape.pi*(self.radius**2)
    def perimetr(self):
        return 2*shape.pi*self.radius
    def __str__(self):
        return f'doira yuzi={self.area()} va uning perimetri={self.perimetr()}'

class uchburchak(shape):
    def __init__(self, asos, balandlik, side1, side2):
        self.asos=asos
        self.balandlik=balandlik
        self.side1=side1
        self.side2=side2
    def area(self):
        return (self.asos*self.balandlik)/2
    def perimetr(self):
        return self.side1+self.side2+self.asos
    def __str__(self):
        return f'uchburchak yuzi={self.area()} va uning perimetri={self.perimetr()}'
    
class kvadrat(shape):
    def __init__(self,a):
        self.a=a
    def area(self):
        return self.a**2
    def perimetr(self):
        return 4*self.a
    def __str__(self):
        return f'kvadrat yuzi={self.area()} va uning perimetri={self.perimetr()}'
    


d1 = circle(5)
k1 = kvadrat(4)
u1 = uchburchak(6, 4, 5, 6)

shapes = [d1, u1, k1]

for i in shapes:
    print(i)
    print(f'{i.area()}')
    print(f'{i.perimetr()}')



# Stack Data Structure
class Stack:
    def __init__(self, items=None):
        if items is None:
            self.items = []
        else:
            self.items = items

    def push(self, item):
        self.items.append(item)
        print(f'{item} stackga qo‘shildi')

    def pop(self):
        if not self.items:
            print("stack bo'm-bo'sh")
            return None
        return self.items.pop()

    def peek(self):
        if not self.items:
            print("Stack bo‘sh! Hech narsa yo‘q.")
            return None
        return self.items[-1]

    def check(self):
        if len(self.items) == 0:
            return 'stack empty'
        else:
            return self.items

    def size(self):
        return len(self.items)

    def display(self):
        if not self.items:
            print("stack bo‘sh")
        else:
            print("Stack (top -> bottom):")
            for i in reversed(self.items):
                print(i)


# Stack obyektini yaratamiz
stack1 = Stack()

# Elementlar qo‘shamiz
stack1.push(10)
stack1.push(20)
stack1.push(30)

# Stackni ko‘rsatamiz
stack1.display()

# Elementni olib tashlaymiz
stack1.pop()

# Stackni qaytadan ko‘rsatamiz
stack1.display()

# Eng yuqoridagi elementni ko‘ramiz
print("Eng ustidagi element:", stack1.peek())

# Stack bo‘shmi?
print("Stack bo‘shmi?", stack1.check())

# Stackdagi elementlar soni
print("Elementlar soni:", stack1.size())


#Linked List Data Structure
#Write a Python program to create a class representing a linked list data structure. 
#Include methods for displaying linked list data, inserting, and deleting nodes.

class NODE:
    def __init__(self, data):
        self.data = data
        self.next = None

class LINKEDLIST:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" --> ")
            current = current.next
        print("None")  # ro'yxat tugaganini ko'rsatadi

    def insert_at_end(self, data):
        new_node = NODE(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_node(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print(f"{key} topilmadi.")
            return

        prev.next = current.next
ll = LINKEDLIST()

# Tugunlar qo‘shamiz
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)

print("Boshlang‘ich ro‘yhat:")
ll.display()  # 10 --> 20 --> 30 --> None

# Bitta tugunni o‘chiramiz
ll.delete_node(20)

print("20 o‘chirilgandan keyin:")
ll.display()  # 10 --> 30 --> None

# O‘chirib bo‘lmaydigan elementni sinaymiz
ll.delete_node(99)  # 99 topilmadi.

# Yana bir tugun qo‘shamiz
ll.insert_at_end(40)

print("Yangi tugun 40 qo‘shilgandan keyin:")
ll.display()  # 10 --> 30 --> 40 --> None

#Shopping Cart Class
#Write a Python program to create a class representing a shopping cart.
#  Include methods for adding and removing items, and calculating the total price.

class shopping_cart:
    def __init__(self):
        self.items=[]
    def add_item(self,name,price):
        self.items.append((name,price))
    def remove_item(self,name):
        for item in self.items:
            if item is None:
                return print(f"{self.name} is not available") 
            else:
                self.items.remove(name)
    def display(self):
        for item in self.items:
            print(f"names={item[0]} and price={item[1]}")
        if not self.items:
            print("savat bo'sh")
    def solver(self):
        return sum(price for self.name,price in self.items)
        
cart = shopping_cart()
cart.add_item("olma", 5000)
cart.add_item("non", 3000)
cart.add_item("shakar", 7000)

cart.display()

print("Umumiy narx:", cart.solver())

#Stack with Display
#Write a Python program to create a class representing a stack data structure.
#Include methods for pushing, popping, and displaying elements.

class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)
        print(f"{item} stackga qoshildi")

    def pop(self):
        if not self.data:
            print("stack bo'm-bo'sh")
            return None
        return self.data.pop()

    def display(self):
        if not self.data:
            print("stack bom-bosh")
            return
        print("Stackdagi elementlar:")
        for item in self.data:
            print(f"item = {item}")

# Sinov
c1 = Stack()
c1.push('olma')
c1.push('anor')
c1.push('olcha')
c1.push('orik')
c1.push('kashnich')

c1.display()

#Queue Data Structure
#Write a Python program to create a class representing a queue data structure.
#Include methods for enqueueing and dequeueing elements.

class Queue:
    def __init__(self):
        self.data = []

    def empty(self):
        return len(self.data) == 0

    def enqueue(self, item):
        self.data.append(item)
        print(f'{item} navbatga qoshildi')

    def dequeue(self):
        if self.empty():
            print('Navbat bosh')
        else:
            removed = self.data.pop(0)
            print(f'{removed} olib tashlandi')
            return removed

    def display(self):
        if self.empty():
            print('Navbat bosh')
        else:
            print("Navbatdagilar:")
            for item in self.data:
                print(item)


q = Queue()

q.enqueue("Ali")
q.enqueue("Vali")
q.enqueue("Aziza")

q.dequeue()

q.display()
#Bank Class
#Write a Python program to create a class representing a bank. \
# Include methods for managing customer accounts and transactions.

class Bank:
    def __init__ (self):
        self.accounts={}
    def create_account(self,name,initial_balance):
        if name in self.accounts:
            print('account is already created')
        else:
            self.accounts[name]=initial_balance
            print(f'{name} uchun yangi {initial_balance} lik hisob yaratildi')
    def deposit(self,name,amount):
        if name in self.accounts:
            self.accounts[name]+=amount
            print(f"{amount} som {name} hisobiga qoshildi.")
        else:
            print(f"{name} nomli hisob topilmadi.")
    def withdraw(self,name,amount):
        if name in self.accounts:
            if self.accounts[name]>=amount:
                self.accounts[name]-=amount
                print(f"{amount} som {name} hisobidan yechib olindi.")
            else:
                print('hisobda mablag yetarli emas')
        print(f"{name} nomli hisob topilmadi.")
    def checking_balance(self,name):
        if name in self.accounts:
            print(f'{name} ning hisobidagi balance={self.accounts[name]}')
        else:
            print(f'{name} ning bankda hisob raqami mavjud emas')
    def display(self):
        if not self.accounts:
            print('bankda shoting yoq')
        else:
            print("Barcha mijozlar va balanslari:")
            for name, balance in self.accounts.items():
                print(f"{name}: {balance} so‘m")   



b = Bank()
b.create_account("Ali", 100000)
b.deposit("Ali", 50000)
b.withdraw("Ali", 20000)
b.checking_balance("Ali")

b.create_account("Vali", 70000)
b.display()
