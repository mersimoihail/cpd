t = int(input())
for _ in range(t):
    val = 0
    s = []
    for i in range(10):
        
        temp = input()
        s.append(temp)
    for i in range(10):
        for j in range(10):
            if s[i][j] =='X':
                if i==0 or i == 9:
                    val += 1
                elif i == 1 or i == 8:
                    if j == 0 or j == 9:
                        val += 1
                    else:
                        val +=2
                elif i == 2 or i == 7:
                    if j == 0 or j == 9:
                        val += 1
                    elif j ==1 or j == 8:
                        val += 2
                    else:
                        val += 3
                elif i == 3 or i == 6:
                    if j == 0 or j == 9:
                        val += 1
                    elif j ==1 or j == 8:
                        val += 2
                    elif j == 2 or j == 7:
                        val += 3
                    else:
                        val +=4
                elif i == 4 or i == 5:
                    if j == 0 or j == 9:
                        val += 1
                    elif j ==1 or j == 8:
                        val += 2
                    elif j == 2 or j == 7:
                        val += 3
                    elif j == 3 or j == 6:
                        val +=4
                    else:
                        val +=5
    print(val)
        

