from random import randint
 
rastgelesayi=randint(1, 100)
sayac=0
 
while True:
    sayac+=1
    sayi=int(input("1 ile 100 arasında değer girin (0 Çıkış):"))
    if(sayi==0):
        print("Oyunu İptal Ettiniz")
        break
    elif sayi < rastgelesayi:
        print("Daha yüksek bir sayı girin.")
        continue
    elif sayi > rastgelesayi:
        print("Daha düşük bir sayı girin.")
        continue
    else:
        print("Tebrikler doğru tahmin ettiniz!")
        print("Tutulan Sayı: {0}!".format(rastgelesayi))
        print("{0} kez tahminde  bulundunuz.".format(sayac))
