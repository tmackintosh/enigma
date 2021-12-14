import itertools

from classes.PlugLead import PlugLead
from classes.Plugboard import Plugboard
from classes.Rotor import Rotor

from helpers.length_assertion import length_assertion
from helpers.lexigraphical_range_assertion import lexigraphical_range_assertion
from helpers.numerical_assertion import numerical_assertion
from helpers.type_assertion import type_assertion
from helpers.is_even import is_even
from helpers.get_setting import get_setting
from helpers.get_string_form import get_string_form

class EnigmaMachine:
    def __init__(self, rotors, reflector, ring_settings = "01 01 01", initial_positions = "A A A", plugboard_pairs = []):
        """
        Instantiates an enigma machine object that can encode messages.

        @param rotors, a string with the different rotors space separated, "I II III"
        @param reflector, a string of the reflector rotor
        @param ring_settings, a string with the different settings space separated, "01 01 01"
        @param initial_positions, a string with the different positions space separated, "A A A"
        @param plugboard_pairs, a list of strings for each plug lead's encryption

        @returns enigma object
        """
        # Method defense
        type_assertion(rotors, str)
        type_assertion(reflector, str)
        type_assertion(ring_settings, str)
        type_assertion(initial_positions, str)

        self.initialize_rotors(rotors, reflector, ring_settings, initial_positions)
        self.initialize_plugboard(plugboard_pairs)

    def initialize_plugboard(self, plugs):
        """
        Sets the object's plugboard attribute to a new plugboard object configured
        with the leads as layed out in the plugs parameter.

        @param plugs, a list of strings for each plug lead's encryption

        @returns nothing
        """
        self.plugboard = Plugboard()

        for plug in plugs:
            self.plugboard.add(PlugLead(plug))

    def initialize_rotors(self, rotors, reflector, ring_settings, positions):
        """
        Sets the object's rotor configuration as well as their initial status.

        Also tags adjacent rotors as attributes to rotors. For example, the
        left-most rotor will have the middle rotor as it's right-connection
        object.

        @param rotors, a string with the different rotors space separated, "I II III"
        @param reflector, a string of the reflector rotor
        @param ring_settings, a string with the different settings space separated, "01 01 01"
        @param positions, a string with the different positions space separated, "A A A"
        @returns nothing
        """
        # Method defense
        type_assertion(rotors, str)
        type_assertion(ring_settings, str)
        type_assertion(positions, str)

        ring_settings = ring_settings.split(" ")
        rotors = rotors.split(" ")
        positions = positions.split(" ")

        if len(rotors) != len(ring_settings) or len(rotors) != len(positions) or len(ring_settings) != len(positions):
            raise ValueError("You must provide the same number of inputs for each rotor")

        # Instantiate rotors
        self.right_rotor = rotor_from_name(rotors[2], ring_settings[2], positions[2])
        self.middle_rotor = rotor_from_name(rotors[1], ring_settings[1], positions[1])
        self.left_rotor = rotor_from_name(rotors[0], ring_settings[0], positions[0])

        rotor_objects = []
        self.reflector = rotor_from_name(reflector)

        for i in range (0, len(rotors)):
            new_rotor = rotor_from_name(rotors[i], ring_settings[i], positions[i])
            
            if i == 0:
                new_rotor.left_connection = self.reflector
                self.reflector.right_connection = new_rotor
            else:
                left_rotor = rotor_objects[i - 1]

                new_rotor.left_connection = rotor_objects[i - 1]
                left_rotor.right_connection = new_rotor

            rotor_objects.append(new_rotor)

        self.starting_rotor = rotor_objects[len(rotor_objects) - 1]
        self.reflector.right_connection = rotor_objects[0]

    def encode(self,text):
        """
        Encodes a piece of text through the enigma machine in its current state.

        @param text, the string of text to encode
        @return string of encoded text
        """
        encoded = ""

        for character in text:
            # Rotations happen at the start of every key press
            self.starting_rotor.rotate()

            character = self.plugboard.encode(character)
            current_rotor = self.starting_rotor

            # Traverse to the left
            while current_rotor.left_connection is not None:
                character = current_rotor.encode_right_to_left(character)
                current_rotor = current_rotor.left_connection

            character = current_rotor.encode_right_to_left(character)
            current_rotor = current_rotor.right_connection

            # Traverse to the right
            while current_rotor.right_connection is not None:
                character = current_rotor.encode_left_to_right(character)
                current_rotor = current_rotor.right_connection

            character = current_rotor.encode_left_to_right(character)
            encoded = encoded + self.plugboard.encode(character)

        return encoded

# method which returns a Rotor object
# @param - name - name of the Rotor e.g. I or Gamma
# @param - setting - initial setting for rotor
# @param - position - initial position of rotor
def rotor_from_name(name, setting = "01", position = "A"):
    # Method defense
    type_assertion(name, str)
    type_assertion(setting, str)
    type_assertion(position, str)
    numerical_assertion(setting)
    lexigraphical_range_assertion(position, "A", "Z")
    length_assertion(position, 1)
    length_assertion(setting, 2)

    mappings = {
        "Beta": "LEYJVCNIXWPBQMDRTAKZGFUHOS",
        "Gamma": "FSOKANUERHMBTIYCWLQPZXVGJD",
        "I": "EKMFLGDQVZNTOWYHXUSPAIBRCJ Q",
        "II": "AJDKSIRUXBLHWTMCQGZNPYFVOE E",
        "III": "BDFHJLCPRTXVZNYEIWGAKMUSQO V",
        "IV": "ESOVPZJAYQUIRHXLNFTGKDCMWB J",
        "V": "VZBRGITYUPSDNHLXAWMJQOFECK Z",
        "A": "EJMZALYXVBWFCRQUONTSPIKHGD",
        "B": "YRUHQSLDPXNGOKMIEBFZCWVJAT",
        "C": "FVPJIAOYEDRZXWGCTKUQSBNMHL"
    }

    rotor_mapping = mappings.get(name)
    if rotor_mapping is None:
        raise ValueError("Name of mapping must be a valid rotor name, got", name)

    return Rotor(mappings[name], setting = setting, position = position)

# method with returns an fully set up enigma machine object
# @param - rotors - string of the rotors used in this enigma machine e.g. "I II III"
# @param - reflector - string of the reflector used in this enigma machine e.g. "B"
# @param - ring_settings - string of the ring settings for the rotors, numbered from 01-26 e.g. "01 02 03"
# @param - initial_positions - string of the starting positions of the rotors, from A-Z e.g. "A A Z"
# @param - plugboard_pairs - list of the plugboard pairs to be used, default is an empty list
def create_enigma_machine(rotors,reflector,ring_settings,initial_positions,plugboard_pairs=[]):
    return EnigmaMachine(rotors, reflector, ring_settings, initial_positions, plugboard_pairs)

# Part 2 : functions to implement to demonstrate code breaking.
# each function should return a list of all the possible answers
# code_one provides an example of how you might declare variables and the return type

def code_one():
    code = "DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ"
    crib = "SECRETS"
    rotors = "Beta Gamma V"
    ring_settings = "04 02 14"
    starting_positions = "M J M"
    plugboard = ["KI", "XN", "FL"]

    possible_reflectors = ["A", "B", "C"]
    possible_answers = []

    for reflector in possible_reflectors:
        machine = EnigmaMachine(rotors, reflector, ring_settings, starting_positions, plugboard)
        encrypted = machine.encode(code)

        if crib in encrypted:
            possible_answers.append(encrypted)

    return possible_answers

def code_two():
    code = "CMFSUPKNCBMUYEQVVDYKLRQZTPUFHSWWAKTUGXMPAMYAFITXIJKMH"
    crib = "UNIVERSITY"
    rotors = "Beta I III"
    ring_settings = "23 02 10"
    plugboard = ["VH", "PT", "ZG", "BJ", "EY", "FS"]
    reflector = "B"

    possible_answers = []

    for first_position in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for second_position in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            for third_position in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                starting_positions = first_position + " " + second_position + " " + third_position
                machine = EnigmaMachine(rotors, reflector, ring_settings, starting_positions, plugboard)
                encrypted = machine.encode(code)

                if crib in encrypted:
                    possible_answers.append(encrypted)

    return possible_answers

def code_three():
    code = "ABSKJAKKMRITTNYURBJFWQGRSGNNYJSDRYLAPQWIAGKJYEPCTAGDCTHLCDRZRFZHKNRSDLNPFPEBVESHPY"
    crib = "THOUSANDS"
    starting_positions = "E M Y"
    plugboard = ["FH", "TS", "BE", "UQ", "KD", "AL"]

    potential_rotors = list(itertools.permutations(["Beta", "Gamma", "II", "IV"], 3))
    potential_reflectors = ["A", "B", "C"]

    potential_answers = []
    
    for first_setting in range (1, 26):
        if not is_even(first_setting):
            continue

        for second_setting in range (1, 26):
            if not is_even(second_setting):
                continue

            for third_setting in range (1, 26):
                if not is_even(third_setting):
                    continue

                ring_settings = get_setting(first_setting) + " " + get_setting(second_setting) + " " + get_setting(third_setting)

                for reflector in potential_reflectors:
                    for rotors in potential_rotors:
                        machine = EnigmaMachine(get_string_form(rotors), reflector, ring_settings, starting_positions, plugboard)
                        encoded = machine.encode(code)

                        if crib in encoded:
                            potential_answers.append(encoded)

    return potential_answers
                

def code_four():
    code = "SDNTVTPHRBNWTLMZTQKZGADDQYPFNHBPNHCQGBGMZPZLUAVGDQVYRBFYYEIXQWVTHXGNW"
    crib = "TUTOR"

    rotors = "V III IV"
    reflector = "A"
    ring_settings = "24 12 10"
    starting_position = "S W U"
    plugboard = ["WP", "RJ", "VF", "HN", "CG", "BS"]

    potential_answers = []

    for first_lead in "DEKLMOQTUXYZ":
        for second_lead in "DEKLMOQTUXYZ":
            if first_lead == second_lead:
                continue

            plugboard.append("A" + first_lead)
            plugboard.append("I" + second_lead)

            machine = EnigmaMachine(rotors, reflector, ring_settings, starting_position, plugboard)
            encoded = machine.encode(code)

            if crib in encoded:
                potential_answers.append(encoded)

            plugboard.remove("A" + first_lead)
            plugboard.remove("I" + second_lead)

    return potential_answers

def code_five():
    return []

if __name__ == "__main__":
    # You can use this section to test your code.  However, remember that your code
    # is automarked in the jupyter notebook so make sure you have followed the
    # instructions in the notebook to make sure your code works and passes the
    # example tests.

    # NOTE - if your code does not work in the notebook when we
    # run the autograded tests you will receive a 0 mark for functionality.
    pass
