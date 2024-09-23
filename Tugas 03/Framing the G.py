besar, tebal = map(int, input().split())
a = tebal
b = besar-a*2
for i in range(1, besar//2+2 if besar%2==1 else besar//2+1):
    if i==0 or i<=tebal:
        print("*"*besar)
    else:
        print("*"*a+" "*b+"*"*a)
        a += 2
        b -= 2
a -= 2
b += 2
for i in range(besar//2+2 if besar%2==1 else besar//2+1, besar+1):
    if i==besar or i>besar-tebal:
        print("*"*besar)
    else:
        print("*"*a+" "*b+"*"*a)
        a -= 2
        b += 2
       
    
