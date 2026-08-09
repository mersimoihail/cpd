
lis = [True] * 200000
lis[0] = lis[1] = False
prime = []
for i in range(2,200000):
    if lis[i]:
        prime.append(i)

        for j in range(i+i,200000,i):
            lis[j] = False
t = int(input())
for _ in range(t):
    n = int(input())
    gc = [2]
    for i in range(n-1):
        gc.append(prime[i]*prime[i+1])
    print(*gc)




