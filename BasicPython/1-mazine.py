# Ini file belajar tentang
# map(), zip(), dan next()

# ====================================================================================================

# map() adalah metode/fungsi yang mengembalikan hasil iterasi
# setelah menerapkan fungsi lain terhadap sebuah iterable.
# iterable adalah sebuah data yang bisa diiterasi.
# contoh iterable : lists, dict, tuple, sets

# sintaks map : map(func, iter)
# func = fungsi yang digunakan
# iter = iterable yang akan diterapkan ke func

# contoh penggunaan map() :
nomor = [2,3,4,5]; # ini iterablenya yang akan diterapkan

def kuadrat(x) : # ini fungsi yang akan digunakan
    hasil = x*x;
    return hasil;

hasilKuadrat = map(kuadrat, nomor); # penggunaan map
print(hasilKuadrat); # output map menggunakan variable saja cuman menghasilkan status

print(next(hasilKuadrat)); 
# ^
# output map menggunakan next akan mengeluarkan hasil map() satu per satu.
# perintah next() sepertinya harus ditaruh sebelum list
# karena kalo sudah ada list, jadinya error
# mungkin karena 'hasilKuadrat' yang udah di list ga bisa dilanjutkan

print(list(hasilKuadrat)); 
# ^
# output map menggunakan list akan mengeluarkan hasil map() ke dalam array.
# perintah list yang sebelumnya ada "next()" akan melanjutkan iterasi setelah next()
# jadi gak ngulang lagi dari indeks 0 pada variable "nomor". Dalam hal ini, karena
# "next()" dipanggil 1 kali, maka list akan lanjut ke indeks 1. indeks 0 dianggap selesai

# ====================================================================================================

# zip() adalah metode yang mampu menggabungkan dua buah iterable
# berdasarkan indeks-indeksnya.

# sintaks zip() : zip(iter1,iter2,...)
# iter1 = iterable urutan pertama yang akan diterapkan ke func
# iter2 = iterable urutan kedua yang akan diterapkan ke func

# contoh penggunaan zip() :
nama = ["ali", "aldi", "ari", "adi"]; # iterable 1
kelas = ["5A", "5B", "5C", "5D"]; # iterable 2
indeks = ["0", "1", "2", "3"]; # iterable 3

hasil = zip(nama,kelas,indeks); # penggunaan zip

print(hasil) # output zip menggunakan variable saja cuman menghasilkan status
print(next(hasil)) 
# ^
# output zip menggunakan list akan mengeluarkan hasil zip() ke dalam array
# perintah next() sepertinya harus ditaruh sebelum list
# karena kalo sudah ada list, jadinya error
# mungkin karena 'hasilKuadrat' yang udah di list ga bisa dilanjutkan

print(list(hasil)) 
# ^
# output zip menggunakan list akan mengeluarkan hasil zip() ke dalam array
# perintah list yang sebelumnya ada "next()" akan melanjutkan iterasi setelah next()
# jadi gak ngulang lagi dari indeks 0 pada variable "nomor". Dalam hal ini, karena
# "next()" dipanggil 1 kali, maka list akan lanjut ke indeks 1. indeks 0 dianggap selesai

# ====================================================================================================
