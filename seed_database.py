import sqlite3
from faker import Faker
from random import choice
from datetime import datetime

fake = Faker()

connection = sqlite3.connect("patients.db")
cursor = connection.cursor()

genders = ["Male", "Female"]

blood_groups = ["A+","A-","B+","B-","AB+","AB-","O+","O-"]

specialties = [
    "Cardiology","Neurology","Radiology","Oncology","Pediatrics",
    "Orthopedics","Emergency Medicine","General Medicine",
    "Dermatology","Psychiatry"
]

statuses = ["Scheduled","Completed","Cancelled","No Show"]

allergy_names = [
    "Penicillin","Peanuts","Latex","Dust","Milk",
    "Egg","Shellfish","Soy","Pollen","Bee Sting"
]

severity_levels = ["Low","Moderate","High"]

medication_names = [
    "Paracetamol","Ibuprofen","Metformin","Amoxicillin",
    "Aspirin","Atorvastatin","Omeprazole","Losartan",
    "Insulin","Vitamin D"
]

dosages = ["5 mg","10 mg","20 mg","50 mg","100 mg","250 mg","500 mg"]

observation_types = [
    "Blood Pressure",
    "Heart Rate",
    "Temperature",
    "Respiratory Rate",
    "Oxygen Saturation",
    "Blood Glucose"
]


def seed_patients():
    cursor.execute("DELETE FROM patients")

    for i in range(1,1001):

        cursor.execute("""
        INSERT INTO patients(
            patient_id,
            first_name,
            last_name,
            dob,
            gender,
            phone,
            email,
            address,
            blood_group,
            created_at
        )
        VALUES(?,?,?,?,?,?,?,?,?,?)
        """,
        (
            f"P{i:04d}",
            fake.first_name(),
            fake.last_name(),
            str(fake.date_of_birth(minimum_age=1, maximum_age=90)),
            choice(genders),
            fake.phone_number(),
            fake.email(),
            fake.address(),
            choice(blood_groups),
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))

    print("✅ 1000 Patients Created")


def seed_providers():
    cursor.execute("DELETE FROM providers")

    for i in range(1,101):

        cursor.execute("""
        INSERT INTO providers(
            provider_id,
            first_name,
            last_name,
            specialty,
            phone,
            email
        )
        VALUES(?,?,?,?,?,?)
        """,
        (
            f"D{i:03d}",
            fake.first_name(),
            fake.last_name(),
            choice(specialties),
            fake.phone_number(),
            fake.email()
        ))

    print("✅ 100 Providers Created")


def seed_appointments():
    cursor.execute("DELETE FROM appointments")

    for _ in range(5000):

        cursor.execute("""
        INSERT INTO appointments(
            patient_id,
            provider_id,
            appointment_date,
            status
        )
        VALUES(?,?,?,?)
        """,
        (
            f"P{fake.random_int(1,1000):04d}",
            f"D{fake.random_int(1,100):03d}",
            fake.date_time_between(start_date="-1y", end_date="+1y").strftime("%Y-%m-%d %H:%M:%S"),
            choice(statuses)
        ))

    print("✅ 5000 Appointments Created")


def seed_allergies():
    cursor.execute("DELETE FROM allergies")

    for _ in range(2000):

        cursor.execute("""
        INSERT INTO allergies(
            patient_id,
            allergy_name,
            severity
        )
        VALUES(?,?,?)
        """,
        (
            f"P{fake.random_int(1,1000):04d}",
            choice(allergy_names),
            choice(severity_levels)
        ))

    print("✅ 2000 Allergies Created")


def seed_medications():
    cursor.execute("DELETE FROM medications")

    for _ in range(3000):

        cursor.execute("""
        INSERT INTO medications(
            patient_id,
            medication_name,
            dosage
        )
        VALUES(?,?,?)
        """,
        (
            f"P{fake.random_int(1,1000):04d}",
            choice(medication_names),
            choice(dosages)
        ))

    print("✅ 3000 Medications Created")


def seed_observations():
    cursor.execute("DELETE FROM observations")

    for _ in range(10000):

        obs = choice(observation_types)

        if obs == "Blood Pressure":
            result = f"{fake.random_int(90,150)}/{fake.random_int(60,100)} mmHg"
        elif obs == "Heart Rate":
            result = f"{fake.random_int(60,110)} bpm"
        elif obs == "Temperature":
            result = f"{round(fake.pyfloat(left_digits=2,right_digits=1,min_value=36,max_value=39),1)} °C"
        elif obs == "Respiratory Rate":
            result = f"{fake.random_int(12,24)} breaths/min"
        elif obs == "Oxygen Saturation":
            result = f"{fake.random_int(92,100)} %"
        else:
            result = f"{fake.random_int(70,180)} mg/dL"

        cursor.execute("""
        INSERT INTO observations(
            patient_id,
            observation_type,
            result,
            observation_date
        )
        VALUES(?,?,?,?)
        """,
        (
            f"P{fake.random_int(1,1000):04d}",
            obs,
            result,
            fake.date_time_between(start_date="-2y", end_date="now").strftime("%Y-%m-%d %H:%M:%S")
        ))

    print("✅ 10000 Observations Created")


if __name__ == "__main__":

    seed_patients()
    seed_providers()
    seed_appointments()
    seed_allergies()
    seed_medications()
    seed_observations()

    connection.commit()
    connection.close()

    print("\n🏥 Healthcare Database Created Successfully!")
