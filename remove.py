t = int(input())
for i in range(t):
    s = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    if s ==1:
        print("YES")
        continue
    else:
        l=0
        for k in range(s-1):
            if abs(arr[k]-arr[k+1])<=1:
                l+=1
            else:
                print("NO")
                break
        if l == s-1:
            print("YES")

