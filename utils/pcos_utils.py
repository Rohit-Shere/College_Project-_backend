import pandas as pd

# Encodings
yes_no_mapping = {'No': 0, 'Yes': 1}
cycle_mapping = {'Regular': 0, 'Irregular': 1}

# ✅ EXACT feature order from model
FEATURE_ORDER = [
    'Follicle No. (R)',
    'Follicle No. (L)',
    'Skin darkening (Y/N)',
    'hair growth(Y/N)',
    'Weight gain(Y/N)',
    'AMH(ng/mL)',
    'Cycle(R/I)',
    'Cycle length(days)',
    'Fast food (Y/N)',
    'LH(mIU/mL)',
    'FSH/LH',
    'Age (yrs)',
    'BMI',
    'Hip(inch)'
]


def calculate_bmi(weight, height):
    return weight / ((height / 100) ** 2)


def preprocess_input(data: dict) -> pd.DataFrame:
    """
    FAST FIX:
    - Map existing inputs
    - Fill missing model features with defaults
    """

    bmi = calculate_bmi(data["Weight"], data["Height"])

    # ⚠️ Default placeholders (since API doesn't provide these)
    df = pd.DataFrame([{
        # Missing clinical features → default safe values
        'Follicle No. (R)': 5,
        'Follicle No. (L)': 5,
        'AMH(ng/mL)': 3.0,
        'LH(mIU/mL)': 5.0,
        'FSH/LH': 1.5,
        'Hip(inch)': 36,

        # Mapped features
        'Skin darkening (Y/N)': yes_no_mapping[data['Skin_Darkening']],
        'hair growth(Y/N)': yes_no_mapping[data['Hair_Growth']],  # ⚠️ lowercase 'hair'
        'Weight gain(Y/N)': yes_no_mapping[data['Weight_Gain']],
        'Cycle(R/I)': cycle_mapping[data['Cycle_Type']],
        'Cycle length(days)': data['Cycle_Length'],
        'Fast food (Y/N)': yes_no_mapping[data['Fast_Food']],
        'Age (yrs)': data['Age'],
        'BMI': bmi
    }])

    # Enforce exact order
    df = df[FEATURE_ORDER]

    return df