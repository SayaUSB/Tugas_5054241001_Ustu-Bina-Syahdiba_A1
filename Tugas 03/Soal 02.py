perulangan = int(input("Masukkan jumlah perulangan : ")) # Masukan untuk berapa angka yang dikode
kalimat = [] # Array untuk output
for _ in range(0, perulangan):
    angka = int(input("Masukkan angka yang dikode : "))
    angka = str(format(angka, "x")) # Mengubah angka langsung menjadi hexadecimal
    temp = [] # Array temporary
    for i in range(1, len(angka)+1, 2):
        temp.append(int(angka[i-1:i+1], 16))
    for i in range(0, len(temp)):
        kalimat.append(chr(temp[i])) # Memasukkan seluruh elemen temporary array ke dalam output array
for _ in kalimat:
    print(_, end="")

