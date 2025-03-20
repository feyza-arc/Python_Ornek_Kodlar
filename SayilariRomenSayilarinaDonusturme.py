#kullanıcıdan 0-100 ars sayı alıp sayının roma rakamlarıyla karşılığını yazan kod
sayi = input("0-100 arasında bir sayı giriniz:")
r_birler ={1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",0:""}
r_onlar ={1:"X",2:"XX",3:"XXX",4:"XL",5:"L",6:"LX",7:"LXX",8:"LXXX",9:"XC",0:""}

if int(sayi) >= 10 and int(sayi) < 100:
    onlar= int(sayi[0])
    birler= int(sayi[1])
    print(r_onlar[onlar] , r_birler[birler])
if int(sayi) <10 :
    birler= int(sayi[0])
    print (r_birler[birler])
