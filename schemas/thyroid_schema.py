from pydantic import BaseModel

class ThyroidInput(BaseModel):
    Age: int

    Response: str
    Risk: str
    Adenopathy: str
    N: str
    T: str
    Stage: str
    Focality: str
    M: str
    Smoking: str
    Gender: str
    Pathology: str
    Physical_Examination: str
    Hx_Radiothreapy: str
    Hx_Smoking: str