import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """ Generate a random identifier composed of 15 lowercase letters."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Dataclass representing a student."""
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """Post-initialization method used to generate the student's login
        after the object has been created."""
        self.login = f"{self.name[0]}{self.surname}"
