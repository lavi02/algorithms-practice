import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [x for x in map(int, input().split())]
data.sort()

print(data[::-1][m-1])