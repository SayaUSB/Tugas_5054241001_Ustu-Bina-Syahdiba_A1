perulangan = int(input("Masukkan jumlah perulangan : ")) # Memasukkan banyaknya perulangan perintah
for _ in range(perulangan):
    tipe, geser = map(int, input("Masukkan perintah : ").split()) # Memasukkan tipe perintah
    kalimat = list(input("Masukkan kalimat : "))
    if tipe==1:
        for i in range(0, len(kalimat)):
            if kalimat[i]==" ":
                continue
            kalimat[i] = chr(ord(kalimat[i])+geser) # Menggeser ASCII dengan pertambahan
    elif tipe==2:
        for i in range(0, len(kalimat)):
            if kalimat[i]==" ":
                continue
            kalimat[i] = chr(ord(kalimat[i])-geser) # Menggeser ASCII dengan pengurangan
    for i in kalimat:
        print(i, end="")
    print()