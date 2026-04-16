t = int(input())
for _ in range(t):
    length = int(input())
    s = input()

    po = 0
    tot = 0
    ind = 0
    while ind < length:
        if s[ind] == '.':
            po +=1
        else:
            tot += po
            po = 0
        if po >=3:
            print(2)
            break
        ind += 1
        if ind == length:
            tot += po
            print(tot)



    
