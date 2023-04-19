import csv_handler as CS

def init(ucsv, ccsv, bpcsv, uname, rol) :
    global user_data
    global candi_data
    global bahan_data
    global loggedin
    global user
    global role

    user_data = CS.opencsv(ucsv)
    candi_data = CS.opencsv(ccsv)
    bahan_data = CS.opencsv(bpcsv)
    loggedin = True
    user = uname
    role = rol

def jumlah_pasir() :
    return bahan_data.content[1][2]

def jumlah_batu() :
    return bahan_data.content[2][2]

def jumlah_air() :
    return bahan_data.content[3][2]

