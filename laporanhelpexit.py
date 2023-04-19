import globalvar
import dynamic_array as DA
import csv_handler as CS

def myStrIn(str, el) :
    for i in range(len(str)) :
        if el == str[i] :
            return True
    return False

def candi_madeby(namajin) :
    # butuh :
    # panjang data candi
    # akses ke data candi
    counter = 0
    for i in range(globalvar.candi_data.size) :
        if globalvar.candi_data.content[i][0] == namajin :
            counter += 1
    return counter

def get_harga_candi(id) :
    rowid = CS.csvColSearch(globalvar.candi_data, "id", str(id))
    datacandi = globalvar.candi_data.content[rowid]
    return 10000 * int(datacandi[2]) + 15000 * int(datacandi[3]) + 7500 * int(datacandi[4])

def laporanjin() : # F9
    # ~ Kebutuhan Fungsi ~

    # Variabel
    # loggedin : berisi boolean apakah sudah ada user yang login atau belum
    # role : berisi role dari user yang terlogin
    # length_userdata : jumlah data yang tersimpan pada data user
    # kolomrole dan kolomusername : Index yang menunjukkan kolom data tersebut apabila csv diload dalam struktur data matriks
    #                               (apabila tidak dapat disesuaikan)

    if not globalvar.loggedin :
        print("Login terlebih dahulu sebelum menggunakan command!")
        return

    if globalvar.role != "bandung_bondowoso" :
        print("Anda tidak berhak untuk mendapat laporan jin!")
        return
    
    counter_jink = 0
    counter_jinb = 0

    jin_rajin = ""
    jin_malas = ""

    rajin_count = 0
    malas_count = 0

    for i in range(globalvar.user_data.size) :
        if globalvar.user_data.content[i][2] == "jin_pengumpul" :
            counter_jink += 1
        elif globalvar.user_data.content[i][2] == "jin_pembangun" :
            counter_jinb += 1
            candi_built = candi_madeby(globalvar.user_data.content[i][1])
            uname_jin = globalvar.user_data.content[i][0]
            if candi_built > rajin_count :
                jin_rajin = uname_jin
                rajin_count = candi_built
            elif candi_built == rajin_count and (uname_jin < jin_rajin or jin_rajin == "") :
                jin_rajin = uname_jin
                rajin_count = candi_built
            if candi_built < malas_count :
                jin_malas = uname_jin
                malas_count = candi_built
            elif candi_built == malas_count and (uname_jin > jin_malas or jin_malas == "") :
                jin_malas = uname_jin
                malas_count = candi_built

    print(f'Total jin: {globalvar.user_data.size - 2}')
    print(f'Total Jin Pengumpul: {counter_jink}')
    print(f'Total Jin Pembangun: {counter_jinb}')
    if counter_jinb == 0 :
        print(f'Jin Terajin: -')
        print(f'Jin Termalas: -')
    else :
        print(f'Jin Terajin: {jin_rajin}')
        print(f'Jin Termalas: {jin_malas}')
    print(f'Jumlah Pasir: {globalvar.jumlah_pasir()}')
    print(f'Jumlah Batu: {globalvar.jumlah_batu()}')
    print(f'Jumlah Air: {globalvar.jumlah_air()}')

def laporancandi() : #F10
     # ~ Kebutuhan Fungsi ~

    # Variabel
    # loggedin : berisi boolean apakah sudah ada user yang login atau belum
    # role : berisi role dari user yang terlogin
    # length_candidata : jumlah data yang tersimpan pada data user
    # candidata : hasil load file csv candi
    # kolompasir, batu, air : Index yang menunjukkan kolom data tersebut apabila csv diload dalam struktur data matriks
    #                         (apabila tidak dapat disesuaikan)

    if not globalvar.loggedin :
        print("Login terlebih dahulu sebelum menggunakan command!")
        return

    if globalvar.role != "bandung_bondowoso" :
        print("Anda tidak berhak untuk mendapat laporan candi!")
        return

    t_candi = 0
    t_pasir = 0
    t_batu = 0
    t_air = 0
    id_mahal = -1
    id_murah = -1
    harga_mahal = 0
    harga_murah = 0

    for i in range(1, globalvar.candi_data.size) :
        datacandi = globalvar.candi_data.content[i]
        t_candi += 1
        t_pasir += int(datacandi[2])
        t_batu += int(datacandi[3])
        t_air += int(datacandi[4])

        id = globalvar.candi_data.content[i][0]

        if get_harga_candi(id) > harga_mahal :
            harga_mahal = get_harga_candi(id)
            id_mahal = id
        elif get_harga_candi(id) < harga_murah or id_murah == -1 :
            harga_murah = get_harga_candi(id)
            id_murah = id

    print(f'Total Candi: {t_candi}')
    print(f'Total Pasir yang digunakan: {t_pasir}')
    print(f'Total Batu yang digunakan: {t_batu}')
    print(f'Total Air yang digunakan: {t_air}')

    if t_candi > 0 :
        print(f'ID Candi Termahal: {id_mahal} (Rp {harga_mahal})')
        print(f'ID Candi Termurah: {id_murah} (Rp {harga_murah})')
    else :
        print(f'ID Candi Termahal: -')
        print(f'ID Candi Termurah: -')

def help() : # F15
    # Butuh : variabel loggedin yang menunjukkan status program (sudah ter login atau belum)
    #         variabel role yang menunjukkan role user yang terlogin saat itu
    if not globalvar.loggedin :
        print("="*8 + " HELP " + "="*8)
        print("1. login \n Command untuk login ke akun yang sudah terdaftar")
    else :
        if globalvar.role == "bandung_bondowoso" :
            print("="*8 + " HELP " + "="*8)
            print("1. logout \n Command untuk logout/keluar dari akun")
            print("2. summonjin \n Command untuk men-summon satu jin")
            print("3. hapusjin \n Command untuk menghilangkan salah satu jin")
            print("4. ubahjin \n Command untuk mengubah tipe dari salah satu jin")
            print("5. batchkumpul \n Command untuk mengarahkan seluruh jin pengumpul untuk mengumpulkan bahan bangunan")
            print("6. batchbangun \n Command untuk mengarahkan seluruh jin pembangun untuk membangun candi")
            print("7. laporanjin \n Command untuk mendapatkan laporan mengenai pasukan jin Anda")
            print("8. laporancandi \n Command untuk mendapatkan laporan mengenai progress pembuatan candi")
            print("9. save \n Command untuk menyimpan progress ke dalam file eksternal")
            print("10. exit \n Command untuk keluar dari program")
        elif globalvar.role == "jin_pembangun" :
            print("="*8 + " HELP " + "="*8)
            print("1. logout \n Command untuk logout/keluar dari akun")
            print("2. bangun \n Command untuk membangun sebuah candi")
            print("3. exit \n Command untuk keluar dari program")
        elif globalvar.role == "jin_pengumpul" :
            print("="*8 + " HELP " + "="*8)
            print("1. logout \n Command untuk logout/keluar dari akun")
            print("2. kumpul \n Command untuk mengumpulkan bahan-bahan pembuatan candi")
            print("3. exit \n Command untuk keluar dari program")
        elif globalvar.role == "roro_jonggrang" :
            print("="*8 + " HELP " + "="*8)
            print("1. logout \n Command untuk logout/keluar dari akun")
            print("2. hancurkancandi \n Command untuk menghancurkan salah satu candi")
            print("3. ayamberkokok \n Command untuk mengkokokkan ayam")
            print("4. save \n Command untuk menyimpan progress ke dalam file eksternal")
            print("5. exit \n Command untuk keluar dari program")


def gameexit() : # F16
    # Butuh : command save
    askSave = "a"

    while (not myStrIn("YyNn", askSave)) or (not len(askSave) == 1) :
        askSave = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
    
    if myStrIn("Yy", askSave) :
        # ~ Command save di sini ~
        pass
    exit()