from classes.PlugLead import PlugLead
from classes.Plugboard import Plugboard
from classes.Rotor import Rotor

class EnigmaMachine:
    def __init__(self, rotors, reflector, ring_settings = "01 01 01", initial_positions = "A A A", plugboard_pairs = []):
        ring_settings = ring_settings.split(" ")
        rotors = rotors.split(" ")
        initial_positions = initial_positions.split(" ")

        self.initialize_rotors(rotors, reflector, ring_settings, initial_positions)
        self.plugboard = Plugboard()

        for plug in plugboard_pairs:
            self.plugboard.add(PlugLead(plug))

    def initialize_rotors(self, rotors, reflector, ring_settings, positions):
        self.right_rotor = rotor_from_name(rotors[2], ring_settings[2], positions[2])
        self.middle_rotor = rotor_from_name(rotors[1], ring_settings[1], positions[1])
        self.left_rotor = rotor_from_name(rotors[0], ring_settings[0], positions[0])

        self.reflector = rotor_from_name(reflector)

        self.right_rotor.left_connection = self.middle_rotor

        self.middle_rotor.right_connection = self.right_rotor
        self.middle_rotor.left_connection = self.left_rotor

        self.left_rotor.right_connection = self.middle_rotor
        self.left_rotor.left_connection = self.reflector

        self.reflector.right_connection = self.left_rotor
        self.starting_rotor = self.right_rotor

    def encode(self,text):
        encoded = ""

        for character in text:
            self.starting_rotor.rotate()
            character = self.plugboard.encode(character)
            current_rotor = self.starting_rotor

            # Traverse to the left
            while current_rotor.left_connection is not None:
                character = current_rotor.encode_right_to_left(character)
                current_rotor = current_rotor.left_connection

            # Traverse to the right
            while current_rotor.right_connection is not None:
                character = current_rotor.encode_left_to_right(character)
                current_rotor = current_rotor.right_connection

            # Traverse the final rotor
            character = current_rotor.encode_left_to_right(character)
            encoded = encoded + self.plugboard.encode(character)

        return encoded

# method which returns a Rotor object
# @param - name - name of the Rotor e.g. I or Gamma
def rotor_from_name(name, setting = "01", position = "A"):
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
    rotors = "Beta Gamma V"
    reflector = "B"
    ring_settings = "23 02 10"
    # initial_positions are unknown
    plugboard = ["VH", "PT", "ZG", "BJ", "EY", "FS"]

    code = "CMFSUPKNCBMUYEQVVDYKLRQZTPUFHSWWAKTUGXMPAMYAFITXIJKMH"
    crib = "UNIVERSITY"

    return [code]

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
