"""
The character seele.
"""

from character import Character
from module import Module
from normal_attack import NA
from skill import Skill
from ultimate import Ultimate


class Seele(Character):
    def __init__(self):
        self.na = NA(1, 20, 50)
        self.skill = Skill(-1, 30, 100)
        self.ultimate = Ultimate(5, 300)

        self.module = Module(120, 50, self.na, self.skill, self.ultimate)
        self.energy = self.module.get_init_energy()
        super().__init__("Seele", self.module)


def main():
    """
    Find the max damage after 5 actions.
    """
    INIT_SP = 3
    TOTAL_ACTIONS = 5

    seele = Seele()

    sp = INIT_SP
    total_damage = 0
    for _ in range(TOTAL_ACTIONS):
        if sp > 0:
            delta_sp, damage = seele.take_action("E")
        else:
            delta_sp, damage = seele.take_action("A")
        sp += delta_sp
        total_damage += damage

        if seele.get_energy() == seele.module.get_max_energy():
            delta_sp, damage = seele.take_action("Q")

    print(f"Total damage: {total_damage}")


if __name__ == "__name__":
    main()
