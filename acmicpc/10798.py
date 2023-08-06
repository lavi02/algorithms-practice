result = ''
datas = []

for _ in range(5):
    datas.append(input())

for i in range(15):
    for j in range(len(datas)):
        if i >= len(datas[j]):
            continue
        result += datas[j][i]

print(str(result), end='')