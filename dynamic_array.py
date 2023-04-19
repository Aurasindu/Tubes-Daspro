def myAppend(arr, el, size) :
    # fungsi myAppend(arr, el, size) mengembalikan array arr dengan ditambahkan elemen el di akhir array

    res = [0 for i in range(size + 1)]
    for i in range(size) :
        res[i] = arr[i]
    res[size] = el
    return res

def arrayPlus(arr1, size1, arr2, size2) :
    # fungsi arrayPlus(arr1, size1, arr2, size2) mengembalikan array berisi data arr1 dan arr2

    res = []
    ressize = 0
    for i in range(size1) :
        res = myAppend(res, arr1[i], ressize)
        ressize += 1
    for i in range(size2) :
        res = myAppend(res, arr2[i], ressize)
        ressize += 1
    return res

def myInArray(arr, el, size) :
    # fungsi myInArray(arr, el, size) mengembalikan predikat dari pernyataan "elemen el ada dalam array arr"
    # sebagai variabel boolean

    for i in range(size) :
        if arr[i] == el :
            return True
    return False

def myIndex(arr, el, size) :
    # fungsi myIndex(arr, el, size) mengembalikan indeks paling rendah dari elemen el pada array arr
    # atau mengembalikan -1 jika elemen tidak ditemukan

    for i in range(size) :
        if arr[i] == el :
            return i
    return -1

def slicing(arr, id1, id2) :
    # fungsi slicing(arr, id1, id2) mengembalikan array baru berisi elemen pada arr dari indeks id1 hingga id2-1

    res = [0 for i in range(id2 - id1)]
    for i in range(id2 - id1) :
        res[i] = arr[id1 + i]
    return res

if __name__ == "__main__" :
    # Kode untuk keperluan testing
    arr1 = [5,2,3,4,5]
    arr2 = [4,-1,-2,-3]
    print(myAppend(arr1, arr2[3], 5))
    print(arrayPlus(arr1, 5, arr2, 4))
    print(myInArray(arr2, -2, 4))
    print(myInArray(arr1, 6, 5))
    print(myIndex(arr1, 3, 5))