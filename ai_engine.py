def analyze_patient(age, temperature, oxygen, heart_rate, bmi_weight, bmi_height):
    """
    Analyze patient health and return:
    BMI, Health Score, Risk Level, Recommendation
    """

    # -----------------------------
    # BMI Calculation
    # -----------------------------
    height_m = bmi_height / 100

    if height_m <= 0:
        bmi = 0
    else:
        bmi = round(bmi_weight / (height_m * height_m), 2)

    # -----------------------------
    # Initial Health Score
    # -----------------------------
    score = 100

    # -----------------------------
    # BMI Check
    # -----------------------------
    if bmi < 18.5:
        score -= 10
    elif bmi >= 30:
        score -= 20

    # -----------------------------
    # Temperature Check
    # -----------------------------
    if temperature > 38:
        score -= 15

    # -----------------------------
    # Oxygen Level Check
    # -----------------------------
    if oxygen < 95:
        score -= 25

    # -----------------------------
    # Heart Rate Check
    # -----------------------------
    if heart_rate > 100 or heart_rate < 60:
        score -= 15

    # -----------------------------
    # Age Check
    # -----------------------------
    if age >= 60:
        score -= 10

    # Prevent negative score
    if score < 0:
        score = 0

    # -----------------------------
    # Risk Level
    # -----------------------------
    if score >= 80:
        risk = "Low Risk"
        recommendation = (
            "Healthy. Continue regular exercise, balanced diet, "
            "and routine health checkups."
        )

    elif score >= 50:
        risk = "Medium Risk"
        recommendation = (
            "Monitor your health regularly. Maintain a healthy lifestyle "
            "and consult a doctor if symptoms continue."
        )

    else:
        risk = "High Risk"
        recommendation = (
            "Immediate medical attention is recommended. "
            "Please consult a healthcare professional as soon as possible."
        )

    return bmi, score, risk, recommendation