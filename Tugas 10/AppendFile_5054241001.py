from datetime import datetime

file = open("myfile.txt", "a")
print("Transaksi yang terjadi:")
nama, harga = map(str, input().split())
harga = int(harga)
file.write(f"{datetime.now()}: {nama} dengan harga {harga}\n")
file.close()
