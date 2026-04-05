from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas.thyroid_schema import ThyroidInput
from services.thyroid_services import predict_thyroid
from schemas.diabetes_schema import DiabetesInput
from services.diabetes_services import predict_diabetes
from schemas.hypertension_schema import HypertensionRequest, HypertensionResponse
from services.hypertension_services import predict_hypertension
from schemas.cardio_schema import CardioRequest, CardioResponse
from services.cardio_services import predict_cardio
from schemas.pcos_schema import PCOSRequest, PCOSResponse
from services.pcos_service import predict_pcos

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],  # Frontend URLs
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Health AI API Running 🚀"}

@app.post("/predict/thyroid")
def thyroid_prediction(input_data: ThyroidInput):
    result = predict_thyroid(input_data.dict())
    return result

@app.post("/predict/diabetes")
def diabetes_prediction(input_data: DiabetesInput):
    result = predict_diabetes(input_data.dict())
    return result

@app.post("/predict/hypertension", response_model=HypertensionResponse)
def predict_hypertension_route(request: HypertensionRequest):
    """
    Hypertension Prediction Endpoint
    """

    result = predict_hypertension(request.dict())

    return result

@app.post("/predict/cardio", response_model=CardioResponse)
def predict_cardio_route(request: CardioRequest):
    """
    Cardiovascular Disease Prediction
    """

    result = predict_cardio(request.dict())

    return result


@app.post("/predict/pcos", response_model=PCOSResponse)
def predict_pcos_route(request: PCOSRequest):
    """
    PCOS Prediction Endpoint
    """

    result = predict_pcos(request.dict())

    return result