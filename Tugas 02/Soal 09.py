def hitung_tagihan(menit_weekday, menit_malam, menit_weekend):
    # Menghitung biaya pada waktu biasa
    if menit_weekday <= 600:
        weekday_charge = 3999
    else:
        weekday_charge = 3999 + (menit_weekday - 600) * 40

    # Menghitung tagihan sebelum pajak
    sebelum_pajak = weekday_charge

    # Menghitung pajak
    pajak = round(sebelum_pajak * 0.0525)

    # Menghitung total biaya
    total_tagihan = sebelum_pajak + pajak

    # Menghitung rerata biaya per menit
    rerata_biaya_menit = round(total_tagihan / (menit_weekday + menit_malam + menit_weekend))

    return sebelum_pajak, pajak, total_tagihan, rerata_biaya_menit

# Input menit pada weekday, malam hari, dan weekend
menit_weekday = int(input("Lama penggunaan dalam hari biasa\t: "))
menit_malam = int(input("Lama penggunaan dalam malam hari\t: "))
menit_weekend = int(input("Lama penggunaan dalam akhir pekan\t: "))

# Memanggil fungsi untuk mengkalkulasi tagihan
sebelum_pajak, pajak, total_tagihan, rerata_biaya_menit = hitung_tagihan(menit_weekday, menit_malam, menit_weekend)

# Output hasil
print("\nData Penggunaan:")
print("\tWaktu normal (menit)\t\t:", menit_weekday)
print("\tWaktu malam (menit)\t\t:", menit_malam)
print("\tWaktu akhir pekan (menit)\t:", menit_weekend)
print("\nData Penggunaan:")
print("\tTagihan sebelum pajak\t\t: $", sebelum_pajak / 100)
print("\tPajak\t\t\t\t: $", pajak / 100)
print("\tTotal tagihan\t\t\t: $", total_tagihan / 100)
print("\tBiaya per menit\t\t\t: $", rerata_biaya_menit / 100)