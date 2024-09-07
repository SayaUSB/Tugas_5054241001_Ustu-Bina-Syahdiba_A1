depan, belakang, waktu = map(int, input().split())
waktu -= 25
sendiri = False
berhenti = 0
while waktu>0:
    if depan>0:
        depan -= 1
    elif not sendiri:
        sendiri = True
    elif belakang>0:
        belakang -= 1
    else:
        break
    berhenti += 1
    waktu -= 5
    if berhenti == 12:
        waktu -= 25
if sendiri:
    print(f"YES! {belakang}")
else:
    print(f"NO! {depan+belakang+1}")