import joblib
import numpy as np
from utils.encoders import encode_thyroid

model = joblib.load("models/Thyroide_lr_model.pkl")
feature_order = ['Age', 'Gender', 'Smoking', 'Hx Smoking', 'Hx Radiothreapy',
       'Physical Examination', 'Adenopathy', 'Pathology', 'Focality', 'Risk',
       'T', 'N', 'M', 'Stage', 'Response']
def predict_thyroid(data: dict):

    encoded = encode_thyroid(data)

    features = features = np.array([[encoded[f] for f in feature_order]])

    prediction = model.predict(features)[0]
    prob = model.predict_proba(features)[0][1]

    return {
        "prediction": int(prediction),
        "risk_score": float(prob)
    }