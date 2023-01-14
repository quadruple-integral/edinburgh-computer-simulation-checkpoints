from iodine import Iodine

def main():
    """ print("decay_constant = 0.02775")
    decay_constant = float(input("Decay constant: "))
    print("length = 50")
    length = int(input("Length of array: "))
    print("timestep = 0.01")
    timestep = float(input("Timestep: ")) """
    print("Legend: 0 for decayed;\n\t1 for undecayed\n")
    decay_constant = 0.02775
    length = 50
    timestep = 0.01
    iodine = Iodine(decay_constant, length, timestep)
    print(iodine.iterate())
    print("Simulated half life: " + str(iodine.half_life) + " mins\n")
    print("Actual half life: 24.98 mins\n")

main()