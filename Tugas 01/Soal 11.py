import math

# Input sisi m dan n
m = int(input("Masukkan sisi m --> "))
n = int(input("Masukkan sisi n --> "))

# Kalkulasi sisi 1, sisi 2, hipotanus
sisi1 = abs(m**2-n**2)
sisi2 = 2*m*n
hipotanus = m**2+n**2

# Output sisi 1, sisi 2, hipotanus
print(f"sisi1 = {sisi1}")
print(f"sisi2 = {sisi2}")
print(f"hipotanus = {hipotanus}")