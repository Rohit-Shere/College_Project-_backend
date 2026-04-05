ordinal_mappings = {
    'Risk': {'Low': 1, 'Intermediate': 2, 'High': 3},
    'T': {'T1a': 1, 'T1b': 2, 'T2': 3, 'T3a': 4, 'T3b': 5, 'T4a': 6, 'T4b': 7},
    'N': {'N0': 0, 'N1a': 1, 'N1b': 2},
    'M': {'M0': 0, 'M1': 1},
    'Stage': {'I': 1, 'II': 2, 'III': 3, 'IVA': 4, 'IVB': 5},
    'Response': {
        'Excellent': 1,
        'Indeterminate': 2,
        'Biochemical Incomplete': 3,
        'Structural Incomplete': 4
    },
}

binary_mappings = {
    'Gender': {'F': 0, 'M': 1},
    'Smoking': {'No': 0, 'Yes': 1},
    'Hx Smoking': {'No': 0, 'Yes': 1},
    'Hx Radiothreapy': {'No': 0, 'Yes': 1},
    'Focality': {'Uni-Focal': 0, 'Multi-Focal': 1},
}






def encode_thyroid(data: dict):
    encoded = {}

    for key, value in data.items():

        if key in ordinal_mappings:
            encoded[key] = ordinal_mappings[key][value]

        elif key in binary_mappings:
            encoded[key] = binary_mappings[key][value]

        else:
            # For categorical not in mappings → simple label encoding
            encoded[key] = hash(value) % 10  # temp (replace later if needed)

    return encoded