class CsvReader:
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.file = None
        self.data = []

    def __enter__(self):
        try:
            self.file = open(self.filename, "r")
            lines = self.file.read().splitlines()
            self.data = [line.split(self.sep) for line in lines]

            length = len(self.data[0])
            for row in self.data:
                if len(row) != length:
                    return None

            return self
        except:
            return None

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

    def getdata(self):
        start = self.skip_top + (1 if self.header else 0)
        end = len(self.data) - self.skip_bottom
        return self.data[start:end]

    def getheader(self):
        if self.header:
            return self.data[0]
        return None