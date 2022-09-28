import requests


def pokemon_api(pokemon_type):
    with requests.Session() as s:
        api = f"https://pokeapi.co/api/v2/type/{pokemon_type}"
        response = s.get(api)
        damage = response.json()
        print(damage)

def main():
    pokemon_api("fire")


if __name__ == "__main__":
    main()