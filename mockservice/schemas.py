from pydantic import BaseModel
from typing import List


class BaggageSelection(BaseModel):
    passengerId: str
    routeId:     str
    baggageIds:  List[str]
    redemption:  bool

class BaggageSelectionsRequest(BaseModel):
    baggageSelections: List[BaggageSelection]


