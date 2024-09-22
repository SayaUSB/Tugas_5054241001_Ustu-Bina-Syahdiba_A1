def aku(tinggi): # Fungsi untuk input 'Aku'
    for i in range(tinggi):
        if i%2==0:
            flag = 0
        else:
            flag = 1
        for j in range(i+1):
            if flag%2==0:
                print("I",end="")
            else:
                print("U",end="")
            flag += 1
        print()

def kamu(tinggi): # Fungsi untuk input 'Kamu'
    spasi = tinggi
    for i in range(tinggi):
        spasi -= 1
        flag = 0
        print(" "*spasi, end="")
        for j in range(i+1):
            if flag%2==0:
                print("I",end="")
            else:
                print("U",end="")
            flag += 1
        print()

tinggi, tipe = input().split() # Input tinggi dan tipe perintah
tinggi = int(tinggi)
# Deteksi perintah
if tipe=="Aku":
    aku(tinggi)
elif tipe=="Kamu":
    kamu(tinggi)