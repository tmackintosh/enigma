import math

def get_binary(number):
    string = ""

    while number != 0:
        if number % 2 != 0:
            string = "1" + string
        else:
            string = "0" + string

        number = math.floor(number / 2)

    return string

def get_permutations(rotors):
    return rotors

def get_rotors(rotors):
    if len(rotors) < 3:
        return []

    possible_rotors = []

    for i in range (7, 2 ** (len(rotors))):
        selection = get_binary(i)
        rotor_combo = []

        while len(selection) != len(rotors):
            selection = "0" + selection

        for j in range(0, len(selection)):
            if selection[j] == "1":
                rotor_combo.append(rotors[j])

        if len(rotor_combo) != 3:
            continue

        possible_rotors.append(rotor_combo)

    return possible_rotors

print(get_rotors(["I", "II", "III", "IV"]))