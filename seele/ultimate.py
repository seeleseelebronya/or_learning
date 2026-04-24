"""
A interface for ultimate module.
"""


class Ultimate:
    def __init__(self, energy: int, damage: float):
        """
        The constructor of ultimate module.

        Args:
            energy: The number of energy that will be added after releasing ultimate.
            After releasing ultimate, full energy will be costed. So this
            value is the total energy after releasing ultimate.

            damage: The damage of skill.
        """
        self.energy = energy
        self.damage = damage

    def get_energe(self):
        """
        Returns the number of energy that will be added after releasing ultimate.
        """
        return self.energy

    def get_damage(self):
        """
        Returns the damage of the ultimaate
        """
        return self.damage
