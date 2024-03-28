class Array:
    values = []

    def __init__(self, str_array):
        self.values = str_array[:-1].split(' ')

