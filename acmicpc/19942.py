import sys

def diet():
    N = int(input())
    mp, mf, ms, mv = map(int, input().split())
    nutrient = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    result = [float('inf'), []]

    for i in range(1 << N):
        p = f = s = v = cost = 0
        temp = []
        for j in range(N):
            if i & (1 << j):
                p += nutrient[j][0]
                f += nutrient[j][1]
                s += nutrient[j][2]
                v += nutrient[j][3]
                cost += nutrient[j][4]
                temp.append(j+1)

        if mp <= p and mf <= f and ms <= s <= ms and mv <= v and cost < result[0]:
            result = [cost, temp]

    if result[0] == float('inf'):
        return -1
    else:
        cost = result[0]
        data = ' '.join(map(str, result[1]))
        return str(cost) + '\n' + data

print(diet())
