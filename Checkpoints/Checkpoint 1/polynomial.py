class Polynomial(object):
    def __init__(self, coefficients):   # initialise variables
        self.coefficients = coefficients

    def order(self):    # returns order of our polynomial
        length = len(self.coefficients) + -1
        return length
    
    # a, b, c, d, e
    def add(self, other_coefficients):  # adds two polynomials of different lengths
        a = len(self.coefficients)
        b = len(other_coefficients)
        c = []
        d = self.coefficients
        e = other_coefficients
        if a == b:
            i = 0
            while i <= a + -1:
                c.append(float(d[i]) + float(e[i]))
                i += 1
        if a > b:
            i = 0
            while i <= b + -1:
                c.append(float(d[i]) + float(e[i]))
                i += 1
            i = b
            while i <= a + -1:
                c.append(d[i])
                i += 1
        if a < b:
            i = 0
            while i <= a + -1:
                c.append(float(d[i]) + float(e[i]))
                i += 1
            i = a
            while i <= b + -1:
                c.append(e[i])
                i += 1
        return c

    # c, d
    def differentiate(self):
        c = []
        d = len(self.coefficients) + -1
        i = 1
        while i <= d:
            if float(self.coefficients[i]) == 0:
                c.append(0)
            else:
                c.append(float(i) * float(self.coefficients[i]))
            i += 1
        return c
    
    # e, f, g
    def integrate_1(self):
        e = float(input("Enter constant of integration: "))
        f = []
        g = len(self.coefficients) + -1
        i = 0
        while i <= g:
            f.append(float(self.coefficients[i]) / float(i + 1))
            i += 1
        f.insert(0, e)
        return f
    
    # copy-paste
    def integrate_2(self, coefficients):
        e = float(input("Enter constant of integration: "))
        f = []
        g = len(coefficients) + -1
        i = 0
        while i <= g:
            f.append(float(coefficients[i]) / float(i + 1))
            i += 1
        f.insert(0, e)
        return f
    
    # h, i, j, k, l, m
    def output_1(self):
        h = len(self.coefficients) + -1
        i = 0
        j = []
        while i <= h:
            if i == 0:
                k = str(round(self.coefficients[i], 3))
            else:
                k = str(round(self.coefficients[i], 3)) + "*x^" + str(i)
            j.append(k)
            i += 1
        l = ' '
        for x in j:
            l += ' + ' + x
        l = l[4:]
        m = "p(x) = " + l
        return m

    # copy-paste
    def output_2(self, coefficients):
        h = len(coefficients) + -1
        i = 0
        j = []
        while i <= h:
            if i == 0:
                k = str(round(coefficients[i], 3))
            else:
                k = str(round(coefficients[i], 3)) + "*x^" + str(i)
            j.append(k)
            i += 1
        l = ' '
        for x in j:
            l += ' + ' + x
        l = l[4:]
        m = "p(x) = " + l
        return m