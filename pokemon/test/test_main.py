from pokemon.damage import Damage
from pokemon.attack import Attack
from pokemon.loader import Loader


def test_calculating0():
    attacks = [Attack(attacker="psychic", sufferer=["poison", "dark"])]
    damage = Damage(attacks)
    damage.conduct_queries()
    assert damage.rates == [0], "Powinno być  zero"


def test_calculating1():
    attacks = [Attack(attacker="fire", sufferer=["rock"])]
    damage = Damage(attacks)
    damage.conduct_queries()
    assert damage.rates == [0.5], "Powinno być pół"


def test_calculating2():
    attacks = [Attack(attacker="fighting", sufferer=["ice", "rock"])]
    damage = Damage(attacks)
    damage.conduct_queries()
    assert damage.rates == [4], "Powinno być cztery"


def test_loading():
    loader = Loader("pokemon/test/test_file.txt")
    assert loader.attacks == [
        Attack(attacker="fire", sufferer=["grass"])
    ], "źle wczytano"
