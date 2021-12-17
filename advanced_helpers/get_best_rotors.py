import itertools

def likely_value(a):
    return a[1]

def get_best_rotors(config):
    rotors = ""

    for enigma_state in config:
        rotors = rotors + enigma_state[0]
        rotors = rotors + " "

    rotors = rotors.split(" ")
    all_rotor_names = list(dict.fromkeys(rotors))
    all_rotor_names.remove("")

    rotor_count = {}

    for item in all_rotor_names:
        rotor_count[item] = rotors.count(item)

    top_values = []

    for item in rotor_count:
        value = rotor_count.get(item)

        top_values.append([item, value])
        top_values.sort(key = likely_value, reverse = True)

        if len(top_values) > 3:
            top_values.pop()

    top_rotors = []

    for value in top_values:
        top_rotors.append(value[0])

    return top_rotors