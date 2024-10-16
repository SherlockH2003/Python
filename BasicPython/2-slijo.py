# Ini file belajar tentang
# "slicing" dan "joining" string

# =======================================================

# slicing adalah teknik memotong sebuah kalimat berdasarkan
# range / rentang karakter tertentu. Sintaksnya hampir sama dengan range.

# contoh slicing :
nama = "Farhan Abyan Putra Karim" ; # panjangnya adalah 24 karakter (0 s.d. 23)
print(nama[:10]); # memberikan output dari indeks 0 s.d. indeks 9
print(nama[-5:]); # memberikan output 5 indeks dari belakang (indeks 19 s.d. 23)
print(nama[20:21]); # memberikan output dari indeks 20 saja
print(nama[3:]); # memberikan output dari indeks 3 s.d. seterusnya
print(nama[0:24]); # memberikan output dari indeks 0 s.d. indeks 23
print(nama[55:]); # memberikan output kosong : ""

print(nama[::3]); 
# memunculkan karakter indeks ke-0 dengan pola hitung 3 indeks (0 - 2)

# teks   : F - a - r - h - a - n -   - A
# indeks : 0 - 1 - 2 - 0 - 1 - 2 - 0 - 1
# status : m - h - h - m - h - h - m - h
# hasil  : "Fh "

# m : muncul | h : hilang

print(nama[2::5]); 
# memunculkan karakter indeks ke-2 dengan pola hitung 5 indeks (0 - 4)

# teks   : F - a - r - h - a - n -   - A - b - y - a - n -  
# indeks : 0 - 1 - 2 - 3 - 4 - 0 - 1 - 2 - 3 - 4 - 0 - 1 - 2
# status : h - h - m - h - h - h - h - m - h - h - h - h - m
# hasil  : "rA "

# m : muncul | h : hilang

print(nama[1::6]); 
# memunculkan karakter indeks ke-4 dengan pola hitung 6 indeks (0 - 5)

# teks   : F - a - r - h - a - n -   - A - b - y - a - n -  
# indeks : 0 - 1 - 2 - 3 - 4 - 5 - 0 - 1 - 2 - 3 - 4 - 5 - 0
# status : h - m - h - h - h - h - h - m - h - h - h - h - h
# hasil  : "aA"

# m : muncul | h : hilang

print(nama[::-3]); 
# memunculkan karakter indeks ke-0 dari belakang dengan pola hitung 3 indeks (0 - 2)

# teks   : m - i - r - a - K -   - a - r - t - u - P -   - n 
# indeks : 0 - 1 - 2 - 0 - 1 - 2 - 0 - 1 - 2 - 0 - 1 - 2 - 0
# status : m - h - h - m - h - h - m - h - h - m - h - h - m
# hasil  : "maaun"

print(nama[-2::-5]); 
# memunculkan karakter indeks ke-2 dari belakang dengan pola hitung 4 indeks (0 - 4) yang dibalik

# teks            : Farhan Abyan Putra Karim
# indeks          : 012340123401234012340123

# teks terbalik   : miraK artuP naybA nahraF
# indeks terbalik : 321043210432104321043210
# status          : hmhhhhmhhhhmhhhhmhhhhmhh

# hasil           : "ia Ar"

# m : muncul | h : hilang

print(nama[2::-5]); # hanya memunculkan indeks ke 2 dari belakang (tidak meneruskan pola hitung)
print(nama[-4::6]); # hanya memunculkan indeks ke 4 dari belakang (tidak meneruskan pola hitung)
# ^
# perhitungan dari belakang mewajibkan kita untuk menyatakan kedua parameter itu negatif
# ga cuman parameter kiri saja "[-kiri::kanan]" atau kanan saja "[kiri::-kanan]"

# =======================================================

# joining / string join / string concatenaete adalah teknik menggabungkan string
# biasalah, gabunginnya make tanda "+"

# contoh string concat :
nama = ["farhan", "abyan", "putra"]

for name in nama:
    print("[email-" + name + ": " + name + "@gmail.com]", end=" ");

# argumen "end=" dalam print() akan menentukan separator/pemisah
# antara satu output dengan output lainnya

# =======================================================

# Slicing & Joining bisa digabungkan menjadi 1 dalam sebuah output !!