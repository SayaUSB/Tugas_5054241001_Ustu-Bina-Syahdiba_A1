# kolom1 = baris pertama selalu 1        |  spasi = (kolom3+2-baris1+2)//2
# kolom2 = selalu + 2 dari sebelumnya    | spasi2 = (kolom2+2-baris2+2)//2
# kolom3 = total col - (2 * (num - 8))
import math

n = int(input())

baris=(n-8)*3
kolom=(n-8)*6

baris1 = 3
baris2 = math.ceil((n - 3) / 2)
baris3 = (n - 3) // 2

kolom1 = 1
kolom2 = ((n-8)*2)-1
kolom3 = kolom - 2*(n-8)

spasi1 = int((kolom3+2-kolom1-2)//2)
spasi2 = int((kolom3+2-kolom2-2)//2)

spasi0 = spasi1+1

if n < 8:
    print("Too Small")
else:
    # Bintang paling atas
    print(" " * spasi0  + "*")
    
    # Roti lapisan pertama (Atas)
    print((" " * spasi1 + "|-|"  + "\n") * baris1,end="")
    
    # Pemisah roti lapisan pertama dan dua(tengah)
    print(" " * spasi2 + "-" * (kolom2+2) + "\n", end="")
    
    # Roti lapisan kedua (tengah)
    print((" " * spasi2 + "|" + "=" * kolom2 + "|" + "\n") * baris2,end="")
    
    # Pemisah roti lapisan kedua dan ketiga(bawah)
    print("-" * (kolom3+2) )
    
    # Roti lapisan ketiga (bawah)
    print(("|" + "="*kolom3 + "|" + "\n")*baris3,end ="")

    # Pemisah roti lapisan ketiga dan bawah
    print("-" * (kolom3+2) )




