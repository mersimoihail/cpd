t = int(input())
for _ in range(t):
    n,k,p,m = map(int,input().split())
    lis = list(map(int,input().split()))
    temp = lis[p-1]
    played = 0
    if k == n:
        played += m //lis[p-1]
    else:
        if k > p:
            del lis[p-1]
            m -= temp
            played += 1
            lis.sort()
            efo = 0
            min = lis[0]
            for i in range(0,k-1):
                if min > lis[i]:
                    min = lis[i]
            for 