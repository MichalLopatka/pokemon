from pokemon.loader import Loader
from pokemon.damage import Damage


def main():
    # conduct_queries(attacks=[{"from": "fire","to": ["grass"]}, {"from":"fighting", "to": ["rock", "ice"]}, {"from": "psychic", "to": ["poison", "dark"]}])
    attacks = Loader("file.txt").attacks
    Damage(attacks=attacks).conduct_queries()


if __name__ == "__main__":
    main()
