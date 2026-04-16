t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    a,b = map(int,input().split())
    if a*2 <=b:
        print((x+y)*a)
    else:
        mini = min(x,y)
        maxi = max(x,y)
        print(mini*b+((maxi-mini)*a))