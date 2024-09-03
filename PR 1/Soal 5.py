# Input banyaknya infus dalam mL dan waktu dalam menit
infus = float(input("Volume to be infused (ml) => "))
menit = float(input("Minutes over which to infuse => "))
jam = menit/60

#Output
print("VTBI : %.2f" %infus)
rate = infus/jam
print("Rate : %.2f mL/hr" %rate)