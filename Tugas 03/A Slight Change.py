from collections import Counter

banyak = int(input("Masukkan banyak ruang : "))
ruang = list(map(int, input("Masukkan tipe ruangan : ").split()))
cek = set(ruang)
if len(cek)<=1:
    print("Banyaknya ruangan yang perlu dirombak adalah", 0)
else:
    counter = Counter(ruang)
    mayoritas = counter.most_common(1)[0][1]
    print("Banyaknya ruangan yang perlu dirombak adalah", len(ruang)-mayoritas)
