from dataclasses import dataclass
import attack as Attack


# class for creating a character
@dataclass
class Character:
    name: str
    hp: int
    atk: Attack
    taunt: str      # flavor text that a character says when they taunt
    defeat: str     # flavor text that a character says when they are defeated