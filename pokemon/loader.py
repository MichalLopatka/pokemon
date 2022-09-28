from pokemon.attack import Attack


class Loader:
    def __init__(self):
        self.lines = self.get_input()
        self.attacks = self.process_input()

    def get_input(self):
        lines = []
        while True:
            line = input()
            if line:
                lines.append(line)
            else:
                break
        return lines

    def process_input(self):
        processed_lines = []
        for line in self.lines:
            attacker, receivers = line.split("->")
            receivers = receivers.split()
            processed_lines.append(
                Attack(attacker=attacker.strip(), sufferer=receivers)
            )
        return processed_lines
