    # Kullanıcıdn 0 ile 50 arasında 10 sayı alıp bir diziye atınız, bu sayıların toplamlarını ve ortalamalarını bulunuz
dizi=[]
toplam=0
sayaç=0

for i in range(10):
     sayilar=int(input("0-50 arasında 10 adet sayı giriniz="))
    
     while True:
        if sayilar>0 and sayilar<50:
             dizi.append(sayilar)
             toplam+=sayilar
             sayaç+=1
             break
        else:
            print("girdiğiniz sayı 0-50 aralığında değil")
            sayilar=int(input("0-50 arasında 10 adet sayı giriniz="))
            
print(dizi)
print("toplam=",toplam)
ort=toplam/sayaç
print("ortalama=",ort)