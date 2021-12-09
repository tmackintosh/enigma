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