
# Part 1 : Classes and functions you must implement - refer to the jupyter notebook
# You may need to write more classes, which can be done here or in separate files, you choose.

class PlugLead:
    def __init__(self, mapping):
        """
        Instantiates a plug lead object that encodes the two
        characters passed into mapping.

        mapping: str, 2 characters

        Returns new PlugLead object.
        """

        # Method defense
        if type(mapping) != str:
            raise TypeError("Mapping should be a str")
        if len(mapping) != 2:
            raise ValueError("Mapping must have 2 characters.")

        self.mapping = mapping

    def encode(self, character):
        """
        Creates an encoding for character in accordance to
        the plug lead's mapping.

        character: str, 1 character

        Returns a 1 character string representing how the
        input was encoded.
        """

        # Method defense
        if type(character) != str:
            raise TypeError("Character should be a str")
        if len(character) != 1:
            raise ValueError("Character must have a length of 1.")

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

        Returns a Plugboard object.
        """

        self.mappings = {}

    def add(self, lead):
        """
        Adds a PlugLoad object onto the board for encoding.

        lead: PlugBoard object

        Returns nothing.
        """
        # Method defense
        if type(lead) != PlugLead:
            raise TypeError("Lead must be a PlugLead object.")

        for character in lead.mapping:
            self.mappings[character] = lead

    def encode(self, character):
        """
        Encodes a character by the current plugboard leads.

        character: str, 1 character

        Returns a 1 character string representing how the
        input was encoded.
        """
        # Method defense
        if type(character) != str:
            raise TypeError("Character must be a string.")
        if len(character) != 1:
            raise ValueError("Character must have a length of 1.")

        character_lead = self.mappings.get(character)
        if character_lead:
            return character_lead.encode(character)
        else:
            return character

plugboard = Plugboard()

plugboard.add(PlugLead("SZ"))
plugboard.add(PlugLead("GT"))
plugboard.add(PlugLead("DV"))
plugboard.add(PlugLead("KU"))

print(plugboard.encode("K") == "U")
print(plugboard.encode("A") == "A")