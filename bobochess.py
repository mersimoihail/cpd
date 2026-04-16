n, m, sx, sy = map(int, input().split())

# Step 1: start
print(sx, sy)

# Step 2: finish the starting row
for j in range(sy - 1, 0, -1):
    print(sx, j)

for j in range(sy + 1, m + 1):
    print(sx, j)

# Step 3: go through other rows
current_col = m  # we ended at column m

for i in range(sx + 1, n + 1):
    print(i, current_col)
    if current_col == m:
        for j in range(m - 1, 0, -1):
            print(i, j)
        current_col = 1
    else:
        for j in range(2, m + 1):
            print(i, j)
        current_col = m

for i in range(sx - 1, 0, -1):
    print(i, current_col)
    if current_col == m:
        for j in range(m - 1, 0, -1):
            print(i, j)
        current_col = 1
    else:
        for j in range(2, m + 1):
            print(i, j)
        current_col = m