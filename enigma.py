
# Part 1 : Classes and functions you must implement - refer to the jupyter notebook
# You may need to write more classes, which can be done here or in separate files, you choose.

class PlugLead:
    def __init__(self, mapping):
        """
        Instantiates a plug lead object that encodes the two
        characters passed into mapping.

        @param mapping: str, 2 characters
        @returns new PlugLead object.
        """

        # Method defense
        if type(mapping) != str:
            raise TypeError("Mapping should be a str")

        mapping = mapping.upper()

        for character in mapping:
            if ord("A") > ord(character) or ord(character) > ord("Z"):
                raise ValueError("Character must be between A-Z")
        if len(mapping) != 2:
            raise ValueError("Mapping must have 2 characters.")
        if mapping[0:1] == mapping[1:2]:
            raise ValueError("You cannot connect a character to itself.")

        self.mapping = mapping

    def encode(self, character):
        """
        Creates an encoding for character in accordance to
        the plug lead's mapping.

        @param character: str, 1 character
        @returns a 1 character string representing how the input was encoded.
        """

        # Method defense
        if type(character) != str:
            raise TypeError("Character should be a str")

        character = character.upper()

        if len(character) != 1:
            raise ValueError("Character must have a length of 1.")
        if ord("A") > ord(character) or ord(character) > ord("Z"):
            raise ValueError("Character must be between A-Z")

        if character in self.mapping:
            location = self.mapping.index(character)
            
            if location == 1:
                return self.mapping[0]
            else:
                return self.mapping[1]

        return character

class Plugboard:
    def __init__(self):
        """
        Instantiates a Plugboard object.

        @returns a Plugboard object.
        """

        self.mappings = {}

    def add(self, lead):
        """
        Adds a PlugLoad object onto the board for encoding.

        @param lead: PlugBoard object
        @returns nothing.
        """
        # Method defense
        if type(lead) != PlugLead:
            raise TypeError("Lead must be a PlugLead object.")

        for character in lead.mapping:
            self.mappings[character] = lead

    def encode(self, character):
        """
        Encodes a character by the current plugboard leads.

        @param character: str, 1 character

        @returns a 1 character string representing how the input was encoded.
        """
        # Method defense
        if type(character) != str:
            raise TypeError("Character must be a string.")

        character = character.upper()

        if len(character) != 1:
            raise ValueError("Character must have a length of 1.")
        if ord("A") > ord(character) or ord(character) > ord("Z"):
            raise ValueError("Character must be between A-Z")

        character_lead = self.mappings.get(character)
        if character_lead:
            return character_lead.encode(character)
        else:
            return character.upper()


class Rotor:
    def __init__(self, mapping, left_connection = None, right_connection = None, setting = "01", position = "A"):
        """
        Instantiates a Rotor object with the right mapping.

        @param mapping: str, 26 characters, the mapping of each letter in the alphabet in lexigraphical order
        @returns newly instantiated Rotor object
        """
        notch = None

        # Method defense
        if type(mapping) != str:
            raise TypeError("Mapping must be a string")
        if len(mapping) != 26:
            mapping = mapping.split(" ")

            if len(mapping) != 2:
                raise ValueError("Mapping must be 26 characters long")

            notch = mapping[1]
            mapping = mapping[0]

        for character in mapping.upper():
            if ord("A") > ord(character) or ord(character) > ord("Z"):
                raise ValueError("Mapping can only contain A-Z characters")

        self.mapping = mapping.upper()
        self.rotation = int(setting) - 1 + ord(position) - 65

        if notch is not None:
            self.notch = ord(notch) - 65

        self.left_connection = left_connection
        self.right_connection = right_connection

        self.ring_setting = None

    def rotate(self):
        if self.left_connection is not None and self.rotation == self.notch:
            self.left_connection.rotate()

        self.rotation += 1
        self.rotation %= 26

    def encode_right_to_left(self, character):
        # Method defense
        if type(character) != str:
            raise TypeError("Character must be a string")
        if len(character) != 1:
            raise ValueError("Character must be a single character")
        
        character = character.upper()

        if ord("A") > ord(character) or ord(character) > ord("Z"):
            raise ValueError("Character must be between A-Z")

        index = ord(character) - 65 + self.rotation

        if self.right_connection:
            index -= self.right_connection.rotation

        index %= 26

        encoded_character = self.mapping[index]

        if self.left_connection:
            return self.left_connection.encode_right_to_left(encoded_character)
        elif self.right_connection:
            # In case this rotor is a reflector
            return self.right_connection.encode_left_to_right(encoded_character)
        else:
            return encoded_character

    def encode_left_to_right(self, character):
        # Method defense
        if type(character) != str:
            raise TypeError("Character must be a string")
        if len(character) != 1:
            raise ValueError("Character must be a single character")
        
        character = character.upper()

        if ord("A") > ord(character) or ord(character) > ord("Z"):
            raise ValueError("Character must be between A-Z")

        character = chr(((ord(character) - 65 + self.rotation) % 26) + 65)
        index = self.mapping.find(character)

        encoded_character = chr(index + 65 - self.rotation)

        if self.right_connection:
            return self.right_connection.encode_left_to_right(encoded_character)
        else:
            return encoded_character

class EnigmaMachine:
    def __init__(self, rotors, reflector, ring_settings = "01 01 01", initial_positions = "A A A", plugboard_pairs = []):
        ring_settings = ring_settings.split(" ")
        rotors = rotors.split(" ")
        initial_positions = initial_positions.split(" ")

        self.initialize_rotors(rotors, reflector, ring_settings, initial_positions)
        self.plugboard = Plugboard()

        for plug in plugboard_pairs:
            self.plugboard.add(plug)

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
            plugboard_character = self.plugboard.encode(character)
            character = self.starting_rotor.encode_right_to_left(plugboard_character)

            encoded = encoded + character

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
