result = [[0 for _ in range(9)] for _ in range(9)]
max = 0; a = 0; b = 0

for x in range(9):
    result[x] = list(map(int, input().split()))

for i in range(9):
    for x in range(9):
        if result[i][x] > max:
            max = result[i][x]
            a = i
            b = x

print(max)
print(a+1, b+1)