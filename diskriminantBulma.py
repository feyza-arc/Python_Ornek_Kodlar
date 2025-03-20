# Bir bilinmeyenli 2. dereceden denklemlerin çözümünü diskriminant yöntemi ile çözüp kök durumunu yazdıran kodlama
import math
a=int(input("a sayısını giriniz="))
b=int(input("b sayısını giriniz="))
c=int(input("c sayısını giriniz="))
diskriminant=b*b-4*a*c
if diskriminant==0:
    print("birbirine eşit iki kök var")
    kokler=(-b)/(2*a)
    print("kök1=kök2=",kokler)
elif diskriminant<0:
    print("denklemin reel kökü yok")
else:
    print("denklemin 2 farklı kökü var")
    kok1=-b+math.sqrt(diskriminant)/2*a
    print("kök1=",kok1)
    kok2=-b-math.sqrt(diskriminant)/2*a
    print("kök2=",kok2)

