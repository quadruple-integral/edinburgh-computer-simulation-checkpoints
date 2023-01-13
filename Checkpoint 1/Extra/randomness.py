class Randomness(object):
    m = 233280
    a = 9301
    c = 49297

    # seed
    # max_value - maximum value
    # number - number of desired random numbers

    def __init__(self, seed, max_value, number):
        self.seed = float(seed * self.a + self.c) % self.m
        self.stem = abs(self.seed / self.m)
        self.max_value = float(max_value)
        self.number = int(number)

    def generate_int(self):  # generate integers
        a = []
        i = 1
        while i <= self.number:
            b = int((self.stem * (10 ^ (i + 3)) * self.max_value) % self.max_value)
            a.append(b)
            i += 1
        return a
    
    def generate_09(self): # generate from 0 to 9
        a = []
        i = 1
        while i <= self.number:
            b = int((self.stem * (10 ^ (i + 3)) * 10) % 10)
            a.append(b)
            i += 1
        return a
    
    def generate_float(self):
        return self.stem