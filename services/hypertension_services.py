import joblib
import os
from functools import lru_cache

from utils.hypertension_utils import preprocess_input

# Model path
MODEL_PATH = 'models/hypertension_dt_model.pkl'


@lru_cache()
def load_model():
    """
    Load model once and cache it (production optimization)
    """
    return joblib.load(MODEL_PATH)


def predict_hypertension(data: dict):
    """
    Main prediction function
    """

    # Load model
    model = load_model()

    # Preprocess input
    processed_data = preprocess_input(data)

    # Prediction
    prediction = model.predict(processed_data)[0]

    # Probability (for Decision Tree, supported)
    probability = model.predict_proba(processed_data)[0][1]

    return {
        "prediction": int(prediction),
        "probability": float(probability)
    }