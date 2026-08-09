li = list(map(int,input().split()))
lis = []
litter =( li[1] *li[2])//li[6]
lis.append(litter)
slices = li[3]*li[4]
lis.append(slices)
grams = li[5]//li[-1]
lis.append(grams)
mi = lis[0]
mi = min(lis[1],mi)
mi = min(lis[2],mi)
print(mi//li[0])