import sys
input = sys.stdin.readline

k = int(input())
data = []
for _ in range(k):
    n, m = input().split()
    data.append([int(n), m])

data.sort(key=lambda x: x[0])

for i in range(k):
    print(data[i][0], data[i][1])