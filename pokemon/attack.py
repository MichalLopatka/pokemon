from pydantic import BaseModel
from typing import List


class Attack(BaseModel):
    attacker: str
    sufferer: List[str]
