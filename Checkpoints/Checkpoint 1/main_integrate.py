from polynomial import Polynomial

def main():
    coefficients = []
    polynomial_length = int(input("Length of polynomial: "))
    i = 1
    while i <= polynomial_length:
        a = float(input("a_" + str(i - 1) + " = "))
        coefficients.append(a)
        i += 1
    a = coefficients
    our_polynomial = Polynomial(coefficients)
    print(our_polynomial.output_2(our_polynomial.integrate_1()))

main()