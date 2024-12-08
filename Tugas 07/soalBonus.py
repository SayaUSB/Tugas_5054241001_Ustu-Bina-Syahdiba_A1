def ganteng(n):
    if n==1:
        return n
    elif n%2==0:
        return 1+ganteng(n//2)
    else:
        return 1+ganteng(n-1)

n = int(input())
print(ganteng(n))