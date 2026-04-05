import os
import joblib
from functools import lru_cache

from utils.pcos_utils import preprocess_input

MODEL_PATH ="models/pcos_rf_model.pkl"


@lru_cache()
def load_model():
    """
    Load model once (cached)
    """
    model = joblib.load(MODEL_PATH)
    print("MODEL FEATURES:", model.feature_names_in_)
    return model


def predict_pcos(data: dict):
    """
    Prediction pipeline
    """

    model = load_model()

    processed_data = preprocess_input(data)

    prediction = model.predict(processed_data)[0]
    probability = model.predict_proba(processed_data)[0][1]

    return {
        "prediction": int(prediction),
        "probability": float(probability)
    }