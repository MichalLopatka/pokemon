from typing import Dict, List
import requests
from pokemon.attack import Attack


class Damage:
    def __init__(self, attacks: List[Attack]):
        self.attacks = attacks

    def conduct_queries(self):
        with requests.Session() as self.session:
            self.rates = []
            for attack in self.attacks:
                damage_relations = self.filter_pokemon(
                    self.query_pokemon(pokemon_type=attack.attacker)
                )
                self.rates.append(
                    self.map_points(attack=attack, damage=damage_relations)
                )
            self.print_rates()

    def query_pokemon(self, pokemon_type: str):
        api = f"https://pokeapi.co/api/v2/type/{pokemon_type}"
        response = self.session.get(api).json()
        return response

    def filter_pokemon(self, response: Dict):
        damage = response["damage_relations"]
        return {k: v for k, v in damage.items() if k.endswith("to")}

    def map_points(self, attack: Attack, damage: Dict):
        effectiveness = 1.0
        for el in attack.sufferer:
            if el in [d["name"] for d in damage["double_damage_to"]]:
                effectiveness *= 2
            elif el in [d["name"] for d in damage["half_damage_to"]]:
                effectiveness *= 0.5
            elif el in [d["name"] for d in damage["no_damage_to"]]:
                effectiveness = 0
                break
        return effectiveness

    def print_rates(self):
        [print(f"{rate}x") for rate in self.rates]
