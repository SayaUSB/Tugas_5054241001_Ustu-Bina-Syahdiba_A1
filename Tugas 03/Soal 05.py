item = {} # Deklarasi dictionary
berubah = []
banyak_stok = int(input("Masukkan nama dan jumlah item : "))
for i in range(0, banyak_stok):
    temp = list(input().split())
    temp[1] = int(temp[1])
    item[temp[0]] = temp[1]
banyak_ambil = int(input("Masukkan nama dan jumlah item yang diambil : "))
for i in range(0, banyak_ambil):
    temp = list(input().split())
    temp[1] = int(temp[1])
    berubah.append(temp[0]) # Mendeteksi item apa yang telah diubah
    item[temp[0]] -= temp[1]
print("\nCHARLIE")
for i in berubah: # Output item apa saja yang telah berubah stoknya
    print(i, end=" ")
print("\nSTORAGE")
for i in item: # Output item apa saja yang telah berubah stoknya dan jumlah stoknya
    print(i, item[i])