from helpers.length_assertion import length_assertion
from helpers.lexigraphical_range_assertion import lexigraphical_range_assertion
from helpers.type_assertion import type_assertion


class PlugLead:
    def __init__(self, mapping):
        """
        Instantiates a plug lead object that encodes the two
        characters passed into mapping.

        @param mapping: str, 2 characters
        @returns new PlugLead object.
        """

        # Method defense
        type_assertion(mapping, str)
        mapping = mapping.upper()
        for character in mapping:
            lexigraphical_range_assertion(character, "A", "Z")
        length_assertion(mapping, 2)
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
        type_assertion(character, str)
        character = character.upper()
        length_assertion(character, 1)
        lexigraphical_range_assertion(character, "A", "Z")

        if character in self.mapping:
            location = self.mapping.index(character)
            
            # Return the otherside of the physical wire
            if location == 1:
                return self.mapping[0]
            else:
                return self.mapping[1]

        return character