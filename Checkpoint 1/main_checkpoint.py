from polynomial import Polynomial

def main():
    a_coefficients = [2, 0, 4, -1, 0, 6]
    a_polynomial = Polynomial(a_coefficients)
    print(a_polynomial.output_1())

    b_coefficients = [-1, -3, 0, 4.5]
    b_polynomial = Polynomial(b_coefficients)
    print(b_polynomial.output_1())
    print("")

    print("Find the order of polynomial_a")
    print(a_polynomial.order())
    print("")

    print("Find the sum of a_polynomial and b_polynomial")
    print(a_polynomial.output_2(a_polynomial.add(b_coefficients)))
    print("")

    print("Find the first derivative of a_polynomial")
    print(a_polynomial.output_2(a_polynomial.differentiate()))
    print("")

    print("Find the antiderivative of the previous result")
    print(a_polynomial.output_2(a_polynomial.integrate_2(a_polynomial.differentiate())))
    print("")

main()