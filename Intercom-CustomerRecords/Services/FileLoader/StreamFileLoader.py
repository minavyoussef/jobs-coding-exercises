class StreamFileLoader:
    """
    Class StreamFileLoader represents reading file as stream if it is too big to be fitted in the memory.
    """

    def __init__(self):
        self._input_file = None

    def load(self, input_file):
        self._input_file = input_file

    def read(self):
        if self._input_file is None:
            raise Exception('File not loaded')

        with open(self._input_file) as infile:
            for line in infile:
                yield line
