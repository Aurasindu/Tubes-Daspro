# fungsi save data dari sebuah file
def SaveData(file, data):
    data = convert_datas_to_string(data)
    f = open(file, "w") 
    f.write(data)
    f.close()

# fungsi ubah data menjadi string
def convert_datas_to_string(data):
    data_string = ""
    for arr_data in data:
        arr_data_all_string = [str(var) for var in arr_data]
        data_string += ";".join(arr_data_all_string)
        data_string += "\n"
    return data_string
