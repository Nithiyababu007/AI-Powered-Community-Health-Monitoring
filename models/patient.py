from models import db


class Patient(db.Model):
    __tablename__ = "patients"

    # -----------------------------
    # Primary Key
    # -----------------------------
    id = db.Column(db.Integer, primary_key=True)

    # -----------------------------
    # Personal Details
    # -----------------------------
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(20), nullable=False)

    mobile = db.Column(db.String(15), nullable=False)
    address = db.Column(db.Text, nullable=False)

    # -----------------------------
    # Health Details
    # -----------------------------
    temperature = db.Column(db.Float, nullable=False)
    blood_pressure = db.Column(db.String(20), nullable=False)
    heart_rate = db.Column(db.Integer, nullable=False)
    oxygen_level = db.Column(db.Integer, nullable=False)

    weight = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)

    symptoms = db.Column(db.Text, nullable=False)
    existing_disease = db.Column(db.Text)

    # -----------------------------
    # AI Analysis
    # -----------------------------
    bmi = db.Column(db.Float)
    score = db.Column(db.Integer)
    risk = db.Column(db.String(50))
    recommendation = db.Column(db.Text)

    # -----------------------------
    # Constructor
    # -----------------------------
    def __init__(
        self,
        name,
        age,
        gender,
        mobile,
        address,
        temperature,
        blood_pressure,
        heart_rate,
        oxygen_level,
        weight,
        height,
        symptoms,
        existing_disease,
        bmi,
        score,
        risk,
        recommendation,
    ):
        self.name = name
        self.age = age
        self.gender = gender

        self.mobile = mobile
        self.address = address

        self.temperature = temperature
        self.blood_pressure = blood_pressure
        self.heart_rate = heart_rate
        self.oxygen_level = oxygen_level

        self.weight = weight
        self.height = height

        self.symptoms = symptoms
        self.existing_disease = existing_disease

        self.bmi = bmi
        self.score = score
        self.risk = risk
        self.recommendation = recommendation

    # -----------------------------
    # String Representation
    # -----------------------------
    def __repr__(self):
        return f"<Patient {self.id} - {self.name}>"