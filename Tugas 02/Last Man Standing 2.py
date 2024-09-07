total_bola, mulai = map(int, int(input()))
kemungkinan = [False]*(total_bola+1)
kemungkinan[1] = True
if total_bola >= 2:
    kemungkinan[2] = True
if total_bola >= 5:
    kemungkinan[5] = True
for i in range(3, total_bola+1):
    if i>=1 and not kemungkinan[i-1]:
        kemungkinan[i] = True
    elif i>=2 and not kemungkinan[i-2]:
        kemungkinan[i] = True
    elif i>=5 and not kemungkinan[i-5]:
        kemungkinan[i] = True
if mulai==1 and kemungkinan[total_bola] or mulai==2 and not kemungkinan[total_bola]:
    print("Lala")
else:
    print("Lili")