# Initial energy is 0
ACTIONS = ("A", "E", "Q")

# NA damage is 50
A_DAMAGE = 50
A_ENERGY = 20

# Skill damage is 100
E_DAMAGE = 100
E_ENERGY = 30

MAX_ENERGY = 120
# Ultimate damage is 300
Q_DAMAGE = 300

# Initial skill points is 3
# 5 turns for action
sp = 3
actions_left = 5
total_damage = 0
energy = 50


def turn(action):
    match action:
        case "A":
            total_damage += A_DAMAGE
            sp += 1
            actions_left -= 1
        case "E":
            total_damage += E_DAMAGE
            sp -= 1
            actions_left -= 1
        case "Q":
            total_damage += Q_DAMAGE
            energy = 5
