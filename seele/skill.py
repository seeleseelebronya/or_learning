"""
A interface for skill module.
"""


class Skill:
    def __init__(self, sp: int, energy: int, damage: float):
        """
        The constructor of skill module.

        Args:
            sp: Cost of sp. 1 means use a sp; -1 means add a sp, etc.
            energy: The number of energy that will be add after skill.
            damage: The damage of skill.
        """
        self.sp = sp
        self.energy = energy
        self.damage = damage
