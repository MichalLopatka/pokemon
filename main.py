import requests


def map_points(attack, damage):
    effectiveness = 1
    for el in attack["to"]:
        if el in [d['name'] for d in damage["double_damage_to"]]:
            effectiveness *=2
        elif el in [d['name'] for d in damage["half_damage_to"]]:
            effectiveness *=0.5
        elif el in [d['name'] for d in damage["no_damage_to"]]:
            effectiveness = 0
            break
    return effectiveness
        
def query_pokemon(session, pokemon_type):
    api = f"https://pokeapi.co/api/v2/type/{pokemon_type}"
    response = session.get(api)
    damage = response.json()["damage_relations"]
    damage_to = {k: v for k, v in damage.items() if k.endswith('to')}
    return damage_to

def conduct_queries(attacks):
    with requests.Session() as session:
        for attack in attacks:
            damage_relations = query_pokemon(session, attack["from"])
            points = map_points(attack, damage_relations)
            print(f"{points}x")


def get_input():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    print(lines)
    return lines

def process_input(lines):
    processed_lines = []
    for line in lines:
        attacker, receivers = line.split('->')
        receivers = receivers.split()
        processed_lines.append({"from": attacker.strip(), "to": receivers})
    print(processed_lines)
    return processed_lines

def main():
    # conduct_queries(attacks=[{"from": "fire","to": ["grass"]}, {"from":"fighting", "to": ["rock", "ice"]}, {"from": "psychic", "to": ["poison", "dark"]}])
    lines = get_input()
    attacks = process_input(lines)
    conduct_queries(attacks)


if __name__ == "__main__":
    main()