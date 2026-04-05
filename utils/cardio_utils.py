import pandas as pd

# ✅ STRICT FEATURE ORDER (from training)
FEATURE_ORDER = [
    'age',
    'gender',
    'ap_hi',
    'cholesterol',
    'gluc',
    'smoke',
    'alco',
    'active',
    'bmi'
]


def calculate_bmi(weight: float, height: float) -> float:
    """
    BMI = weight / (height in meters)^2
    """
    return weight / ((height / 100) ** 2)


def preprocess_input(data: dict) -> pd.DataFrame:
    """
    Convert raw input into model-ready format
    """

    # Create BMI (CRITICAL - must match training)
    bmi = calculate_bmi(data["weight"], data["height"])

    # Build dataframe exactly like training
    df = pd.DataFrame([{
        "age": data["age"],
        "gender": data["gender"],
        "ap_hi": data["ap_hi"],
        "cholesterol": data["cholesterol"],
        "gluc": data["gluc"],
        "smoke": data["smoke"],
        "alco": data["alco"],
        "active": data["active"],
        "bmi": bmi
    }])

    # Enforce strict order
    df = df[FEATURE_ORDER]

    return df