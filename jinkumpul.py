import load
import random

def run():
    
    # cek udh login blm
    # cek jin bukan
    load.bahan_bangunan() 
    load.data_bahan_bangunan[0] += random.randrange(1, 5)
    load.data_bahan_bangunan[1] += random.randrange(1, 5)
    load.data_bahan_bangunan[2] += random.randrange(1, 5)
    print("Jin menemukan", load.data_bahan_bangunan[0], "pasir, ", load.data_bahan_bangunan[1], "batu, dan", load.data_bahan_bangunan[2], "air")