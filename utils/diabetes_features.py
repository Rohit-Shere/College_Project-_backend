import numpy as np

def create_diabetes_features(data: dict):
    
    bmi = data["BMI"]
    glucose = data["Glucose"]
    insulin = data["Insulin"]
    age = data["Age"]

    # 1. BMI Category
    if bmi < 18.5:
        bmi_cat = 1
    elif bmi < 24.9:
        bmi_cat = 2
    elif bmi < 29.9:
        bmi_cat = 3
    else:
        bmi_cat = 4

    # 2. Glucose-Insulin Ratio
    gir = glucose / (insulin + 1)

    # 3. Age * Glucose
    age_glucose = age * glucose

    return {
        **data,
        "BMI_Cat": bmi_cat,
        "Glucose_Insulin_Ratio": gir,
        "Age_Glucose": age_glucose
    }