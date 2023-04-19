import dynamic_array as DA

class CSV :
    # Tipe bentukan CSV dengan atribut
    # size : Integer
    # content : Matriks
    # column : Integer

    # size adalah jumlah baris pada matriks
    # content adalah isi data
    # column adalah jumlah kolom pada matriks
    
    def __init__ (self, sizeinp = 0, contentinp = [0 for i in range(0)], columninp = 0) :
        self.size = sizeinp
        self.content = contentinp
        self.column = columninp

def csvAppend(csv, el) :
    # fungsi csvAppend(csv, el) mengembalikan CSV csv dengan isinya ditambahkan elemen el
    rescontent = DA.myAppend(csv.content, el, csv.size)
    rescsv = CSV(csv.size + 1, rescontent, csv.column)
    return rescsv

def csvPlus(csv1, csv2) :
    # fungsi csvPlus(csv1, csv2) mengembalikan sebuah CSV yang berisi data dari csv1 dan csv2
    # dengan csv1 dan csv2 memiliki jumlah kolom yang sama
    res_content = DA.arrayPlus(csv1.content, csv1.size, csv2.content, csv2.size)
    return CSV(csv1.size + csv2.size, res_content, csv1.column)

def csvColSearch(csv, colname, el) :
    # fungsi csvColSearch(csv, colname, el) mengembalikan indeks baris pertama pada data csv memiliki elemen pada kolom colname
    # bernilai el atau mengembalikan -1 jika elemen tidak ditemukan
    id = DA.myIndex(csv.content[0], colname, csv.size)
    for i in range(csv.size) :
        if csv.content[i][id] == el :
            return i
    return -1

def csvElGet(csv, col, rowid) :
    # fungsi csvElGet(csv, col, rowid) mengembalikan isi elemen pada data csv pada kolom colname dan indeks baris rowid
    colid = DA.myIndex(csv.content[0], col, csv.column)
    return csv.content[rowid][colid]

def delEntry(csv, rowid) :
    # fungsi delEntry(csv, rowid) mengembalikan CSV csv dengan entry pada indeks rowid dihapuskan
    rescontent = DA.arrayPlus(DA.slicing(csv.content, 0, rowid), rowid, DA.slicing(csv.content, rowid + 1, csv.size), csv.size - rowid - 1)
    return CSV(csv.size - 1, rescontent, csv.column)

def line_to_array(line) :
    # fungsi line_to_array(line) mengembalikan array berisi representasi data dari sebuah string yang setiap elemennya terseparasi
    # oleh character ;
    res = []
    size = 0
    next_e = ""
    for i in range(len(line)) :
        if line[i] != ";" and i != len(line) - 1:
            next_e += line[i]
        else :
            res = DA.myAppend(res, next_e, size)
            next_e = ""
            size += 1

    return (res, size)

def array_to_line(arr, size) :
    # fungsi array_to_line(arr, size) mengembalikan string berisi representasi data dari sebuah array sebagai bentuk
    # string yang setiap elemennya terseparasi oleh karakter ;

    res = ""
    for i in range(size) :
        res += str(arr[i])
        res += ";"
    res += str(arr[size - 1])
    return res

def opencsv(file_name) :
    # fungsi opencsv(file_name) mengembalikan CSV yang berisi data dari sebuah file csv pada path file_name

    f = open(file_name, "r")
    
    start = True
    content = []
    size = 0
    for line in f :

        if start :
            column = line_to_array(line)[1]
            start = False

        content = DA.myAppend(content, line_to_array(line)[0], size)
        size += 1
    return CSV(size, content, column)

def savetocsv(csv, file_path) :
    # prosedur savetocsv(csv, file_path) akan membuat file dengan ekstensi .csv baru pada file_path yang memiliki
    # data pada csv

    f = open(file_path, 'w')
    for i in range(csv.size) :
        f.write(array_to_line(csv.content[i]))
        if i != csv.size - 1 :
            f.write("\n")

def dupecsv(csv) :
    # dupecsv(csv) akan menghasilkan csv yang sama persis dengan csv namun menduduki posisi yang berbeda pada memori

    dupecontent = [0 for i in range(csv.size)]
    for i in range(csv.size) :
        dupecontent[i] = csv.content[i]
    return CSV(csv.size, dupecontent, csv.column)


if __name__ == "__main__" :
    # Kode untuk keperluan testing
    csv1 = CSV(3, [[4,1,2,3],[4,2,3,1],[4,3,2,1]], 4)
    csv2 = CSV(2, [[2,1,2,4], [2,2,1,7]], 4)
    merged = csvPlus(csv1, csv2)
    print(merged.content)
    deled = delEntry(merged, 3)
    print(deled.content)