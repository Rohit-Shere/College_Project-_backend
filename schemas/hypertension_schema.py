from pydantic import BaseModel, Field
from typing import Literal

class HypertensionRequest(BaseModel):
    """
    Request schema for Hypertension prediction
    """

    # Numerical Features
    Age: int = Field(..., ge=0, le=120)
    Salt_Intake: float = Field(..., ge=0)
    Stress_Score: float = Field(..., ge=0, le=10)
    Sleep_Duration: float = Field(..., ge=0, le=24)
    BMI: float = Field(..., ge=0)

    # Categorical Features
    Smoking_Status: Literal['Non-Smoker', 'Smoker']
    Family_History: Literal['No', 'Yes']
    BP_History: Literal['Normal', 'Prehypertension', 'Hypertension']


class HypertensionResponse(BaseModel):
    """
    Standardized response schema
    """
    prediction: int
    probability: float