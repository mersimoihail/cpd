a = input()
b = input()
c = input()
ab = a+b
abso = "".join(sorted(ab))
cc = "".join(sorted(c))
if len(cc) !=len(abso):
    print("NO")
else:
    for i in range(len(abso)):
        if abso[i] != cc[i]:
            print("NO")
            break
        elif i == len(abso)-1:
            print("YES")