'''Bir 100 metre koşucusu farklı günlerde yaptığı sürelerin kaydını tutmaktadır.
Kullanıcıdan süre sayısını ve süreleri alan; en küçük, en büyük ve ortalama
süreleri ekrana yazdıran Python kodunu yazınız. Ortalamayı yazdırırken ondalıklı
2 basamağa yuvarlamanız gerekmektedir. Örneğin 6.66666 değeri 6.67 biçiminde
yazdırılmalıdır. Yuvarlama için round fonksiyonunu kullanınız.
Örnek girdi ve çıktı aşağıda verilmiştir:
Girdi:
9
10.79
12.35
9.91
10.07
11.4
12.19
11.36
9.87
12.37
Çıktı:
9.87
12.37
11.15
'''



sayi = int(input('Girilecek Süre sayısını giriniz: '))

süreler = []

for i in range(sayi):
    süre = float(input('Girilen Sürelerin Kaydı: '))
    süreler.append(süre)

enküçük_süre = min(süreler)
enbüyük_süre = max(süreler)

ortalama = round(sum(süreler) / sayi, 2)

print(f"\nEn küçük süre:{enküçük_süre:} ")
print(f"\nEn büyük süre:{enbüyük_süre:} ")
print(f"Ortalama:{ortalama:.2f} ")

