"""
A interface for skill module.
"""


class Skill:
    def __init__(self, sp: int, energy: int, damage: float):
        """
        The constructor of skill module.

        Args:
            sp: Delta of sp. -1 means use a sp; 1 means add a sp, etc.
            energy: The number of energy that will be add after releasing skill.
            damage: The damage of skill.
        """
        self.sp = sp
        self.energy = energy
        self.damage = damage

    def get_sp(self):
        """
        Returns the delta SP.
        """
        return self.sp

    def get_energy(self):
        """
        Returns the added energy after releasing skill.
        """
        return self.energy

    def get_damage(self):
        """
        Returns the damage of the skill.
        """
        return self.damage
