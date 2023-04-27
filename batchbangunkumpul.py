def batchbangun():
    if banyakjin_bangun == 0:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
    else:
        bahan_butuh = [[0,0,0] for i in range (banyakjin_bangun)]
        bahan_butuh_total = [0,0,0]
        kurang = [0,0,0]
        for i in range(banyakjin_bangun):
            bahan_butuh[i][0] = random.randrange(1, 5)
            bahan_butuh[i][1] = random.randrange(1, 5)
            bahan_butuh[i][2] = random.randrange(1, 5)

            bahan_butuh_total[0] += bahan_butuh[i][0]
            bahan_butuh_total[1] += bahan_butuh[i][1]
            bahan_butuh_total[2] += bahan_butuh[i][2]

        if bahan_butuh[0] > data_bahan_bangunan[0]:
            kurang[0] = bahan_butuh[0] - data_bahan_bangunan[0]
        if bahan_butuh[1] > data_bahan_bangunan[1]:
            kurang[1] = bahan_butuh[1] - data_bahan_bangunan[1]
        if bahan_butuh[2] < data_bahan_bangunan[2]:
            kurang[2] = bahan_butuh[2] - data_bahan_bangunan[2]   
            
        
        print("Mengerahkan", banyakjin_bangun, "jin untuk membangun candi dengan total bahan", bahan_butuh_total[0], "pasir,", bahan_butuh_total[1], "batu, dan", bahan_butuh_total[2], "air.")
        print("Jin berhasil membangun total,", banyakjin_bangun, "candi.")   
        
        if kurang[0] + kurang[1] + kurang[2] > 0:
            print("Bangun gagal. Kurang", kurang[0], "pasir, ", kurang[1], "batu, ", kurang[2], "air.")
        
        
            
        candi[jumlah_candi][0] = jumlah_candi + 1
        candi[jumlah_candi][1] = usernamejin
        candi[jumlah_candi][2] = pasir
        candi[jumlah_candi][3] = batu
        candi[jumlah_candi][4] = air
        
def batchkumpul():
    if banyakjin_kumpul == 0:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    else:
        bahan_butuh = [[0,0,0] for i in range (banyakjin_bangun)]
        bahan_butuh_total = [0,0,0]
        
        for i in range(banyakjin_bangun):
            bahan_butuh[i][0] = random.randrange(1, 5)
            bahan_butuh[i][1] = random.randrange(1, 5)
            bahan_butuh[i][2] = random.randrange(1, 5)

            bahan_butuh_total[0] += bahan_butuh[i][0]
            bahan_butuh_total[1] += bahan_butuh[i][1]
            bahan_butuh_total[2] += bahan_butuh[i][2]
            
        print("Mengerahkan", banyakjin_bangun, "jin untuk mengumpulkan bahan.")
        print("Jin menemukan total", bahan_butuh_total[0], "pasir, ", bahan_butuh_total[1], "batu, dan", bahan_butuh_total[2], "air.")
    