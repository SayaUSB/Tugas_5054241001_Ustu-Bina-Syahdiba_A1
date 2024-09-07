# Output interface
print("(1) First Free Service")
print("(2) Second Free Service")

# Input tipe service dan jarak
tipe = int(input("Enter the Free Service number >> "))
jarak = int(input("Enter number of Miles >> "))

# Kategorisasi apakah harus service atau tidak
if (tipe==1 and jarak>1500 and jarak<=3000) or (tipe==1 and jarak>3001 and jarak<=4500):
    print("Vehicle must be serviced.")
else:
    print("Vehicle don't have to be serviced")
