t = int(input())

for _ in range(t):
    k = int(input())
    count = 0
    for i in range(k):
        count +=1
        if count % 10 == 3 or count % 3 ==0:
            count+=1
    print(count)

   
