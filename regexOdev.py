#Aşağıdaki s stringi için regex ifadelerini ve sonuçlarını yazınız?

s = "No. Wrong. Choice is an illusion, created between those with power, and those without. This is the nature of the universe. We struggle against it, we fight to deny it, but it is of course pretense, it is a lie. Beneath our poised appearance, the truth is we are completely out of control. Causality. There is no escape from it, we are forever slaves to it. Our only hope, our only peace is to understand it, to understand the 'why'. 'Why' is what separates us from them, you from me. 'Why' is the only real social power, without it you are powerless. And this is how you come to me, without 'why', without power. Another link in the chain."


#1. Kaç adet boşluk vardır? Regex ifesedesini yazınız?
#2. why/Why sözcüklarinin adetini bulan regex ifadesini yazınız?
#3. Nokta sayısını bulan regex ifadesini yazınız?
#4. Causality kelimesinin konumunu bulunuz? (re.search())
#5. Tüm why/Why kelimelerinin yerine casuality yazdınırız? (replace)
#6. Tüm sözcükleri boşluktan parçalıyınız? (split)
#7. a = re.findall("i.",s)  -> a dizisinde neler listelenir?
#8. a = re.findall("[aonudr]{3}",s) -> a dizisinde neler listelenir?
#9. a = re.findall(r'"(.*?)"', s) -> a dizisinde neler listelenir?
#10. Virgül sayısını bulan regex ifadesini yazınız?


import re
#1. soru
a= re.findall("\s",s)
print("boşluk sayısı:",len(a))

#2. soru
a=re.findall("[Wwhy]{3}",s)
print("Why/why kelimelerinin sayısı:",len(a))

#3. soru
a=re.findall("[.]",s)
print("nokta sayısı:",len(a))

#4. soru
a=re.search("Causality",s)
print("'Causality' kelimesinin konumu:",a)

#5. soru
a=re.sub("[Wwhy]{3}","causality",s)
print(a)

#6. soru
a=re.split("[\s]",s)
print(a)

#7. soru
a = re.findall("i.",s) # ilk harfi i olan iki harfli olan tüm kelimeler 

#8. soru
a = re.findall("[aonudr]{3}",s)  # içerisinde aonudr harfleri olan 3 harfli kelimeler
print(a)

#9. soru
a = re.findall("(.*?)", s)  #???? bunu anlamadım
print(a)

#10. soru
a=re.findall("[,]",s)
print("virgül sayısı:",len(a))