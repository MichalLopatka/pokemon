from pokemon.loader import Loader
from pokemon.damage import Damage


def main():
    attacks = Loader("file.txt").attacks
    Damage(attacks=attacks).conduct_queries()


if __name__ == "__main__":
    main()
