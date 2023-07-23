import sys
input = sys.stdin.readline

n,m = map(int,input().split())
basket = [x for x in range(1,n + 1)]

for x in range(m):
    a, b = map(int,input().split())
    basket[a - 1], basket[b - 1] = basket[b - 1], basket[a - 1]

for i in basket:
    print(i,end=' ')