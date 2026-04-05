from pydantic import BaseModel, Field
from typing import Literal


class PCOSRequest(BaseModel):
    """
    Request schema for PCOS prediction
    """

    # Numerical
    Age: float = Field(..., ge=10, le=60)
    Weight: float = Field(..., ge=30, le=150)
    Height: float = Field(..., ge=100, le=200)
    Cycle_Length: int = Field(..., ge=0, le=100)

    # Categorical
    Cycle_Type: Literal['Regular', 'Irregular']

    Hair_Growth: Literal['Yes', 'No']
    Skin_Darkening: Literal['Yes', 'No']
    Weight_Gain: Literal['Yes', 'No']
    Fast_Food: Literal['Yes', 'No']
    Pimples: Literal['Yes', 'No']
    Regular_Exercise: Literal['Yes', 'No']


class PCOSResponse(BaseModel):
    prediction: int
    probability: float