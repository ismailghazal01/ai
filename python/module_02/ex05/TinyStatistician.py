class TinyStatistician:
    def mean(self, x):
        if not x:
            return None
        return sum(x) / len(x)

    def median(self, x):
        if not x:
            return None
        x = sorted(x)
        n = len(x)
        mid = n // 2
        if n % 2 == 0:
            return (x[mid - 1] + x[mid]) / 2
        return float(x[mid])

    def quartiles(self, x):
        if not x:
            return None
        x = sorted(x)
        n = len(x)
        return [float(x[n // 4]), float(x[(3 * n) // 4])]

    def var(self, x):
        if not x:
            return None
        m = self.mean(x)
        return sum((i - m) ** 2 for i in x) / len(x)

    def std(self, x):
        if not x:
            return None
        return self.var(x) ** 0.5