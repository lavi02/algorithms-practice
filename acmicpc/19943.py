import sys
from collections import deque

class ConvexHull:
    def __init__(self):
        self.la = [0] * 101001
        self.lb = [0] * 101001
        self.sz = 0

    def cross(self, x, y):
        return (self.lb[y] - self.lb[x]) / (self.la[x] - self.la[y])

    def insert(self, a, b):
        self.la[self.sz] = a
        self.lb[self.sz] = b
        while self.sz > 1 and self.cross(self.sz - 2, self.sz - 1) > self.cross(self.sz - 1, self.sz):
            self.la[self.sz - 1] = self.la[self.sz]
            self.lb[self.sz - 1] = self.lb[self.sz]
            self.sz -= 1
        self.sz += 1

    def query(self, x):
        lo, hi = 0, self.sz - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if self.cross(mid, mid + 1) <= x:
                lo = mid + 1
            else:
                hi = mid
        return self.la[lo] * x + self.lb[lo]


def solve():
    mod = [".00", ".25", ".50", ".75"]
    for _ in range(int(sys.stdin.readline())):
        n = int(sys.stdin.readline())
        px, py = [], []
        for _ in range(n):
            x, y = map(int, sys.stdin.readline().split())
            px.append(x)
            py.append(y)

        stk = deque()
        stk.append(0)

        for next in range(1, n):
            now = stk[-1]
            dx = (px[now] + px[next] - py[now] + py[next]) / 2.0
            if dx >= px[next]:
                while dx >= px[next]:
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

        while len(stk) != 0:
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

        print(dp[n - 1] // 4, mod[dp[n - 1] % 4])

solve()

