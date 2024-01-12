class Bottle:
    def __init__(self, size, value):
        self.size = size
        self.value = value
        self.rings_allocated = 0
        self.p_in_play = 1