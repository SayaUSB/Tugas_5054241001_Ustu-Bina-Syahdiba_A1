x = int(input())
spasi = x-1
for i in range(1, x+1):
    print(" "*spasi,end="")
    print("*"*(i*2-1),end="")
    print(" "*spasi, end=" ")
    print("\tBintang :", i*2-1, "\tSpasi :", spasi)
    spasi -= 1
spasi = 1
for i in range(x-1, 0, -1):
    print(" "*spasi,end="")
    print("*"*(i*2-1),end="")
    print(" "*spasi, end=" ")
    print("\tBintang :", i*2-1, "\tSpasi :", spasi)
    spasi += 1