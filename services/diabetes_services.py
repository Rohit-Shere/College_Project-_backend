import joblib
import numpy as np
from utils.diabetes_features import create_diabetes_features
from utils.feature_order import DIABETES_FEATURE_ORDER

model = joblib.load("models/diabetes_dt_model.pkl")

def predict_diabetes(data: dict):

    # Step 1: Feature Engineering
    enriched = create_diabetes_features(data)

    # Step 2: Arrange features
    features = np.array([[enriched[f] for f in DIABETES_FEATURE_ORDER]])

    # Step 3: Prediction
    prediction = model.predict(features)[0]
    prob = model.predict_proba(features)[0][1]

    return {
        "prediction": int(prediction),
        "risk_score": float(prob),
        "derived_features": {
            "BMI_Cat": enriched["BMI_Cat"],
            "Glucose_Insulin_Ratio": enriched["Glucose_Insulin_Ratio"],
            "Age_Glucose": enriched["Age_Glucose"]
        }
    }