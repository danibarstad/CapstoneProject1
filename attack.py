from dataclasses import dataclass


# class a character's attack
@dataclass
class Attack:
    name: str
    damage: int