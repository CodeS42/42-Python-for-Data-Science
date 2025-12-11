from abc import ABC, abstractmethod
# TypeError: Can't instantiate abstract class Character with abstract method <- TRY EXCEPT?


class Character(ABC):
    """Abstract base class representing a generic character."""
    
    def __init__(self, first_name, is_alive=True):
        """Initialize a character with a first name and alive status."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Change the character's status to dead."""
        pass

class Stark(Character):
    """Class representing a member of House Stark."""
    
    def __init__(self, first_name, is_alive=True):
        """Initialize a Stark character with a name and alive status."""
        super().__init__(first_name, is_alive)
    
    def die(self):
        """Set the character's alive status to False."""
        self.is_alive = False