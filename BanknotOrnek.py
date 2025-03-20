#bir bankada 10-20-50-100-200 lük banknotlar bulunmaktadır.kullanıcıdan çekmek istediği para miktarını alıp banknot miktarı en az olacak şekilde veren kod.
para = int(input("Bir miktar giriniz:"))
while True:
    if para % 10 == 0:
        adet = para / 200
        para= para % 200 
        print("200'lük banknot",int(adet))
        adet= para / 100
        para = para % 100
        print("100'lük banknot",int(adet))
        adet = para / 50 
        para = para % 50
        print("50'lik banknot",int(adet))
        adet = para / 20
        para = para % 20
        print("20'lik banknot",int(adet))
        adet = para /10
        para = para % 10
        print("10'luk banknot",int(adet))
        break
    else:
        print("10'un katı bir sayı giriniz.")
        para = int(input("Bir miktar giriniz:"))