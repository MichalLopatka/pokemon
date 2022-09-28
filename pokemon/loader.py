from pokemon.attack import Attack


class Loader:
    def __init__(self, filename: str):
        self.lines = self.get_input(filename=filename)
        self.attacks = self.process_input()


    def get_input(self, filename:str):
        with open(filename) as f:
            return f.readlines()


    def process_input(self):
        processed_lines = []
        for line in self.lines:
            attacker, receivers = line.split("->")
            receivers = receivers.split()
            processed_lines.append(
                Attack(attacker=attacker.strip(), sufferer=receivers)
            )
        return processed_lines
