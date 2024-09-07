import math as m

angka = int(input())
if angka<=1:
    print("IT IS NOT A PRIME")
elif angka==2 or angka==3:
    print("IT IS A PRIME")
else:
    for i in range(4, m.sqrt(angka)+1):
        if angka%i==0:
            print("IT IS NOT A PRIME")
    print("IT IS A PRIME")