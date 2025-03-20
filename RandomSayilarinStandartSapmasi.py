#  Sıfır ile 100 arasında rastgele 10000 sayı üretip bir diziye atınız, bu sayıların standart sapmalarını hesaplayınız?
import random
import math
dizi = []
adet = 10000
for i in range (0,10001) :
     dizi.append(random.randint(0,100))
toplam = 0
for i in dizi:
    toplam += i
print (" toplam= ", toplam)
ort = toplam / adet
print("ortalama = ", ort)
formultoplam = 0
for i in dizi :
    fark = i-ort
    fark = fark** 2
    formultoplam += fark
a = formultoplam / adet
ssapma = math.sqrt(a)
print ("standart sapma =" , ssapma)








