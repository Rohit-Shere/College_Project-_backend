import pandas as pd

# Encoding mappings
bp_mapping = {
    'Normal': 0,
    'Prehypertension': 1,
    'Hypertension': 2
}

sm_mapping = {
    'Non-Smoker': 0,
    'Smoker': 1
}

fm_mapping = {
    'No': 0,
    'Yes': 1
}

# Strict feature order (CRITICAL)
FEATURE_ORDER = [
    'Age',
    'Salt_Intake',
    'Stress_Score',
    'Sleep_Duration',
    'BMI',
    'Smoking_Status',
    'Family_History',
    'BP_History'
]


def preprocess_input(data: dict) -> pd.DataFrame:
    """
    Converts raw input into model-ready DataFrame
    """

    # Convert to DataFrame
    df = pd.DataFrame([data])

    # Apply encoding
    df['Smoking_Status'] = df['Smoking_Status'].map(sm_mapping)
    df['Family_History'] = df['Family_History'].map(fm_mapping)
    df['BP_History'] = df['BP_History'].map(bp_mapping)

    # Enforce feature order STRICTLY
    df = df[FEATURE_ORDER]

    return df