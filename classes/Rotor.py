from helpers.length_assertion import length_assertion
from helpers.lexigraphical_range_assertion import lexigraphical_range_assertion
from helpers.numerical_assertion import numerical_assertion
from helpers.type_assertion import type_assertion


class Rotor:
    def __init__(self, mapping, left_connection = None, right_connection = None, setting = "01", position = "A"):
        """
        Instantiates a Rotor object with the right mapping.

        @param mapping: str, 26 characters, the mapping of each letter in the alphabet in lexigraphical order
        @param left_connection: Rotor object that is located physically to the left of this rotor
        @param right_connection: Rotor object that is location physically to the right of this rotor
        @param setting: numeric string value representing the ring setting of the rotor
        @param position: character representing the initial rotation of the rotor
        @returns newly instantiated Rotor object
        """
        # Method defense
        type_assertion(left_connection, Rotor, True)
        type_assertion(right_connection, Rotor, True)
        type_assertion(setting, str)
        type_assertion(position, str)
        type_assertion(mapping, str)
        length_assertion(setting, 2)
        numerical_assertion(setting)

        self.notch = -1

        if len(mapping) != 26:
            # A rotor could have a notch, in which case it is input through the mapping parameter
            mapping = mapping.split(" ")

            length_assertion(mapping, 2)
            length_assertion(mapping[0], 26)
            length_assertion(mapping[1], 1)

            self.notch = mapping[1]
            mapping = mapping[0]

        for character in mapping.upper():
            lexigraphical_range_assertion(character, "A", "Z")

        self.mapping = mapping.upper()
        self.position = ord(position) - 65
        self.setting = int(setting) - 1

        # Not all rotors have notches
        if self.notch != -1:
            self.notch = ord(self.notch) - 65

        self.left_connection = left_connection
        self.right_connection = right_connection

        self.ring_setting = None

    def rotate(self):
        """
        Rotates this rotor by 1 position

        @returns Nothing
        """
        if self.left_connection is not None and self.position == self.notch:
            self.left_connection.rotate()

        self.position += 1
        self.position %= 26

    def get_contact(self, character):
        index = ord(character) - 65
        index += self.position
        index -= self.setting
        index %= 26
        return index

    def get_pin(self, character):
        index = ord(character) - 65
        index -= self.position
        index += self.setting
        index %= 26
        return chr(index + 65)

    def encode_right_to_left(self, character):
        """
        Takes an input onto this rotor's pin and pushes the current through
        the circuit and returns this rotor's contact.

        Input should be as if the rotor has no rotation, for example, if
        this rotor has been rotated once and the input is B, the rotor
        will treat the input on its A pin.

        @param character: the character of the input pin
        @returns character: the character of the output contact
        """
        # Method defense
        type_assertion(character, str)
        length_assertion(character, 1)
        character = character.upper()
        lexigraphical_range_assertion(character, "A", "Z")

        index = self.get_contact(character)

        encoded_character = self.mapping[index]
        return self.get_pin(encoded_character)

    def encode_left_to_right(self, character):
        """
        Takes an input onto this rotor's contact and pushes the current through
        the circuit and returns this rotor's pin.

        Input should be as if the rotor has no rotation, for example, if
        this rotor has been rotated once and the input is A, the rotor
        will treat the input on its B contact.

        @param character: the character of the input contact
        @returns character: the character of the output pin
        """
        # Method defense
        type_assertion(character, str)
        length_assertion(character, 1)
        character = character.upper()
        lexigraphical_range_assertion(character, "A", "Z")

        index = self.get_contact(character)
        encoded_character = chr(index + 65)
        pin = self.mapping.index(encoded_character)
        return self.get_pin(chr(pin + 65))