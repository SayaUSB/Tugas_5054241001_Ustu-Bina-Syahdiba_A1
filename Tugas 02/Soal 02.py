# Input berat badan dalam pounds dan tinggi dalam inch
berat = float(input("Masukkan berat badan (pound) : "))
tinggi = float(input("Masukkan tinggi badan (inch) : "))

# Kalkulasi index massa tubuh
index = 703*berat/tinggi

# Mengkategorikan index massa tubuh
print("Index massa tubuh : 0", end="")
if index<18.5:
    print("Underweight")
elif index>=18.5 and index<=24.9:
    print("Normal")
elif index>=25 and index<=29.9:
    print("Overweight")
else:
    print("Obese")
