n = int(input())
paper = [[0]*101 for _ in range(101)]
total = 0

for i in range(n):
    a, b = map(int, input().split())

    for x in range(10):
        for y in range(10):
            paper[a+x][b+y] = 1

for i in paper:
    total += sum(i)
print(total)

