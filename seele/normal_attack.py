"""
A interface of NA module.
"""


class NA:
    def __init__(self, sp: int, energy: int, damage: float):
        """
        The constructor of NA module.

        Args:
            sp: Cost of sp. 1 means use a sp; -1 means add a sp, etc.
            energy: The number of energy that will be add after NA.
            damage: The damage of NA.
        """
        self.sp = sp
        self.energy = energy
        self.damage = damage
