t = int(input())
for j in range(t):
    swap =0
    count_a =0
    m = int(input())
    st =input()
    i=0
    while i < m-1:
        if st[i] =='A':
            count_a +=1
        elif st[i] =='B' and count_a != 0:
            swap+=count_a
            count_a=0
            while st[i+1]=='B' and i+1 != m-1:
                i+=1
                swap+=1
                i+=1
    if st[m-1]=='B':
        swap+=count_a
        
    print(swap)
        
            
        

