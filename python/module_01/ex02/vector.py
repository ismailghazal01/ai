class Vector:
    def __init__(self, values):
        if isinstance(values, int):
            self.values = [[float(i)] for i in range(values)]
        elif isinstance(values, tuple):
            self.values = [[float(i)] for i in range(values[0], values[1])]
        elif isinstance(values, list):
            self.values = values
        else:
            raise TypeError

        if len(self.values) == 1:
            self.shape = (1, len(self.values[0]))
        else:
            self.shape = (len(self.values), 1)

    def dot(self, other):
        result = 0
        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                result += self.values[i][j] * other.values[i][j]
        return result

    def T(self):
        if self.shape[0] == 1:
            return Vector([[x] for x in self.values[0]])
        else:
            return Vector([[row[0] for row in self.values]])

    def __add__(self, other):
        return Vector([[self.values[i][j] + other.values[i][j]
                        for j in range(len(self.values[i]))]
                       for i in range(len(self.values))])

    def __sub__(self, other):
        return Vector([[self.values[i][j] - other.values[i][j]
                        for j in range(len(self.values[i]))]
                       for i in range(len(self.values))])

    def __mul__(self, other):
        return Vector([[x * other for x in row] for row in self.values])

    def __truediv__(self, other):
        return Vector([[x / other for x in row] for row in self.values])

    def __repr__(self):
        return str(self.values)