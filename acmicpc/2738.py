x, y = map(int, input().split())
first = [[0 for _ in range(y)] for _ in range(x)]
second = [[0 for _ in range(y)] for _ in range(x)]

for i in range(x):
    first[i] = list(map(int, input().split()))

for i in range(x):
    second[i] = list(map(int, input().split()))

result = [[0 for _ in range(y)] for _ in range(x)]

for i in range(x):
    for j in range(y):
        result[i][j] = first[i][j] + second[i][j]

for i in range(x):
    for j in range(y):
        print(result[i][j], end=' ')
    print()

        