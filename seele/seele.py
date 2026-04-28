"""
The character seele.
"""

from functools import lru_cache

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
            total_damage += damage

    print(f"Total damage: {total_damage}")

    seele1 = Seele()
    max_damage = solve(seele1, TOTAL_ACTIONS, seele1.get_energy(), INIT_SP)
    print(f"Max damage: {max_damage}")


@lru_cache(None)
def solve(c: Character, n: int, e: int, sp: int) -> int:
    """
    Use DP to find the max damage.
    Args:
        c: The Character.
        n: Left actions.
        e: Current energy.
        sp: Current SP.
    Returns: The max damage.
    """
    if n == 0:
        return 0

    ultimate = c.get_module().get_ultimate()
    if e >= c.get_module().get_max_energy():
        res_ultimate = ultimate.get_damage() + solve(c, n, ultimate.get_energe(), sp)
    else:
        res_ultimate = -1

    na = c.get_module().get_na()
    res_na = na.get_damage() + solve(c, n - 1, e + na.get_energy(), sp + na.get_sp())

    skill = c.get_module().get_skill()
    if sp > 0:
        res_skill = skill.get_damage() + solve(
            c, n - 1, e + skill.get_energy(), sp + skill.get_sp()
        )
    else:
        res_skill = -1

    return round(max(res_na, res_skill, res_ultimate))


if __name__ == "__main__":
    main()
