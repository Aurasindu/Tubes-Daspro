import argparse
import os

import globalvar
import laporanhelpexit as LHE

def getInput() :
    return input(">>> ")

def load() :

    parser = argparse.ArgumentParser()
    parser.add_argument("folder_path", nargs='?', default = None)
    args = parser.parse_args()
    
    folder_path = args.folder_path

    if folder_path == None :
        print("\nTidak ada nama folder yang diberikan!")
        print("\nUsage: python main.py <nama_folder>")
        exit()

    folder_path = "save/" + folder_path

    # folder_path = "save/tes2"

    if not os.path.isdir(folder_path) :
        print(f'Folder "{folder_path}" tidak ditemukan.')
        exit()

    globalvar.init(folder_path + "/user.csv", folder_path + "/candi.csv", folder_path + "/bahan_bangunan.csv", "", "")

    print('Selamat datang di program "Manajerial Candi"')
    print('Gunakan command "help" untuk bantuan')

load()
while True :
    cmd = getInput()

    if cmd == "login" :
        pass
        # pending
    elif cmd == "logout" :
        # pending
        pass
    elif cmd == "summonjin" :
        # pending
        pass
    elif cmd == "hapusjin" :
        # pending
        pass
    elif cmd == "ubahjin" :
        # pending
        pass
    elif cmd == "bangun" :
        # pending
        pass
    elif cmd == "kumpul" :
        # pending
        pass
    elif cmd == "batchbangun" :
        # pending
        pass
    elif cmd == "batchkumpul" :
        # pending
        pass
    elif cmd == "laporanjin" :
        LHE.laporanjin()
    elif cmd == "laporancandi" :
        LHE.laporancandi()
    elif cmd == "hancurkancandi" :
        # pending
        pass
    elif cmd == "ayamberkokok" :
        # pending
        pass
    elif cmd == "save" :
        # pending
        pass
    elif cmd == "help" :
        LHE.help()
    elif cmd == "quit" or cmd == "exit" or cmd == "stop" :
        LHE.gameexit()
    elif cmd == "custom" : # ini buat testing aja
        exec(input())