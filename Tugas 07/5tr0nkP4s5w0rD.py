pw, angka = map(str, input().split())
angka = int(angka)
sAngka = False
sKapital = False
total = 0
for i in range(len(pw)):
    if pw[i].isdigit():
        sAngka = True
        total += int(pw[i])
    if pw[i].isupper():
        sKapital = True
if not sAngka:
    print("Password needs number")
if not sKapital:
    print("Password requires at least one uppercase letter")
if angka!=total:
    print("Digits in password not equal to key")
if not sAngka or not sKapital or angka!=total:
    print("Weak password, fix your mistakes")
else:
    print("Password is strong, just like you")
    