from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config

from models import db
from models.user import User
from models.patient import Patient

from ai_engine import analyze_patient

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# -----------------------------
# Create Database & Default Users
# -----------------------------
with app.app_context():

    db.create_all()

    if User.query.count() == 0:

        admin = User(
            username="admin",
            password="admin123",
            role="Admin"
        )

        doctor = User(
            username="doctor",
            password="doctor123",
            role="Doctor"
        )

        nurse = User(
            username="nurse",
            password="nurse123",
            role="Nurse"
        )

        db.session.add(admin)
        db.session.add(doctor)
        db.session.add(nurse)

        db.session.commit()

        print("Default Users Created Successfully")


# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return render_template("login.html")


# -----------------------------
# Login
# -----------------------------
@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    user = User.query.filter_by(
        username=username,
        password=password
    ).first()

    if not user:

        flash("Invalid Username or Password")

        return redirect(url_for("home"))

    if user.role == "Admin":
        return redirect(url_for("admin_dashboard"))

    elif user.role == "Doctor":
        return redirect(url_for("doctor_dashboard"))

    elif user.role == "Nurse":
        return redirect(url_for("nurse_dashboard"))

    return redirect(url_for("home"))


# -----------------------------
# Admin Dashboard
# -----------------------------
@app.route("/admin")
def admin_dashboard():

    total_patients = Patient.query.count()

    low_risk = Patient.query.filter_by(
        risk="Low Risk"
    ).count()

    medium_risk = Patient.query.filter_by(
        risk="Medium Risk"
    ).count()

    high_risk = Patient.query.filter_by(
        risk="High Risk"
    ).count()

    recent_patients = Patient.query.order_by(
        Patient.id.desc()
    ).limit(5).all()

    return render_template(
        "admin_dashboard.html",
        total=total_patients,
        low=low_risk,
        medium=medium_risk,
        high=high_risk,
        recent_patients=recent_patients
    )


# -----------------------------
# Doctor Dashboard
# -----------------------------
@app.route("/doctor")
def doctor_dashboard():

    patients = Patient.query.all()

    return render_template(
        "doctor_dashboard.html",
        patients=patients
    )


# -----------------------------
# Nurse Dashboard
# -----------------------------
@app.route("/nurse")
def nurse_dashboard():

    patients = Patient.query.all()

    return render_template(
        "nurse_dashboard.html",
        patients=patients
    )
# -----------------------------
# Register Patient
# -----------------------------
@app.route("/register_patient", methods=["GET", "POST"])
def register_patient():

    if request.method == "POST":

        # Convert numeric values
        age = int(request.form["age"])
        temperature = float(request.form["temperature"])
        heart_rate = int(request.form["heart_rate"])
        oxygen_level = int(request.form["oxygen_level"])
        weight = float(request.form["weight"])
        height = float(request.form["height"])

        # AI Analysis
        bmi, score, risk, recommendation = analyze_patient(
            age=age,
            temperature=temperature,
            oxygen=oxygen_level,
            heart_rate=heart_rate,
            bmi_weight=weight,
            bmi_height=height
        )

        patient = Patient(

            name=request.form["name"],
            age=age,
            gender=request.form["gender"],

            mobile=request.form["mobile"],
            address=request.form["address"],

            temperature=temperature,
            blood_pressure=request.form["blood_pressure"],
            heart_rate=heart_rate,
            oxygen_level=oxygen_level,

            weight=weight,
            height=height,

            symptoms=request.form["symptoms"],
            existing_disease=request.form["existing_disease"],

            bmi=bmi,
            score=score,
            risk=risk,
            recommendation=recommendation
        )

        db.session.add(patient)
        db.session.commit()

        flash("Patient Registered Successfully!")

        return redirect(url_for("patient_list"))

    return render_template("register_patient.html")


# -----------------------------
# Patient List
# -----------------------------
@app.route("/patients")
def patient_list():

    patients = Patient.query.order_by(
        Patient.id.desc()
    ).all()

    return render_template(
        "patient_list.html",
        patients=patients
    )


# -----------------------------
# Search Patient
# -----------------------------
@app.route("/search")
def search_patient():

    keyword = request.args.get("keyword", "")

    patients = Patient.query.filter(
        Patient.name.contains(keyword)
    ).all()

    return render_template(
        "patient_list.html",
        patients=patients
    )
# -----------------------------
# Edit Patient
# -----------------------------
@app.route("/edit_patient/<int:id>", methods=["GET", "POST"])
def edit_patient(id):

    patient = Patient.query.get_or_404(id)

    if request.method == "POST":

        # Convert values
        age = int(request.form["age"])
        temperature = float(request.form["temperature"])
        heart_rate = int(request.form["heart_rate"])
        oxygen_level = int(request.form["oxygen_level"])
        weight = float(request.form["weight"])
        height = float(request.form["height"])

        # AI Analysis Again
        bmi, score, risk, recommendation = analyze_patient(
            age=age,
            temperature=temperature,
            oxygen=oxygen_level,
            heart_rate=heart_rate,
            bmi_weight=weight,
            bmi_height=height
        )

        # Update Patient
        patient.name = request.form["name"]
        patient.age = age
        patient.gender = request.form["gender"]

        patient.mobile = request.form["mobile"]
        patient.address = request.form["address"]

        patient.temperature = temperature
        patient.blood_pressure = request.form["blood_pressure"]
        patient.heart_rate = heart_rate
        patient.oxygen_level = oxygen_level

        patient.weight = weight
        patient.height = height

        patient.symptoms = request.form["symptoms"]
        patient.existing_disease = request.form["existing_disease"]

        patient.bmi = bmi
        patient.score = score
        patient.risk = risk
        patient.recommendation = recommendation

        db.session.commit()

        flash("Patient Updated Successfully!")

        return redirect(url_for("patient_list"))

    return render_template(
        "edit_patient.html",
        patient=patient
    )


# -----------------------------
# Delete Patient
# -----------------------------
@app.route("/delete_patient/<int:id>")
def delete_patient(id):

    patient = Patient.query.get_or_404(id)

    db.session.delete(patient)
    db.session.commit()

    flash("Patient Deleted Successfully!")

    return redirect(url_for("patient_list"))
# -----------------------------
# Error Handlers
# -----------------------------
@app.errorhandler(404)
def page_not_found(error):

    return render_template(
        "404.html"
    ), 404


@app.errorhandler(500)
def internal_server_error(error):

    return render_template(
        "500.html"
    ), 500


# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )