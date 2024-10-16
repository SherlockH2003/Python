# Ini file belajar tentang
# "Dictionary"

# Dictionary adalah struktur data yang terdiri dari "key : value"

# Key dictionary tidak dapat diubah, tapi value bisa diubah/duplikasi
# struktur dictionary tidak sequensial/terurut, dan random

# =======================================================

# dict dideklarasi hampir sama dengan list hanya saja menggunakan kurung kurawal.

dictionary = {};
print(type(dictionary));

dictionary = {
    "ayam" : "30000",
    "sapi" : "70000",
    "kambing" : "60000"
}

# memanggil key dan value dalam dictionary harus menggunakan looping

for key, value in dictionary.items():
    print(f"key = {key} : value = {value}");

# =====================================================

# dict operations

# len(dictionary)                      : banyak item (gabungan 'key : values')
# for key in dictionary                : iterasi kunci aja
# for key, value in dictionary.items() : iterasi kunci dan value pake method ".items()"
# dictionary[key]                      : akses value pake kata kunci "key"
# dictionary[key] = newValue           : assign value baru ke dalam dict menurut kata kuncinya
# del dictionary[key]                  : menghapus sebuah kunci dalam dict

# dict methods

# dictionary.get(key, default)         : mengembalikan nilai sesuai kata kunci
print(dictionary.get("ayam"))
# dictionary.keys()                    : mengembalikan kunci saja
print(dictionary.keys());
# dictionary.values()                  : mengembalikan value saja
print(dictionary.values());

# dictionary[key].append(value)        : menambah nilai lists baru untuk kunci yang ada

dictionary1 = {
    "buah" : ["apel", "pisang", "jeruk", "kelapa"],
    "sayur": ["sawi", "kangkung", "kol", "terung"],
    "karbo": ["nasi", "roti", "kentang", "singkong"]
}
dictionary1["sayur"].append("ketimun");
for key, value in dictionary1.items():
    print(f"key = {key} : value = {value}");

# dictionary.update(other_dictionary)  : menggabungkan satu dict dengan dict lainnya
dictionary2 = dictionary1
dictionary2.update(dictionary)
for key, value in dictionary2.items():
    print(f"dict2 | key = {key} : value = {value}");

# dictionary.clear()                   : menghapus semua item
dictionary2.clear()
for key, value in dictionary2.items():
    print(f"key = {key} : value = {value}");

# dictionary.copy                      : menyalin dictionary
dictionary3 = dictionary.copy();
for key, value in dictionary3.items():
    print(f"dict3 | key = {key} : value = {value}");