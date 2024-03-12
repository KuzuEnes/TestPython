"""
Bir bakkal ve çırağı 7/24 açık olan bakkalda vardiyalı olarak çalışmaktadır.
Bakkal, sınırlı sayıda müşteriye veresiye mal vermektedir ve bakkal ve
çırağı iki ayrı veresiye defteri tutmaktadır. Ay sonunda bakkal ve çırağı
veresiye defterlerini birleştirip her müşterinin borcunu hesaplamak istemektedir.
Bakkaldaki müşterilerin borcunu hesaplayacak ve alfabetik sırada ekrana
yazdıracak Python kodunu yazmanız istenmektedir. Programa önce bakkalın
defterindeki müşteri sayısı(ilk satır), sonra her bir müşterinin adı ve
borcu(aralarında boşluk olacak şekilde) satır satır girilmektedir. Daha
sonra çırağın defteri aynı biçimde girilmektedir. Programınız müşterilerin
borçlarını hesaplayıp ekrana alfabetik sırada, bakkal ve çırağın borçları
girdiği biçimde yazdırmalıdır. 

İpucu: Borçları iki ayrı sözlükte tutup birleştirebilirsiniz

Aşağıda programın örnek çalışması verilmiştir:

Girdi:
8
Pelin 250
Ibrahim 400
Riza 250
Kemal 350
Yasemin 100
Fatma 350
Umut 450
Hande 400
7
Fatma 300
Ahmet 350
Tolga 500
Ibrahim 50
Gul 100
Yasemin 350
Gokhan 500

Çıktı:
12
Ahmet 350
Fatma 650
Gokhan 500
Gul 100
Hande 400
Ibrahim 450
Kemal 350
Pelin 250
Riza 250
Tolga 500
Umut 450
Yasemin 450
"""


def veresiye_defteri(bakkal_defteri, cirak_defteri):
    tum_defter = dict(bakkal_defteri)
    for musteri, borc in cirak_defteri.items():
        if musteri in tum_defter:
            tum_defter[musteri] += borc
        else:
            tum_defter[musteri] = borc

    sirali_borclar = sorted(tum_defter.items(), key=lambda x: x[0])

    print(len(sirali_borclar))
    for musteri, borc in sirali_borclar:
        print(f"{musteri} {borc}")


bakkal_musteri_sayisi = int(input())
bakkal_defteri = {}
for _ in range(bakkal_musteri_sayisi):
    musteri, borc = input().split()
    bakkal_defteri[musteri] = int(borc)

cirak_musteri_sayisi = int(input())
cirak_defteri = {}
for _ in range(cirak_musteri_sayisi):
    musteri, borc = input().split()
    cirak_defteri[musteri] = int(borc)

veresiye_defteri(bakkal_defteri, cirak_defteri)