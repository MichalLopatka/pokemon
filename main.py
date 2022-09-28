import requests

def query_pokemon(session, pokemon_type):
    api = f"https://pokeapi.co/api/v2/type/{pokemon_type}"
    response = session.get(api)
    damage = response.json()
    print(damage)

def conduct_queries(attacks):
    with requests.Session() as session:
        for attack in attacks:
            query_pokemon(session, attack)

def main():
    conduct_queries(attacks=["fire", "normal", "water"])


if __name__ == "__main__":
    main()