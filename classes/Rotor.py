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
        index = (self.mapping.find(character) - self.rotation) % 26

        encoded_character = chr(index + 65)

        if self.right_connection:
            return self.right_connection.encode_left_to_right(encoded_character)
        else:
            return encoded_character