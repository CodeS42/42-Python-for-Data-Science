from S1E9 import Character

class Baratheon(Character):
    """Class representing a member of House Baratheon."""

    def __init__(self, first_name, is_alive=True):
        """Initialize a Baratheon character with a name and alive status."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"
    
    def die(self):
        """Set the character's alive status to False."""
        self.is_alive = False
    
    def __repr__(self):
        """Return a string representation of the character's attributes."""
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def __str__(self):
        """Return a user-friendly string of the character."""
        return self.__repr__()

class Lannister(Character):
    """Class representing a member of House Lannister."""

    def __init__(self, first_name, is_alive=True):
        """Initialize a Lannister character with a name and alive status."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Create a new Lannister character using the class method."""
        return cls(first_name, is_alive)

    def die(self):
        """Set the character's alive status to False."""
        self.is_alive = False

    def __repr__(self):
        """Return a string representation of the character's attributes."""
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def __str__(self):
        """Return a user-friendly string of the character."""
        return self.__repr__()
