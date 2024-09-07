# Input jenis pelanggan, diskon, pajak, dan total pembelian
jenis_pelanggan = input("Jenis pelanggan : ")
total_beli = float(input("Total pembelian : "))
diskon = float(input("Masukkan diskon (%) : "))/100
pajak = float(input("Masukkan pajak (%) : "))/100

# Cek apakah mahasigma atau bukan
if jenis_pelanggan == "Mahasigma":
    total_beli -= diskon*total_beli
total_beli += pajak*total_beli

# Output total pembelian
print(f"Total pembelian adalah ${total_beli}")

