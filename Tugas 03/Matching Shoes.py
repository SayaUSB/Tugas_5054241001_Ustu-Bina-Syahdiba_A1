banyak = int(input("Masukkan jumlah sepatu : ")) # Input banyak perulangan
sepatu = [] # List untuk menyimpan sepatu
for _ in range(banyak):
    masuk = input() # Input kata acak
    temp = "" # String sementara sebelum masuk ke list utama
    for i in range(len(masuk)):
        if masuk[i].isdigit(): # Cek apakah karakter adalah angka
            temp += masuk[i]
        elif masuk[i]=="L" or masuk[i]=="R": # Cek apakah karakter adalah L atau R
            temp += masuk[i]
    sepatu.append(temp) # Memasukkan string sementara ke list utama
sama = 0 # Variabel untuk menyimpan hasil deteksi ukuran yang sama  
i = 0
while i<len(sepatu)-1: # Looping untuk cek pasang sepatu
    j = i+1
    while j<len(sepatu):
        if sepatu[i][:-1]==sepatu[j][:-1]:
            if sepatu[i][-1]=="L" and sepatu[j][-1]=="R":
                sama += 1
            elif sepatu[i][-1]=="R" and sepatu[j][-1]=="L":
                sama += 1
        j += 1
    i += 1
print(f"Pasang sepatu yang dihasilkan : {sama}")
