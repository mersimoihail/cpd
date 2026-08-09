n = int(input())
lis = list(map(int,input().split()))
maxim,minim = lis[0],lis[0]
bre = 0
for i in range(n):
    if lis[i] > maxim:
        maxim = lis[i]
        bre +=1
    if lis[i] < minim:
        bre +=1
        minim = lis[i]
print(bre)