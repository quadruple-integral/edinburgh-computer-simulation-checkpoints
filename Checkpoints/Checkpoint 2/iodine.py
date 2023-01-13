import numpy as np
np.set_printoptions(threshold = np.inf)
import random

class Iodine(object):
    def __init__(self, decay_constant, length, timestep):
        self.decay_constant = decay_constant
        self.length = length
        self.timestep = timestep
        self.nuclei = length * length
        self.array = np.ones((self.length, self.length), dtype = np.int8)
        self.decayed = 0
        self.undecayed = self.nuclei

    def _decay(self):
        probability = float(self.decay_constant * self.timestep)
        if random.random() <= probability:
            return True
        else:
            return False

    def _iterate(self):
        probability = float(self.decay_constant * self.timestep)
        a = self.nuclei
        b = self.array
        c = (1/2) * a
        i = a
        step = 0
        while i > c:
            with np.nditer(b, op_flags = ['readwrite']) as it:
                for x in it:
                    if random.random() <= probability:
                        if x[...] == 1:
                            x[...] = x[...] + -1
                            i += -1
                        if x[...] == 0:
                            x[...] = x[...]
                    if random.random() > probability:
                        x[...] = x[...]
            step += 1
        return (b, step)

    def iterate(self):   
        decayed_array = self._iterate()[0]
        str_nucleide = ""
        i = 0
        while i < self.length:
            str_row = ""
            j = 0
            while j < self.length:
                str_row += str(decayed_array[i,j])
                j += 1
            str_nucleide += str_row + "\n"
            i += 1
        return str_nucleide

    def half_life(self):
        return self._iterate()[1] * 0.01