print("Merhaba")
print("sayı tahmin oyunumuza hoşgeldiniz")
print("1 - 100 arasında bir sayı tutunuz")
while True:
    cevap = input("Tuttuysanız E/e basınız")
    if cevap =="e" or cevap =="E":
        break
print("Sayınızın bilinmesi halinde E/e tuşlarından birine basınız")
print("eğer tuttuğunuz sayı daha büyükse B/b")
print("eğer tuttuğunuz sayı daha küçükse K/k tuşunu cevap olarak giriniz")
kere,taban,tavan = 1,0,100
while True:
    sayi = int((taban + tavan) / 2)
    print("tuttuğunuz sayı : ",sayi)
    cevap = input("cevabınızı giriniz E(vet)-B(üyük)-K(üçük) ?")
    if cevap =="e" or cevap =="E":
        print("Sayınız",sayi)
        print("Sayınızı",kere," kere bildik")
        break
    elif cevap =="k" or cevap =="K":
        tavan = sayi
    elif cevap =="B" or cevap =="b":
        taban = sayi
    kere+=1