import math

t = int(input())
for _ in range(t):

    length = int(input())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)

    lis = []

    
    if arr[length - 1] == arr[length - 2]:
        print("YES")
        continue   

    m = arr[-1]

    for i in range(length - 2, -1, -1):
        if arr[i] % m == 0:
            lis.append(arr[i] // m)

    if lis:
        g = 0
        for x in lis:
            g = math.gcd(g, x)   

        if g == 1:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")