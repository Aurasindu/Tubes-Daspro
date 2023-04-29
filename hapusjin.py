Username = input("Masukkan username jin : ")
if csvColSearch ("user.csv","Username",Username) != -1: # Manggil fungsi csvColSearch yang di csvhandler.py sorry kalau salah pemakaiannya
    konfirmasi = input("Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? ")
    if konfirmasi == "Y":
      
        # Command untuk menghapus dari csv
        delEntry("user.csv",csvColSearch ("user.csv","Username",Username)) # manggil dua fungsi dari csvhandler.py sorry kalau salah juga pemakaiannya
        
        print("Jin telah berhasil dihapus dari alam gaib.")
else: # Tidak ada usernamenya dalam csv
    print("Tidak ada jin dengan username tersebut.")
