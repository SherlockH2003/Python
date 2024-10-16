# Ini file belajar tentang
# "string methods"

# string methods adalah method yang digunakan untuk memformat
# data string agar memenuhi kebutuhan developer

# =======================================================

# 1. {string}.upper() dan {string}.lower()
#    -> berfungsi sebagai pengubah string menjadi uppercase atau lowercase

upperText = "HURUF KAPITAL";
lowerText = "huruf kecil"
print(upperText.upper());
print(lowerText.lower());

# =======================================================

# 2. {string}.strip(), {string}.rstrip(), {string}.lstrip()
#    -> berfungsi menghapus spasi berlebih di kanan dan/atau kiri string
#       tidak akan menghapus spasi di tengah string

stripText1 = "      kalimat Pertama      "
stripText2 = "      kalimat        Kedua       "
stripText3 = "      kalimat ketiga"
stripText4 = "kalimat keempat      "

print(stripText1.strip());
print(stripText2.strip());
print(stripText3.strip());
print(stripText4.strip());

# =======================================================

# 3. {string}.count("{substring}")

#    -> berfungsi menghitung substring dalam string

countText1 = "kalimat yang dihitung"
countText2 = "kalimat yang akan akan dihitung"

print(countText1.count("a"));
print(countText2.count("akan"));

# =======================================================

# 4. {string}.endswith("{substring}")

#    -> berfungsi me-return boolean True/False jika suffix
#       atau akhiran string mengikuti substring yang dimaksud

endswithText = "kalimat berakhiran nasi - Transluminasi"
print(endswithText.endswith("nasi"));
print(endswithText.endswith("goreng"));

# =======================================================

# 5. {string}.isnumeric() dan {string}.isalpha()

#    -> isnumeric berfungsi me-return boolean True/False jika string
#       terdiri dari hanya angka atau tidak

#    -> isalpha berfungsi me-return boolean True/False jika string
#       terdiri dari hanya alphabet atau tidak

# contoh isnumeric :
isnumericText1 = "123456"
isnumericText2 = "1a2b3c"
print(isnumericText1.isnumeric());
print(isnumericText2.isnumeric());

# string juga bisa diubah menjadi int atau float dengan
# "Explicit Conversion"

toNumber = int(isnumericText1);
print(toNumber + 111111); # 123456 + 111111 = 234567

# contoh isalpha :
isalphaText1 = "ABCDEF"
isalphaText2 = "1a2b3c"
print(isalphaText1.isalpha());
print(isalphaText2.isalpha());

# =======================================================

# 6. {delimiter}.join([stringList])

#   -> berfungsi untuk meng-concat/menggabungkan banyak
#      string dalam list dan memisahkan antar kata/kalimat
#      menggunakan delimiter yang diinginkan
# 
#      p.s. : jenis bracket mengikuti tipe data iterable yang dipakai
#             tuple      : var = (text1, text2, ...)
#             dictionary : var = {text1 : textA, text2 : textB, ...}

joinTextList = ("Ini", "adalah", "contoh", "teks", "yang", "akan", "digabungkan");
print(" ".join(joinTextList));

# =======================================================

# 7. {string}.split({delimiter}, {maxSplit})
#   delimiter / separator : pemisah (Default " " untuk 'Spasi')
#   maxSplit              : jumlah pemisahan (Default "-1" untuk 'Sampai Akhir')

#   -> berfungsi untuk memisahkan kata/kalimat dengan delimiter yang digunakan
splitTextList = ("Ini adalah contoh teks yang akan dipisahkan");
print(splitTextList.split(" ", 5));

# =======================================================

# 8. {string}.replace(lama, baru)
#   lama : kata/kalimat lama yang akan diganti
#   baru : kata/kalimat baru yang akan menggantikan

#   -> berfungsi untuk menggantikan dua buah kata/kalimat
replaceTextList = ("Ini adalah contoh teks yang akan digantukan");
print(replaceTextList.replace("digantukan", "digantikan"));

# =======================================================

# 9. {string}.index(substring)

#   -> berfungsi untuk menggantikan dua buah kata/kalimat
indexTextList = ("Ini adalah contoh teks yang akan dicari adalah index");
print(indexTextList.index("adalah",1,-1));



