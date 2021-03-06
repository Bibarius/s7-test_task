from pydantic import BaseModel
from typing import List


class SkiRequest(BaseModel):
    reservationId: str
    passengerName: str