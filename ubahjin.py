Username = input("Masukkan username jin : ")
  
if csvColSearch ("user.csv","Username",Username) != -1: # Manggil fungsi csvColSearch yang di csvhandler.py sorry kalau salah pemakaiannya
    konfirmasi = input("Jin ini bertipe “" + csvElGet("user.csv","Role",csvColSearch("user.csv","Username",Username)) + "”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ")
    if konfirmasi == "Y":
      
        # Command untuk mengubah tipe jin tapi belum beres belum yakin cara akses kolom pada csv
        
        print("Jin telah berhasil diubah.")
else: # Tidak ada usernamenya dalam csv
    print("Tidak ada jin dengan username tersebut.")
