# Konstanta suhu maksimal benda
benda = {100: "water", 357:"mercury", 1187:"copper", 2193:"silver", 2660:"gold"}

# Input suhu
suhu = int(input("Masukkan suhu benda : "))

# Variabel untuk mengetahui bahwa benda dapat diindetifikasi
flag = 0

# Kategorisasi benda
for i in benda:
    if suhu<=i+i*0.05 and suhu>=i-i*0.05:
        print(f"Benda ini adalah {benda[i]}")
        flag += 1
        break
if not flag:
    print("Benda ini tidak diketahui")