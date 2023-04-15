jumlah_candi = 6
data_candi = [[['' for k in range(10)] for j in range(5)]for i in range(jumlah_candi)]
data_bahan_bangunan = [2, 4, 6]

def candi():
    global jumlah_candi
    global data_candi
    for i in range(4):
        for j in range(5):
            data_candi[i][j] = input()
        print("----")
    jumlah_candi = 4
    
def bahan_bangunan():
    global data_bahan_bangunan

