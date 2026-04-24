"""
A interface for modules of characters.
"""


class Module:
    def __init__(self, energy: int, na: NA, skill: Skill, ultimate: Ultimate):
        """
        Constructor of Module.

        Args:
            energy: The max energy of the character.
            na: The normal ATK of the character.
            skill: The skill of the character.
            ultimate: The ultimate of the character.
        """
        self.energy = energy
        self.na = na
        self.skill = skill
        self.ultimate = ultimate
