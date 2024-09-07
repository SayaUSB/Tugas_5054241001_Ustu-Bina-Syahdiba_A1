masukan = input("DIMAS?! Dimasukin angkanya --> ")
digit = len(masukan)
hasil = 0
for i in range(0, digit):
    hasil += int(masukan[i])**digit
print(f"{masukan} adalah bilangan tangan kuat") if int(masukan)==hasil else print(f"{masukan} bukan bilangan tangan kuat")