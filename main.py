from typing import Dict, List
import requests
from pydantic import BaseModel
from pokemon.loader import Loader
from pokemon.damage import Damage


def main():
    # conduct_queries(attacks=[{"from": "fire","to": ["grass"]}, {"from":"fighting", "to": ["rock", "ice"]}, {"from": "psychic", "to": ["poison", "dark"]}])
    attacks = Loader().attacks
    Damage(attacks=attacks).conduct_queries()


if __name__ == "__main__":
    main()
