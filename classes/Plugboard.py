from classes.PlugLead import PlugLead
from helpers.length_assertion import length_assertion
from helpers.lexigraphical_range_assertion import lexigraphical_range_assertion
from helpers.type_assertion import type_assertion
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
        type_assertion(lead, PlugLead)

        for character in lead.mapping:
            self.mappings[character] = lead

    def encode(self, character):
        """
        Encodes a character by the current plugboard leads.

        @param character: str, 1 character

        @returns a 1 character string representing how the input was encoded.
        """
        # Method defense
        type_assertion(character, str)
        character = character.upper()
        length_assertion(character, 1)
        lexigraphical_range_assertion(character, "A", "Z")

        character_lead = self.mappings.get(character)
        if character_lead:
            return character_lead.encode(character)
        else:
            return character.upper()