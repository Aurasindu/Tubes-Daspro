import load
import random


def run():
    for i in range(jumlahjin):
        load.candi() 
        load.bahan_bangunan() 
        jumlah_candi = load.jumlah_candi
        pasir = random.randrange(1, 5)
        batu = random.randrange(1, 5)
        air = random.randrange(1, 5)
        if pasir < load.data_bahan_bangunan[0]:
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")
        elif batu < load.data_bahan_bangunan[1]:
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")
        elif air < load.data_bahan_bangunan[2]:
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")
        elif load.jumlah_candi == 100:
            print("Candi berhasil dibangun.")
            print("Sisa candi yang perlu dibangun: 0")
        else:
            print("Candi berhasil dibangun.")
            print("Sisa candi yang perlu dibangun", 100-jumlah_candi)
            load.data_bahan_bangunan[0] -= pasir
            load.data_bahan_bangunan[1] -= batu
            load.data_bahan_bangunan[2] -= air
        
        candi[jumlah_candi][0] = jumlah_candi + 1
        candi[jumlah_candi][1] = jin[i]
        candi[jumlah_candi][2] = pasir
        candi[jumlah_candi][3] = batu
        candi[jumlah_candi][4] = air
        
        jumlah_candi += 1