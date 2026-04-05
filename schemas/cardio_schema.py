from pydantic import BaseModel, Field

class CardioRequest(BaseModel):
    """
    Request schema for Cardiovascular Disease prediction
    """

    age: float = Field(..., ge=0, le=120)

    # Raw inputs (used to derive BMI)
    height: float = Field(..., ge=100, le=250)
    weight: float = Field(..., ge=30, le=200)

    ap_hi: int = Field(..., ge=50, le=250)

    # Categorical (already numeric in dataset)
    gender: int = Field(..., ge=1, le=2)
    cholesterol: int = Field(..., ge=1, le=3)
    gluc: int = Field(..., ge=1, le=3)
    smoke: int = Field(..., ge=0, le=1)
    alco: int = Field(..., ge=0, le=1)
    active: int = Field(..., ge=0, le=1)


class CardioResponse(BaseModel):
    prediction: int
    probability: float