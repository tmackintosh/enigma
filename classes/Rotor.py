from helpers.length_assertion import length_assertion
from helpers.lexigraphical_range_assertion import lexigraphical_range_assertion
from helpers.type_assertion import type_assertion


class Rotor:
    def __init__(self, mapping, left_connection = None, right_connection = None, setting = "01", position = "A"):
        """
        Instantiates a Rotor object with the right mapping.

        @param mapping: str, 26 characters, the mapping of each letter in the alphabet in lexigraphical order
        @param left_connection: Rotor object that is located physically to the left of this rotor
        @param right_connection: Rotor object that is location physically to the right of this rotor
        @param setting: numeric string value
        @returns newly instantiated Rotor object
        """
        notch = None

        # Method defense
        type_assertion(left_connection, Rotor)
        type_assertion(right_connection, Rotor)
        type_assertion(setting, str)
        type_assertion(position, str)
        type_assertion(mapping, str)
        length_assertion(setting, 2)

        if len(mapping) != 26:
            # A rotor could have a notch, in which case it is input through the mapping parameter
            mapping = mapping.split(" ")

            length_assertion(mapping, 2)
            length_assertion(mapping[0], 26)
            length_assertion(mapping[1], 1)

            notch = mapping[1]
            mapping = mapping[0]

        for character in mapping.upper():
            lexigraphical_range_assertion(character, "A", "Z")

        self.mapping = mapping.upper()
        self.rotation = int(setting) - 1 + ord(position) - 65

        # Not all rotors have notches
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
        type_assertion(character, str)
        length_assertion(character, 1)
        character = character.upper()
        lexigraphical_range_assertion(character, "A", "Z")

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
        type_assertion(character, str)
        length_assertion(character, 1)
        character = character.upper()
        lexigraphical_range_assertion(character, "A", "Z")

        character = chr(((ord(character) - 65 + self.rotation) % 26) + 65)
        index = (self.mapping.find(character) - self.rotation) % 26

        encoded_character = chr(index + 65)

        if self.right_connection:
            return self.right_connection.encode_left_to_right(encoded_character)
        else:
            return encoded_character