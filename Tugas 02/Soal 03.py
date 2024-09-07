# Variabel untuk benar atau salah dan nilai
P = [True, False]
Q = [True, False]
nilai = 0

# Ujian pemahaman operasi 'and' dan 'or'
for i in range(0, len(P)):
    for j in range(0, len(Q)):
        jawaban = input(f"Hasil dari operasi (&&) P berisi {P[i]} dan Q berisi {Q[j]} \t===> ")
        if jawaban==str(P[i] and Q[j]):
            print("Anda benar!")
            nilai += 1
        else:
            print("Kesalahan berpikir!")
for i in range(0, len(P)):
    for j in range(0, len(Q)):
        jawaban = input(f"Hasil dari operasi (||) P berisi {P[i]} dan Q berisi {Q[j]} \t===> ")
        if jawaban==str(P[i] or Q[j]):
            print("Anda benar!")
            nilai += 1
        else:
            print("Kesalahan berpikir!")

# Output skor ujian
nilai = (nilai/8)*100
print(f"Nilai ujian : {nilai}") if nilai>=75 else print("REMED WALAWE!!!")