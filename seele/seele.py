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

        self.module = Module(120, self.na, self.skill, self.ultimate)
        super().__init__("Seele", self.module)
