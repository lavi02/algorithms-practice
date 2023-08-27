import sys
input = sys.stdin.readline

class ConvexHull:
    def __init__(self):
        self.la = [0] * 101001
        self.lb = [0] * 101001
        self.sz = 0
        self.pointer = 0

    def cross(self, x, y):
        return (self.lb[y] - self.lb[x]) / (self.la[x] - self.la[y])

    def insert(self, a, b):
        self.la[self.sz] = a
        self.lb[self.sz] = b
        for _ in range(self.sz - 1, 0, -1):
            if self.sz < 2 or self.cross(self.sz - 2, self.sz - 1) <= self.cross(self.sz - 1, self.sz):
                break
            self.la[self.sz - 1] = self.la[self.sz]
            self.lb[self.sz - 1] = self.lb[self.sz]
            self.sz -= 1
        self.sz += 1


    def query(self, x):
        pointer = self.pointer
        for _ in range(self.sz - 1 - pointer):
            if self.cross(pointer, pointer + 1) <= x:
                pointer += 1
            else:
                break
        self.pointer = pointer
        return self.la[pointer] * x + self.lb[pointer]



mod = [".00", ".25", ".50", ".75"]
for _ in range(int(input())):
    n = int(input())
    px, py = [], []
    for _ in range(n):
        x, y = map(int, input().split())
        px.append(x)
        py.append(y)

    stk = []
    stk.append(0)
    for next in range(1, n):
        now = stk[-1]
        dx = (px[now] + px[next] - py[now] + py[next]) / 2.0
        if dx >= px[next]:
            for _ in range(n):
                if dx < px[next]:
                    break
                stk.pop()
                if len(stk) == 0:
                    break
                now = stk[-1]
                dx = (px[now] + px[next] - py[now] + py[next]) / 2.0
            stk.append(next)
        elif dx <= px[now]:
            pass
        else:
            stk.append(next)

    n = len(stk)
    lx, ly = [], []

    for _ in range(len(stk)):
        top = stk.pop()
        lx.append(px[top])
        ly.append(py[top])

    lx.reverse()
    ly.reverse()

    hull = ConvexHull()
    dp = [0] * (n + 1)
    hull.insert(-2 * (lx[0] - ly[0]), (lx[0] - ly[0]) * (lx[0] - ly[0]))
    for i in range(n):
        u = lx[i] + ly[i]
        v = lx[i + 1] - ly[i + 1] if i + 1 < n else 0
        dp[i] = hull.query(u) + u * u
        hull.insert(-2 * v, v * v + dp[i])
    
    data = "".join([str(dp[n - 1] // 4), mod[dp[n - 1] % 4], "\n"])
    sys.stdout.write(data)
