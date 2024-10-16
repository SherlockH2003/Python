# Ini file belajar tentang
# "Lists dan Tuples"

# Lists adalah struktur data sementara yang bisa diubah-ubah elemennya.
# Tuples adalah struktur data sementara yang tidak bisa diubah elemennya

# Lists digunakan ketika kita membutuhkan data yang fleksibel
# Tuples digunakan ketika kita membutuhkan data yang bernilai tetap

# =======================================================

# Operasi Lists

# 1. .append(element) : untuk menambahkan elemen dari urutan belakang
buah = ["mangga", "alpukat", "semangka", "melon", "nanas"]
buah.append("pisang");
print(buah);

# 2. .insert(element) : untuk menambahkan elemen dari urutan pertama/tertentu
# .insert() tidak menghapus nilai pada indeks yang dipanggil, namun menggesernya ke indeks selanjutnya
buah.insert(0,"kelapa");
print(buah);

# 3. .remove(element) : untuk menghapus elemen dari index tertentu berdasarkan nama element
#    .pop(index)      : untuk menghapus elemen dari index tertentu berdasarkan nomor index
buah.pop(3);
print(buah);
buah.remove("melon");
print(buah);

# 4. .sort() : untuk menyortir list
# 5. .reverse() : untuk membalik elemen list berdasarkan indexnya
# 6. .clear() : untuk menghapus semua elemen
# 7. .copy() : untuk membuat copy list
# 8. .extend(list) : untuk meng-append list dengan list lainnya

# Iterasi Lists
# menghitung jumlah karakter dalam lists
nama = ["farhan", "fadia", "fahry", "fitri", "farrel"];
print(len(nama)); # ini hanya akan mengembalikan jumlah elemen
karakter = 0;
for names in nama:
    karakter += len(names); 
print("total karakter : {}, rata-rata huruf : {avg}".format(karakter, avg=karakter/len(nama)));

# input sebagai parameter
def gmailKampus(orang):
    nama, npm = orang;
    result = [];
    for nama, npm in orang:
        result.append("{} <email kampus: {}@student.unsika.ac.id>".format(nama, npm));
    return result
    

print(gmailKampus([("Farhan Abyan", "2210631250049"), ("Fadia Lutfiyah", "2210631250047")]))

# methods "enumerate"
# methods enumerate mengambil lists sebagai parameter
# dan mengembalikan tuples yang berisi indeks dan nilai dalam sebuah nilai
for indeks, nilai in enumerate(nama):
    print(f"[{indeks} - {nilai}]", end=" ");
print();

# singkatan lists / lists comprehensions
# -> untuk membuat lists berdasarkan sequences atau range

print([perkalian7*7 for perkalian7 in range (1,11)]); # list berisi perkalian angka 7 dari 7x1 s.d. 7x10
print([names for names in nama if "ar" in names]) # memanggil lists nama berdasarkan kondisi jika ada "ar" di dalamnya

# =======================================================

# Tuples

tupleExample = (1,2, [2,4,5]);
# angka1,angka2 = tupleExample # tidak bisa assign ke variabel jika kurang dari len(tuple)
# print(angka1, angka); # akan muncul ValueError: too many values to unpack
# tupleExample(1); # akan muncul TypeError : 'tuple' object is not callable
# tupleExample(0) = "ganti"; # akan muncul SyntaxError : cannot assign to function

# Kita bisa memodifikasi objek mutable dalam tuple
tupleExample[2][0] = 3
print(tupleExample)  # Outputs: (1,2, [3,4,5]);

# tuples menjadi basic ketika sebuah fungsi mengembalikan
# nilai dengan variabel yang banyak.

def pangkat(angka):
    return angka**2, angka**3, angka**4;

hasil = pangkat(5);
print(hasil);
print(type(hasil));

# tuples juga bisa displit menjadi variabel terpisah
# kegiatan ini disebut "Unpacking"
kuadrat, kubik, kuartik = hasil;
print(kuadrat, kubik, kuartik);
