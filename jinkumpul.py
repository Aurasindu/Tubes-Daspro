import random

def run():
    # cek udh login blm
    # cek jin bukan
    bahan_bangunan() 
    data_bahan_bangunan[0] += random.randrange(1, 5)
    data_bahan_bangunan[1] += random.randrange(1, 5)
    data_bahan_bangunan[2] += random.randrange(1, 5)
    print("Jin menemukan", data_bahan_bangunan[0], "pasir, ", data_bahan_bangunan[1], "batu, dan", data_bahan_bangunan[2], "air")