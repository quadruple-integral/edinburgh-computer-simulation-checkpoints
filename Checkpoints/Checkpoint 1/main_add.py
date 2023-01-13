from polynomial import Polynomial

def main():
    first_coefficients = []
    first_polynomial_length = int(input("Length of first polynomial: "))
    i = 1
    while i <= first_polynomial_length:
        a = float(input("a_" + str(i - 1) + " = "))
        first_coefficients.append(a)
        i += 1
    first_polynomial = Polynomial(first_coefficients)

    second_coefficients = []
    second_polynomial_length = int(input("Length of second polynomial: "))
    i = 1
    while i <= second_polynomial_length:
        a = float(input("a_" + str(i - 1) + " = "))
        second_coefficients.append(a)
        i += 1
    second_polynomial = Polynomial(second_coefficients)

    print(first_polynomial.output_2(first_polynomial.add(second_coefficients)))

main()