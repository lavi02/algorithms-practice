import sys
input = sys.stdin.readline

n, m = map(int, input().split())
basket = [x for x in range(1,n + 1)]

for x in range(m):
    a, b = map(int, input().split())
    basket = basket[:a-1] + basket[a-1:b][::-1] + basket[b:]
for i in basket:
    print(i,end=' ')

# try:
#     while True:
#         a, b = map(int, input().split())
#         if a < b: a, b = b, a
#         basket = basket[:b - 1] + basket[b - 1:a:-1] + basket[a:]

# except:
#     for i in basket:
#         print(i,end=' ')
#     exit()