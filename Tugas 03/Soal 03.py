batu = list(input()) # Input batu
rugi = 0 # Variabel penyimpan kerugian
i = 0 # Iterator
while i<len(batu)-1:
    if batu[i]==batu[i+1]:
        rugi += int(ord(batu[i])*1e3)
        batu.pop(i) # Menghapus jenis batu bersebelahan yang sama
    else:
        i += 1
print(f"Di gudang tersisa {len(batu)} batu")
if rugi==0: # Ketika rugi = 0 berarti tidak ada perubahan
    print("Wah, Jotaro Joemama tidak jadi dipecat")
else: # Mengalami kerugian
    print(f"Total Kerugian: {rugi} Dolar Imbu")
