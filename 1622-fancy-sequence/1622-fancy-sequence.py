class Fancy:
    def __init__(self):
        self.x = []
        self.add = 0
        self.mul = 1
        self.mod = 10**9 + 7
        self.inv = [0, 1]
        for i in range(2, 101):
            self.inv.append((self.mod - self.mod//i) * self.inv[self.mod%i] % self.mod)

    def append(self, val: int) -> None:
        self.x.append(((val - self.add) * pow(self.mul, self.mod-2, self.mod)) % self.mod)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.mod

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % self.mod
        self.add = (self.add * m) % self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.x):
            return -1
        return (self.x[idx] * self.mul + self.add) % self.mod

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)