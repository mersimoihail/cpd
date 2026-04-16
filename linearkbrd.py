t = int(input())
for _ in range(t):
    orde = {}
    keyboard = input()
    stri = input()
    num = 1 
    tim = 0
    for i in keyboard:
        orde[i] = num
        num +=1
    for i in range(len(stri)-1):
        tim += abs(orde[stri[i]] - orde[stri[i+1]])
    print(tim)

    
