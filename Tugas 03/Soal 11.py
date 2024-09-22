kalimat = input("Masukkan kalimat : ") # Input kalimat
kalimat = kalimat.replace(" ", "") # Menghapus spasi
kalimat = ''.join(dict.fromkeys(kalimat)) #Menghapus karakter yang sama
print(kalimat) # Print kalimat