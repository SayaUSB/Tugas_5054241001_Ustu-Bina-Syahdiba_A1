def namaku(nama, umur):
    print(f"Nama saya adalah {nama} dan umur saya adalah {umur} tahun")

def penjumlahan_ambangka(angka1, angka2):
    hasil = (angka1+angka2)**(angka1-angka2)
    return hasil

def nama_hari(*hari):
    for h in hari:
        print(f"Hari ini adalah hari {h}")

def nama_bulan(bulan):
    for key, value in bulan.items():
        print(f"Bulan {key} adalah bulan ke-{value}")

def negara(country="Indonesia", continent="Asia"):
    print(f"Negara saya adalah {country}, which is located in {continent}")

def list_array(*args):
    for arg in args:
        print(arg)

def fungsi_a(x, y, /):
    print(x, y)

def fungsi_b(a, b, /, *, c, d):
    print(a+b+c+d)

if __name__ == "__main__":
    namaku("Sigma", 20)
    print(f"Penjumlahan ambangka dari 10 dan 5 adalah {penjumlahan_ambangka(4, 2)}")
    nama_hari("Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu")
    nama_bulan({"Januari":1, "Februari":2, "Maret":3, "April":4, "Mei":5, "Juni":6, "Juli":7, "Agustus":8, "September":9, "Oktober":10, "November":11, "Desember":12})
    negara()
    negara("Jepang")
    negara("Amerika Serikat", "Amerika")
    negara(continent="Eropa")
    negara(continent="Australia", country="Australia")
    list_array("Satu", "Dua", "Tiga", "Empat", "Lima")
    fungsi_a(10, 20)
    # fungsi_a(y=10, x=20) # Error
    fungsi_b(1, 2, c=3, d=4)