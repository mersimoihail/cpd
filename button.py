t = int(input())
for i in range(t):
    a , k ,bo = map(int,input().split())
    if bo % 2 !=0:
        a+=1
    if a <=k:
        print("Second")
    else:
        print("First")
        