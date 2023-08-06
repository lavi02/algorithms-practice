n, m = map(int, input().split())
min_count = float('inf')
board = []

for _ in range(n):
    data = input()
    row = [i for i in data]
    board.append(row)

for i in range(n - 7): # row
    for j in range(m - 7): # col
        for first in ['W', 'B']:
            count = 0
            for k in range(8):
                for l in range(8):
                    if (i+k+j+l) % 2 == 0 and board[i+k][j+l] != first:
                        count += 1
                    elif (i+k+j+l) % 2 == 1 and board[i+k][j+l] == first:
                        count += 1
            min_count = min(min_count, count)

print(min_count)
