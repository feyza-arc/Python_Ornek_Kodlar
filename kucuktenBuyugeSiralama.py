#kullanıcıdan 3 sayı al. bu sayıları küçükten büyüğe sırala
a=int(input("1. sayı="))
b=int(input("2. sayı="))
c=int(input("3. sayı="))

if a<b<c:
    print("küçükten büyüğe doğru sıralama",a,"-", b,"-",c)
elif a<c<b:
    print("küçükten büyüğe doğru sıralama",a,"-", c,"-",b)
elif b<c<a:
    print("küçükten büyüğe doğru sıralama",b,"-", c,"-",a)
elif b<a<c:
    print("küçükten büyüğe doğru sıralama",b,"-", a,"-",c)
elif c<a<b:
    print("küçükten büyüğe doğru sıralama",c,"-", a,"-",b)
else:
    print("küçükten büyüğe doğru sıralama",c,"-", b,"-",a)