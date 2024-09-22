kalimat = input("Masukkan kalimat : ") # Input kalimat
panjang = int(input("Masukkan panjang kalimat : ")) # Input panjang kalimat yang didecrypt
masuk = list(map(int, input().split())) # Ambil karakter
for i in range(len(masuk)):
    print(kalimat[masuk[i]],end="") # Output decrypted kalimat
