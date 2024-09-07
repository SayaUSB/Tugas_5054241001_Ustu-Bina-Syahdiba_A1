# Input penggunaan data
data = float(input("Data usage (GB) : "))

# Kategori tagihan penggunaan data
if data>0 and data<=1:
    tagihan = 250
elif data>1 and data<=2:
    tagihan = 500
elif data>2 and data<=5:
    tagihan = 1000
elif data>5 and data<=10:
    tagihan = 1500
elif data>10:
    tagihan = 2000
else:
    tagihan = "Bad input"

# Output tagihan penggunaan data
print(f"Your data bill : ${tagihan}")