n = int(input())
output = 0
for i in range(0, n):
    output += (2**i)*sum(range(1,n+1))
    n -= 1
print(output)