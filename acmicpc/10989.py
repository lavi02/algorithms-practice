import sys
input = sys.stdin.readline

n = int(input())
inputData = [0] * 10001
for _ in range(n):
    inputData[int(input())] += 1

for i in range(10001):
    if inputData[i] != 0:
        for _ in range(inputData[i]):
            print(i)
