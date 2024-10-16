# Ini file belajar tentang
# "string formatting"

# string formatting adalah syntax yang digunakan untuk memformat
# data string agar memenuhi kebutuhan developer

# =======================================================

# {"string var1 = {} , var2 = {}"}.format(var1, var2,...)
#    -> berfungsi menambahkan variable ditengah kalimat menggunakan
#       kurung kurawal "{}", dan suffix '.format(var1,var2,...)' di
#       akhir string

def angkaHoki(nama):
    return "Selamat {}, angka keberuntunganmu hari ini adalah {}".format(nama, len(nama)*777);
print(angkaHoki("Farhan Abyan"))

# isi kurung kurawal di dalam string juga bisa ditambahkan dengan nama variabel.
# biasanya untuk mencegah variable tertukar
nama = "Farhan Abyan PK"
angka = len(nama)*77777
print("Selamat {name}, angka keberuntunganmu adalah {number}".format(name=nama, number=angka))

# isi kurung kurawal di dalam string juga bisa ditambahkan dengan limiter desimal.
# formatting expression ini biasanya untuk membatasi angka dibelakang koma yang kepanjangan

def hitungPPN(harga):
    return harga*112/100.00;
print("Harga setelah PPN : Rp{:.2f}".format(hitungPPN(16999)));

# isi kurung kurawal di dalam string juga bisa ditambahkan dengan indentator.
# formatting expression ini biasanya untuk merapihkan alignment teks
# {:d}               : untuk nilai integer
# {:.{desimal}f}     : untuk nilai float beserta desimal
# {:.{separator}s}   : untuk nilai string yang dipisah sejumlah separator
# {:>{jumlah spasi}} : untuk alignment ke kanan
# {:<{jumlah spasi}} : untuk alignment ke kiri
# {:^{jumlah spasi}} : untuk alignment ke tengah
# {(number),}        : untuk pemisah ribuan uang    

def hitungPPN(harga):
    return harga*112.00/100.00;
namaBarang = ("ayam" ,"ikan","sayur")
hargaBarang = [32499,24999,10999]
print("harga terkini (sudah termasuk PPN):")
for nama in namaBarang:
    index = namaBarang.index(nama)
    print("|{:<6}= Rp{:>10,.2f} |".format(nama,hitungPPN(hargaBarang[index])))

# =======================================================

# f-string / formatted string

# -> hampir mirip sama .format(), cuman f-string ngambil variabel
#    secara mentah / literal alih-alih make parameter.
# contoh :
nama = "Farhan"
umur = "20"
print(f"selamat ulang tahun yang ke-{umur}, {nama} !!")

# =======================================================

# old string formatting

# -> intinya jaman dulu tuh bisa make metode format string
#    kayak punya bahasa C, atau C++. Pake "%s, %3d, %.2f"   
# contoh :
nama = "Farhan"
umur = 20
print("selamat ulang tahun yang ke-%d , %s !!" % (umur+1, nama));
print("selamat ulang tahun yang ke-%(var1)d, %(var2)s !!" % {"var1":umur+2, "var2":nama});

# =======================================================

# catatan dari coursera : FORMAT LISTS

# Here are the items in the customer's basket. Each item is a tuple
# of (item name, weight, price per pound).
basket = [
    ("Peaches", 3.0, 2.99),
    ("Pears", 5.0, 1.66),
    ("Plums", 2.5, 3.99)
    ]


# Calculate the total price for each item (weight times price per pound)
# and add them up to get a subtotal.
print("---------------------------------------")
subtotal = 0.00
total = 0.00
for item in basket:
    fruit, weight, unit_price = item
    subtotal += (weight * unit_price)
    total += subtotal
    print("name   : {:<7} \nweight : {:<4} \nprice  : ${:<5.2f}".format(fruit, weight,subtotal))
    print("---------------------------------------")
print("Total  : ${:>5.2f}".format(total))


# variable also could be passed by index number in format
fruit = "peaches"
weight = 3.0
per_pound = 2.99

output = "{1} are {2} per pound, and you have {0} pounds of {1}.".format(weight, fruit, per_pound)
# ^ in above example
# weight    = {0}
# fruit     = {1}
# per_pound = {2}

print(output);