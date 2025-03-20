vize = int(input("vize notunu gir "))
final = int(input ("final notunu gir"))
sonuc = (vize*40/100)+(final*60/100)
print(sonuc)

if sonuc >= 90 :
    print("AA")

elif sonuc >= 85:
    print("BA")

elif sonuc >= 75:
    print("BB")

elif sonuc >= 70 :
    print("CB")

elif sonuc >= 60:
    print("CC")

elif sonuc >= 55:
    print("DC")

elif sonuc >= 50 :
    print("DD")

elif sonuc >= 40 :
    print("FD")

elif sonuc >= 0:
    print("FF")

else :
    print("F")






