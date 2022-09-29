from pydantic import BaseModel
from typing import List


class Attack(BaseModel):
    """
    Class representing single pokemon attack
    """

    attacker: str
    sufferer: List[str]
