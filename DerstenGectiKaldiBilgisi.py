#kullanıcıdan ad, vize ve final notunu al. İsmini, başarı notunu ve geçti/kaldı bilgisini yazdır
isim=input("isminizi giriniz:")
v=float(input("vize notunuzu giriniz:"))
f=float(input("final notunuzu giriniz:"))
ort=v*0.4+f*0.6

if ort>=60:
    bilgi="GEÇTİ"
else:
    bilgi="KALDI"
print("öğrencinin ismi:",isim)
print("öğrencinin ortalaması:",ort)
print("başarı bilgisi:",bilgi)