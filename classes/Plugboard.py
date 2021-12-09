from classes.PlugLead import PlugLead

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