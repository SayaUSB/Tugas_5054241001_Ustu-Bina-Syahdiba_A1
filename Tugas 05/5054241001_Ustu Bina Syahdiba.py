# Create String
nama = "Ustu Bina Syahdiba"
nrp = "5054241001"
asal = "Surabaya"

# Print String Data
print("Nama Saya \t: " + nama)
print("NRP Saya \t: " + nrp)
print("Asal Saya \t: " + asal)

# Access Character In String
print("Inisial Saya \t: " + nama[0] + nama[5] + nama[10])

# String Slicing
print("Nama Belakang \t: " + nama[10:])
print("Nama Awal \t: " + nama[:5])

# Reverse String
print("Reverse NRP \t: " + nrp[::-1])

# Update String
rka = "Saya Mahasiswa RKA"
print(rka)
#ubah Menjadi "Saya bukan mahasiswa RPL"
rka = list(rka)
rka[4] = ' bukan '
bukan = ''.join(rka)

rpl = bukan[0:21] + "RPL"
print(rpl)

# Tugas Implementasi

# 1. Deleting a character
nama = nama.replace("Ustu ","")
nama = nama.replace("Syahdiba","")
print("Nama panggilan saya adalah", nama)

# 2. Escape Sequencing in python + Example
cerdas = "C:\\Windows\\System32\\"
print("Tolong hapus ini karena directory ini sangat tidak berguna", cerdas)
print("Biasanya ini tidak bisa diprint biasa (\\)")
print("Rekayasa \'Kecerdasan\' Artifisial")
print("Rekayasa \"Kecerdasan\" Artifisial")
print("Biasanya ini tidak bisa diprint biasa (\\n)")
print("Biasanya ini tidak bisa diprint biasa (\\t)")
print("Biasanya ini tidak bisa diprint biasa (\\r)")
print("Biasanya ini tidak bisa diprint biasa (\\b)")
print("Biasanya ini tidak bisa diprint biasa (\\f)")
print("Biasanya ini tidak bisa diprint biasa (\\v)")
print("Biasanya ini tidak bisa diprint biasa (\\0)")
print(r"Bisa juga dengan cara ini (\)")
print(r"Bisa juga dengan cara ini (\n)")
print(r"Bisa juga dengan cara ini (\t)")
print(r"Bisa juga dengan cara ini (\r)")
print(r"Bisa juga dengan cara ini (\b)")
print(r"Bisa juga dengan cara ini (\f)")
print(r"Bisa juga dengan cara ini (\v)")
print(r"Bisa juga dengan cara ini (\0)")

# 3. Python String Formating + Example
ipk = 2.3
makanan = "nasi"
dobleh = "ayam"
huruf = "Bina"
angka = 1342.213
print("Aku fufufafa dan ip ku %.2f"%(ipk))
print("Saya aslinya %.0f orang"%(ipk))
print(f"Aku fufufafa dan ip ku {ipk:.2f}") # fungsi dari :.2f adalah membulatkan angka menjadi dua angka di belakang koma
print(f"Saya aslinya {ipk:.0f} orang")
print("{0:e}".format(angka)) # output format dengan bilangan exponential
print("Saya aslinya {:.0f} orang".format(ipk)) # fungsi dari :.0f adalah membulatkan angka dan menghilangkan angka di belakang koma
print("Saya suka makan {} bersama {}".format(makanan, dobleh)) # mengambil data sesuai dengan urutan yang ada di dalam format
print("Inisial ku adalah {1} dan aku suka makan {0}".format(makanan, huruf)) # {1} mengakses data kedua atau index pertama, sedangkan {0} mengakses data pertama atau index ke0