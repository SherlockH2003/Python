# Ini file belajar tentang
# "string operations"

# string operations adalah syntax yang digunakan untuk
# memanipulasi data dalam string

# =======================================================

# len(string) : untuk mengembalikan nilai "panjang" string
print(len("kalimat 19 karakter"));

# =======================================================

# for {character} in {string} : untuk mengembalikan tiap karakter dalam string 
# atau mengiterasi karakter dalam string menggunakan for loop
for kata in "Farhan":
    print(kata);
    
# bisa juga dibuat seperti ini :
for c in "ABCDE": print(c);

# =======================================================

# {substring} in {string} : untuk mengembalikan nilai boolean saat memeriksa
#                           apakah substring yang dipanggil ada di dalam 
#                           string yang dimaksud
print("ayam" in "Sukabumi bakar ayam");

# =======================================================

# {string}[indeks] : untuk mengembalikan substring berdasarkan indeks yang dimaksud
print("huruf x ada di indeks ke-6"[6]);
print("huruf e ada di indeks ke-(-4)"[-6]); # klo indeks diisi bilangan negatif, akan mulai dari belakang