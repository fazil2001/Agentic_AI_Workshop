def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)
