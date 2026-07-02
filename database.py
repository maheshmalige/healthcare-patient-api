import sqlite3

DATABASE_NAME = "patients.db"


def create_connection():
    return sqlite3.connect(DATABASE_NAME)


def create_database():

    connection = create_connection()
    cursor = connection.cursor()

    # Patients
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        patient_id TEXT PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        dob TEXT,
        gender TEXT,
        phone TEXT,
        email TEXT,
        address TEXT,
        blood_group TEXT,
        created_at TEXT
    )
    """)

    # Providers
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS providers (
        provider_id TEXT PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        specialty TEXT,
        phone TEXT,
        email TEXT
    )
    """)

    # Appointments
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
        appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id TEXT,
        provider_id TEXT,
        appointment_date TEXT,
        status TEXT
    )
    """)

    # Allergies
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS allergies (
        allergy_id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id TEXT,
        allergy_name TEXT,
        severity TEXT
    )
    """)

    # Medications
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS medications (
        medication_id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id TEXT,
        medication_name TEXT,
        dosage TEXT
    )
    """)

    # Observations
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS observations (
        observation_id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id TEXT,
        observation_type TEXT,
        result TEXT,
        observation_date TEXT
    )
    """)

    connection.commit()
    connection.close()