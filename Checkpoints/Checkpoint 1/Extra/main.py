from randomness import Randomness

def main():
    #seed = float(input("Please enter seed: "))
    #max_value = int(input("Please enter max value: "))
    #number = int(input("Desired numbers of generated values: "))
    seed, max_value, number = 100, 5, 5
    our_random_number = Randomness(seed, max_value, number)
    print(str(our_random_number.generate_float()))

main()