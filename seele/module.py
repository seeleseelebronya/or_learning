"""
A interface for modules of characters.
"""

from normal_attack import NA
from skill import Skill
from ultimate import Ultimate


class Module:
    def __init__(
        self,
        max_energy: int,
        init_energy: int,
        na: NA,
        skill: Skill,
        ultimate: Ultimate,
    ):
        """
        Constructor of Module.

        Args:
            max_energy: The max energy of the character.
            init_energy: The initial energy of the character.
            na: The normal ATK of the character.
            skill: The skill of the character.
            ultimate: The ultimate of the character.
        """
        self.max_energy = max_energy
        self.init_energy = init_energy
        self.na = na
        self.skill = skill
        self.ultimate = ultimate

    def get_max_energy(self):
        """
        Returns the max energy of the character.
        """
        return self.max_energy

    def get_init_energy(self):
        """
        Returns the initial energy of the character.
        """
        return self.init_energy

    def get_na(self):
        """
        Returns the NA of the character.
        """
        return self.na

    def get_skill(self):
        """
        Returns the skill of the character.
        """
        return self.skill

    def get_ultimate(self):
        return self.ultimate
