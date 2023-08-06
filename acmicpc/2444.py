n = int(input())

# 공백 n-1개 + 별 2n-1개
for i in range(n-1):
    print(' '*(n-i-1) + '*'*(2*i+1))
# 별 2n-1개
print('*'*(2*n-1))
for i in range(n, 1, -1):
    print(' '*(n-i+1) + '*'*(2*i-3))