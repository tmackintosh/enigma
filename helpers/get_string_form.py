def get_string_form(rotors):
    string = ""

    for rotor in rotors:
        if string == "":
            string = rotor
        else:
            string = string + " " + rotor

    return string