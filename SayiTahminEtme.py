#Bilgisayar 0 ile 100 arasında rastgele sayı üretsin, kullanıcı bir tahminde bulunsun eğer sayı küçükse "Yukarı" yazsın,
#  büyükse "Aşağı" yazsın.
import random
sayi= random.randint(0,100)
tahmin=int(input("0-100 arasında bir sayı tahmin ediniz="))
while True:
    if tahmin>sayi:
            print("daha KÜÇÜK bir sayı tahmin ediniz")
            tahmin=int(input("0-100 arasında bir sayı tahmin ediniz="))
            
    elif tahmin<sayi:
        print("daha BÜYÜK bir sayı tahmin ediniz")
        tahmin=int(input("0-100 arasında bir sayı tahmin ediniz="))
    else:
         print("TEBRİKLER DOĞRU TAHMİN ETTİNİZ")
         break
    

