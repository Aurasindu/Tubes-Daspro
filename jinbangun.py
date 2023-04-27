import random


def run():
    pasir = random.randrange(1, 5)
    batu = random.randrange(1, 5)
    air = random.randrange(1, 5)
    if pasir < data_bahan_bangunan[0]:
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")
    elif batu < data_bahan_bangunan[1]:
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")
    elif air < data_bahan_bangunan[2]:
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")
    elif jumlah_candi == 100:
        print("Candi berhasil dibangun.")
        print("Sisa candi yang perlu dibangun: 0")
    else:
        print("Candi berhasil dibangun.")
        print("Sisa candi yang perlu dibangun", 100-jumlah_candi)
        data_bahan_bangunan[0] -= pasir
        data_bahan_bangunan[1] -= batu
        data_bahan_bangunan[2] -= air
    
    candi[jumlah_candi][0] = jumlah_candi + 1
    candi[jumlah_candi][1] = usernamejin
    candi[jumlah_candi][2] = pasir
    candi[jumlah_candi][3] = batu
    candi[jumlah_candi][4] = air







