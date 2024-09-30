U5 = 11
jumlah_U8_U12 = 52
n = 8
# Menghitung beda (b)
b = (jumlah_U8_U12 / 2 - U5) / (18 / 2 - 4)
print(b) 

# Menghitung suku pertama (a)
a = U5 - 4 * b
print (a)
# Menghitung jumlah 8 suku pertama
jumlah_8_suku = (8 / 2) * (2 * a + 7 * b)
print("Jumlah 8 suku pertama:",jumlah_8_suku)