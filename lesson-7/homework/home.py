#1. is_prime(n) funksiyasi
#is_prime(n) funksiyasini hosil qiling (n > 0). Agar n soni tub bo'lsa True, aks holda False qiymat qaytarsin.

#Misollar:
#Kiritish:
#4
#Natija:
#False
#(Izoh: 4 soni tub emas, chunki u 2 ga bo'linadi.)

#Kiritish:
#7
#Natija:
#True
#(Izoh: 7 soni faqat 1 va o'ziga bo'linadi, ya'ni tub son.)

def is_prime(n):
    if n<2:
        return False
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

is_prime(44)

    

#2. digit_sum(k) funksiyasi
#digit_sum(k) funksiyasini yozing, u k sonining raqamlari yig'indisini hisoblaydi.

#Misollar:
#Kiritish:
#24
#Natija:
#6
#(Izoh: 24 sonining raqamlari yig'indisi: 2 + 4 = 6.)

#Kiritish:
#502
#Natija:
#7
#(Izoh: 502 sonining raqamlari yig'indisi: 5 + 0 + 2 = 7.)



def digit_sum(k):
    return sum(int(i) for i in str(k))

digit_sum(12)



#3. Ikki sonning darajalari
#Berilgan N sonidan oshmaydigan barcha 2 ning darajalarini (ya'ni, 2**k shaklidagi sonlarni) chop etuvchi funksiyani yozing.

#Misol:
#kiritish:
#10
#Natija:
#2 4 8
#(Izoh: 10 dan kichik yoki teng bo'lgan 2 ning darajalari: 2, 4, 8.)


def daraja(n):
    for i in range (1,n+1):    
        if 2**i<n:
            print (2**i, end=" ")

daraja(22)
    

