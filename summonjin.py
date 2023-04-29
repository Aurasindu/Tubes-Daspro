print("Jenis jin yang dapat dipanggil:")
print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
print(" (2) Pembangun - Bertugas membangun candi")
 
Nomor = int(input("Masukkan nomor jenis jin yang dipanggil: "))

# Mengeluarkan kata-kata awal saja karena prosedurnya sama
def kataAwal(nomor):
    if nomor == 1:
        print("Memilih jin “Pengumpul”.")
    elif nomor == 2:
        print("Memilih jin “Pembangun”.")

# Mencari apakah usernamenya sudah diambil atau belum
def ketemu(username):
    if csvColSearch ("user.csv","Password",username) != -1: # Manggil fungsi csvColSearch yang di csvhandler.py sorry kalau salah pemakaiannya
        return True
    else:
        return False

# Menentukan apakah sudah ada 100 jin atau nggak
def jumlahJin("file"): # Belum beres belum tahu cara melihat banyaknya baris dalam file csv
      
# Program Utama
if jumlahJin("user.csv") <= 100:
  if Nomor == 1 or Nomor == 2:
        kataAwal(Nomor) # Panggil prosedur pengeluaran kata-kata awal

        Username = input("Masukkan username jin: ")

        # Mencari apakah usernamenya sudah diambil atau belum
        while ketemu(Username): # Selama usernamenya masih ketemu di csv minta password terus
            print("Username “" + Username + "” sudah diambil!")
            Username = input("Masukkan username jin: ")

        # Ketika username baru dan tidak ada di csv mau ditambahkan ke csv
        csvAppend("user.csv",Username) # panggil csv append untuk masukin ke csv baru sorry kalau salah pemakaian juga

        Password = input("Masukkan password jin: ")

        # Selama passwordnya tidak memasuki kriteria panjangnya antara 5 dan 25
        while len(Password) < 5 or len(Password) > 25:
            print("Password panjangnya harus 5-25 karakter!")
            Password = input("Masukkan password jin: ")

        # Ketika password sudah menemui kriteria
        print("Mengumpulkan sesajen...")
        print("Menyerahkan sesajen...")
        print("Membacakan mantra...")
        print("")
        print("Jin " + Username + " berhasil dipanggil!")

  else: # Kalau nomor yang dimasukkan pertama kali bukan 1 atau 2
        print("Tidak ada jenis jin bernomor “" + Nomor + "”!")
else: # Kalau sudah ada 100 jin
  print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
        

      
