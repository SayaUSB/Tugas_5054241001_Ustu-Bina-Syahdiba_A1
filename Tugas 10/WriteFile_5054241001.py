file = open("MyFamily.txt", "w")
print("Keluargamu leee")
jumlah = int(input("Berapa anggota keluarga kamu? "))
for i in range(1, jumlah + 1):
    nama = input(f"Anggota ke-{i}: ")
    file.write(f"{nama}\n")
file.close()

file = open("MyFamily.txt", "r")
print("Anggota keluargamu:")
for line in file:
    print(line.strip())
