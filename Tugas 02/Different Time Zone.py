# Input waktu stream dan sekarang lalu mengkorversinya menjadi detik
jam_stream, menit_stream, detik_stream = map(int, input("Masukkan waktu stream dengan format (JJ:MM:DD) : ").split(":"))
jam_skrg, menit_skrg, detik_skrg = map(int, input("Masukkan waktu sekarang dengan format (JJ:MM:DD) : ").split(":"))
waktu_stream = jam_stream*3600+menit_stream*60+detik_stream
waktu_skrg = jam_skrg*3600+menit_skrg*60+detik_skrg

# Selisih waktu dan cek kenegatifan
if waktu_skrg>86400:
    waktu_skrg %= 86400
waktu_skrg -= 3600*5
if waktu_skrg>waktu_stream:
    print("See you on the next Pear Event!")
else:
    waktu_selisih = waktu_stream-waktu_skrg
    jam = waktu_selisih//3600
    waktu_selisih %= 3600
    menit = waktu_selisih//60
    waktu_selisih %= 60
    detik = waktu_selisih
    if jam<10:
        if menit<10:
            if detik<10:
                print(f"0{jam}:0{menit}:0{detik}")
            else:
                print(f"0{jam}:0{menit}:{detik}")
        else:
            if detik<10:
                print(f"0{jam}:{menit}:0{detik}")
            else:
                print(f"0{jam}:{menit}:{detik}")
    else:
        if menit<10:
            if detik<10:
                print(f"{jam}:0{menit}:0{detik}")
            else:
                print(f"{jam}:0{menit}:{detik}")
        else:
            if detik<10:
                print(f"{jam}:{menit}:0{detik}")
            else:
                print(f"{jam}:{menit}:{detik}")