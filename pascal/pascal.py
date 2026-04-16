def Ncr(n,r):
    summation = 1
    for i in range(r):
        summation *= n - i
        summation /= i+1
    return summation
row , column = map(int,input().split())
result = Ncr(row-1,column-1)
print(result)
