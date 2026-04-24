"""
A interface for characters.
"""

from module import Module


class Character:
    def __init__(self, name: str, module: Module):
        """
        Constructor of Character.

        Args:
            name: The name of character.
            module: The module of character (see Module class).
        """
        self.name = name
        self.module = module
        self.energy = module.get_init_energy()

    def get_energy(self):
        """
        Returns the number of current energy.
        """
        return self.energy

    def get_module(self):
        """
        Returns the module of the character.
        """
        return self.module

    def change_energy(self, energy: int):
        self.energy += energy
        if self.energy > self.module.max_energy:
            self.energy = self.module.max_energy

    def take_action(self, action: str) -> tuple[int, float]:
        """
        Take the input action.
        Args:
            action:
                "NA" or "A" if you want to release normal ATK.
                "Skill" or "E" if you want to release skill.
                "Ultimate" or "Q" if you want to release ultimate.
                If you want to release ultimate but the energy is not fulled,
                all return values will be 0 and a message will be sent.
                If action is not matched, KeyError will be released.
        Returns:
            [delta_sp, damage]

            delta_sp: The delta sp after this action.
            damage: The damage of this action.
        """
        match action.strip():
            case "NA" | "A":
                delta_sp = self.module.get_na().get_sp()
                damage = self.module.get_na().get_damage()
                self.change_energy(self.module.get_na().get_energy())
            case "Skill" | "E":
                delta_sp = self.module.get_skill().get_sp()
                damage = self.module.get_skill().get_damage()
                self.change_energy(self.module.get_skill().get_energy())
            case "Ultimate" | "Q":
                delta_sp = 0
                if self.energy != self.module.get_max_energy():
                    damage = 0
                else:
                    self.change_energy(
                        self.module.get_ultimate().energy - self.module.max_energy
                    )
                    damage = self.module.get_ultimate().get_damage()
            case _:
                raise KeyError
        return delta_sp, damage
