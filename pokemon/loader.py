from pokemon.attack import Attack
from typing import List


class Loader:
    def __init__(self, filename: str):
        self.lines = self.get_input(filename=filename)
        self.attacks = self.process_input()

    def get_input(self, filename: str) -> List:
        """
        Load input file with pokemon attacks
        """
        with open(filename) as f:
            return f.readlines()

    def process_input(self) -> List:
        """
        Process input file to list of pokemon attacks
        """
        processed_lines = []
        for line in self.lines:
            attacker, receivers = line.split("->")
            receivers = receivers.split()
            processed_lines.append(
                Attack(attacker=attacker.strip(), sufferer=receivers)
            )
        return processed_lines
