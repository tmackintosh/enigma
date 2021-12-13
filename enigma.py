from classes.PlugLead import PlugLead
from classes.Plugboard import Plugboard
from classes.Rotor import Rotor
from helpers.length_assertion import length_assertion
from helpers.lexigraphical_range_assertion import lexigraphical_range_assertion
from helpers.numerical_assertion import numerical_assertion

from helpers.type_assertion import type_assertion

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

        if len(ring_settings) != 3 or len(rotors) != 3 or len(positions) != 3:
            raise ValueError("You must provide the same number of arguments for each rotor, setting and position.")

        # Instantiate rotors
        self.right_rotor = rotor_from_name(rotors[2], ring_settings[2], positions[2])
        self.middle_rotor = rotor_from_name(rotors[1], ring_settings[1], positions[1])
        self.left_rotor = rotor_from_name(rotors[0], ring_settings[0], positions[0])

        self.reflector = rotor_from_name(reflector)

        # Set relative rotor positions
        self.right_rotor.left_connection = self.middle_rotor

        self.middle_rotor.right_connection = self.right_rotor
        self.middle_rotor.left_connection = self.left_rotor

        self.left_rotor.right_connection = self.middle_rotor
        self.left_rotor.left_connection = self.reflector

        self.reflector.right_connection = self.left_rotor
        self.starting_rotor = self.right_rotor

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
            # print("Adding", self.plugboard.encode(character))
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
    return []

def code_three():
    return []

def code_four():
    return []

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
