t = int(input())
for _ in range(t):
    minimums = []
    summation = 1
    n , k = map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    length = len(arr1)
    for i in range(length):
        if arr1[i] >=arr2[i]:
            summation += arr1[i]
            minimums.append(arr2[i])
        else:
            summation += arr2[i]
            minimums.append(arr1[i])
    minimums.sort(reverse = True)
    for i in range(k-1):
        summation += minimums[i]
    print(summation)


