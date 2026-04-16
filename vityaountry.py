lis = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
n = int(input())
consi = list(map(int,input().split()))
next_n = []
for i in range(len(lis)):
    if lis[i] == consi[0]:
        for j in range(n):
            if lis[(i+j)%len(lis)] != consi[j]:
                break
            if j+1 == n:
                next_n.append(lis[(i+j+1)%len(lis)])
if next_n:
    if next_n[0] > consi[-1]:
        for i in range(len(next_n)):
            if next_n[i] <consi[-1]:
                print(-1)
                break
            if i+1 == len(next_n):
                print("UP")
    if next_n[0] < consi[-1]:
        for i in range(len(next_n)):
            if next_n[i] > consi[-1]:
                print(-1)
                break
            if i+1 == len(next_n):
                print("DOWN")
else:
    print(-1)

