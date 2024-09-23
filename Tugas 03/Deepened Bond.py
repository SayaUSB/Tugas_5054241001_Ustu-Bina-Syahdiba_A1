from itertools import product

banyak = int(input("Masukkan banyak perulangan : "))
for _ in range(banyak):
    flag = 0
    target = int(input("Masukkan angka : "))
    pangkat = []
    i = 1
    while i**2<=target:
        pangkat.append(i**2)
        i += 1
    kombinasi = list(product(pangkat, repeat=4))
    for a in range(len(kombinasi)):
        for i in kombinasi[a]:
            if sum(kombinasi[a])==target:
                print("LEAVE")
                flag = 1
                break
        if flag==1:
            break
    if flag!=1:
        print("ERASE")
    

