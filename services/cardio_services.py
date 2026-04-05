import os
import joblib
from functools import lru_cache

from utils.cardio_utils import preprocess_input

MODEL_PATH = 'models/cardio_rf_model.pkl'
@lru_cache()
def load_model():
    """
    Load model once (cached)
    """
    return joblib.load(MODEL_PATH)


def predict_cardio(data: dict):
    """
    Prediction pipeline
    """

    model = load_model()

    # Preprocess
    processed_data = preprocess_input(data)

    # Predict
    prediction = model.predict(processed_data)[0]

    # Probability
    probability = model.predict_proba(processed_data)[0][1]

    return {
        "prediction": int(prediction),
        "probability": float(probability)
    }