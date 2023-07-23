import sys
input = sys.stdin.readline

n,m = map(int,input().split())
basket = [0 for _ in range(n)]

for i in range(m):
    a,b,c = map(int,input().split())
    for j in range(a-1,b):
        basket[j] = c

for i in basket:
    print(i,end=' ')
    