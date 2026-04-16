t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    zeros = 0
    cou = n//2
    eve =0
    for i in range(n):
        if s[i] == '0':
            zeros +=1
        else:
            if zeros %2 !=0:
                eve +=1
            zeros = 0
    cou -= eve//2
    if s[n-1] =='1':
        cou +=1
    print(cou)

    