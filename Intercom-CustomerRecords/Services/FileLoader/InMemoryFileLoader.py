class InMemoryFileLoader:
    """
    Class InMemoryFileLoader represents loading the full customer file in memory for execution.
    """

    def __init__(self):
        self._lines = []
        self._lines_count = 0

    def load(self, input_file):
        with open(input_file) as file:
            self._lines = file.readlines()
        self._lines_count = len(self._lines)

    def read(self):
        idx = 0
        while True:
            if idx >= self._lines_count:
                break
            line = self._lines[idx]
            yield line.strip()
            idx += 1
