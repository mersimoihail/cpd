t = int(input())
for _ in range(t):
    liod = []
    liev = []
    n = int(input())
    if (n//2)%2 != 0:
        print("NO")
    else:
        print("YES")
        for i in range(n//2):
            liev.append((2*i+1)*2)
        for i in range(len(liev)):
            if i%2 == 0:
                liod.append(liev[i]-1)
            else:
                liod.append(liev[i] +1)

        for i in liod:
            liev.append(i)
        for i in range(len(liev)):
            print(liev[i],end =" ")