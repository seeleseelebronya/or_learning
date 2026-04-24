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
