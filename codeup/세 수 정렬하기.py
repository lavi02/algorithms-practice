a, b, c = input().split()
data = []

data.append(int(a))
data.append(int(b))
data.append(int(c))

data = sorted(data)

print("%s %s %s" % (str(data[0]), str(data[1]), str(data[2])))