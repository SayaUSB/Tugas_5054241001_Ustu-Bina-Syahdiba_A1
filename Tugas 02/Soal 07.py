# Input tanggal
tanggal = list(map(int, input("Masukkan tanggal (Bulan:Hari:Tahun): ").split(":")))
bulan = [31,28,31,30,31,30,31,31,30,31,30,31]

# Cek tahun kabisat
if tanggal[2]%400==0:
    kabisat = True
elif tanggal[2]%100==0:
    kabisat = False
elif tanggal[2]%4==0:
    kabisat = True
else:
    kabisat = False

# Menambah sehari jika tahun kabisat
if kabisat:
    bulan[1]+=1

# Menghitung jumlah hari yang telah terlewat
if tanggal[0]==1:
    jumlah_hari = tanggal[0]
    print(f"Hari yang terlewatkan dalam tahun {jumlah_hari}")
else:
    jumlah_hari = sum(bulan[:tanggal[0]-1])
    jumlah_hari += tanggal[1]

# Output jumlah hari yang telah terlewat
print(jumlah_hari)


