
import itertools
import math

from advanced_helpers.index_of_coincidence import index_of_coincidence
from enigma import EnigmaMachine

def fitness_value(a):
    return a[1]

def find_rotor_configuration(code, rotors):
    permutations = list(itertools.permutations(rotors, 3))
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    top_fitness_states = []

    for permutation in permutations:
        for a in alphabet:
            for b in alphabet:
                if a == b:
                    continue
                for c in alphabet:
                    if a == c or b == c:
                        continue
                    
                    starting_positions = a + " " + b + " " + c
                    rotors = permutation[0] + " " + permutation[1] + " " + permutation[2]

                    print(rotors, starting_positions)

                    ring_positions = "01 01 01"
                    plugboard = []

                    machine = EnigmaMachine(rotors, "B", ring_positions, starting_positions, plugboard)
                    decrypted = machine.encode(code)
                    fitness = abs(index_of_coincidence(decrypted) - 0.0667)
                    state = [rotors, fitness, starting_positions]

                    top_fitness_states.append(state)
                    top_fitness_states.sort(key = fitness_value, reverse = True)

                    if len(top_fitness_states) > 5:
                        top_fitness_states.pop()
        
    return top_fitness_states