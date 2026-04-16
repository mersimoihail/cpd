t = int(input())
for _ in range(t):
    s = input()
    li = []
    li.append(s[0])
    i = 1
    while i < len(s):
        li.append(s[i])
        i +=2
   
    print("".join(li))