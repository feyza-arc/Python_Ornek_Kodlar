#kullanıcıdan bir metin al. Bu metinde kaç harf, kaç rakam ve kaç boşluk olduğunu göster
m=(input("bir metin giriniz:"))
harf_sayac=0
rakam_sayac=0
bosluk_sayac=0
for i in m:
    if i.isalpha():
        harf_sayac+=1
    elif i.isdigit():
        rakam_sayac+=1
    elif i.isspace():
        bosluk_sayac+=1
    
print("metindeki harf sayısı=",harf_sayac)
print("metindeki rakam sayısı=",rakam_sayac)
print("metindeki boşluk sayısı=",bosluk_sayac)





