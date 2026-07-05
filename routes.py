from flask import Blueprint, request
import sqlite3

patient_routes = Blueprint("patient_routes", __name__)


@patient_routes.route("/patients")
def get_patients():

    connection = sqlite3.connect("patients.db")
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM patients")

    patients = cursor.fetchall()

    connection.close()

    return [dict(patient) for patient in patients]


@patient_routes.route("/patients/<patient_id>")
def get_patient(patient_id):

    connection = sqlite3.connect("patients.db")
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM patients WHERE patient_id = ?",
        (patient_id,)
    )

    patient = cursor.fetchone()

    connection.close()

    if patient:
        return dict(patient)

    return {"message": "Patient not found"}, 404

@patient_routes.route("/patients", methods=["POST"])
def create_patient():

    data = request.get_json()

    connection = sqlite3.connect("patients.db")

    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO patients
    (
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
    VALUES
    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
        data["patient_id"],
        data["first_name"],
        data["last_name"],
        data["dob"],
        data["gender"],
        data["phone"],
        data["email"],
        data["address"],
        data["blood_group"],
        data["created_at"]
    ))

    connection.commit()

    connection.close()

    return {
        "message": "Patient created successfully"
    }, 201

@patient_routes.route("/patients/<patient_id>", methods=["PUT"])
def update_patient(patient_id):

    data = request.get_json()

    connection = sqlite3.connect("patients.db")

    cursor = connection.cursor()

    cursor.execute("""
    UPDATE patients
    SET
        phone = ?,
        email = ?,
        address = ?
    WHERE patient_id = ?
    """,
    (
        data["phone"],
        data["email"],
        data["address"],
        patient_id
    ))

    connection.commit()

    connection.close()

    return {
        "message": "Patient updated successfully"
    }

@patient_routes.route("/patients/<patient_id>", methods=["DELETE"])
def delete_patient(patient_id):

    connection = sqlite3.connect("patients.db")

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM patients WHERE patient_id = ?",
        (patient_id,)
    )

    connection.commit()

    connection.close()

    return {
        "message": "Patient deleted successfully"
    }

@patient_routes.route("/providers")
def get_providers():

    connection = sqlite3.connect("patients.db")
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM providers")

    providers = cursor.fetchall()

    connection.close()

    return [dict(provider) for provider in providers]

@patient_routes.route("/providers/<provider_id>")
def get_provider(provider_id):

    connection = sqlite3.connect("patients.db")
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM providers WHERE provider_id = ?",
        (provider_id,)
    )

    provider = cursor.fetchone()

    connection.close()

    if provider:
        return dict(provider)

    return {"message": "Provider not found"}, 404

@patient_routes.route("/providers", methods=["POST"])
def create_provider():

    data = request.get_json()

    connection = sqlite3.connect("patients.db")
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO providers
    (
        provider_id,
        first_name,
        last_name,
        specialty,
        phone,
        email
    )
    VALUES
    (?, ?, ?, ?, ?, ?)
    """,
    (
        data["provider_id"],
        data["first_name"],
        data["last_name"],
        data["specialty"],
        data["phone"],
        data["email"]
    ))

    connection.commit()
    connection.close()

    return {
        "message": "Provider created successfully"
    }, 201

@patient_routes.route("/providers/<provider_id>", methods=["PUT"])
def update_provider(provider_id):

    data = request.get_json()

    connection = sqlite3.connect("patients.db")
    cursor = connection.cursor()

    cursor.execute("""
    UPDATE providers
    SET
        first_name = ?,
        last_name = ?,
        specialty = ?,
        phone = ?,
        email = ?
    WHERE provider_id = ?
    """,
    (
        data["first_name"],
        data["last_name"],
        data["specialty"],
        data["phone"],
        data["email"],
        provider_id
    ))

    connection.commit()
    connection.close()

    return {
        "message": "Provider updated successfully"
    }

@patient_routes.route("/providers/<provider_id>", methods=["DELETE"])
def delete_provider(provider_id):

    connection = sqlite3.connect("patients.db")
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM providers WHERE provider_id = ?",
        (provider_id,)
    )

    connection.commit()
    connection.close()

    return {
        "message": "Provider deleted successfully"
    }


@patient_routes.route("/appointments")
def get_appointments():

    connection = sqlite3.connect("patients.db")
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM appointments")

    appointments = cursor.fetchall()

    connection.close()

    return [dict(appointment) for appointment in appointments]


@patient_routes.route("/appointments/<int:appointment_id>")
def get_appointment(appointment_id):

    connection = sqlite3.connect("patients.db")
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM appointments WHERE appointment_id = ?",
        (appointment_id,)
    )

    appointment = cursor.fetchone()

    connection.close()

    if appointment:
        return dict(appointment)

    return {"message": "Appointment not found"}, 404


@patient_routes.route("/appointments", methods=["POST"])
def create_appointment():

    data = request.get_json()

    connection = sqlite3.connect("patients.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO appointments
        (patient_id, provider_id, appointment_date, status)
        VALUES (?, ?, ?, ?)
    """, (
        data["patient_id"],
        data["provider_id"],
        data["appointment_date"],
        data["status"]
    ))

    connection.commit()

    connection.close()

    return {
        "message": "Appointment created successfully"
    }, 201

@patient_routes.route("/appointments/<int:appointment_id>", methods=["PUT"])
def update_appointment(appointment_id):

    data = request.get_json()

    connection = sqlite3.connect("patients.db")
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE appointments
        SET
            appointment_date = ?,
            status = ?
        WHERE appointment_id = ?
    """,
    (
        data["appointment_date"],
        data["status"],
        appointment_id
    ))

    connection.commit()
    connection.close()

    return {
        "message": "Appointment updated successfully"
    }

@patient_routes.route("/appointments/<int:appointment_id>", methods=["DELETE"])
def delete_appointment(appointment_id):

    connection = sqlite3.connect("patients.db")
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM appointments WHERE appointment_id = ?",
        (appointment_id,)
    )

    connection.commit()
    connection.close()

    return {
        "message": "Appointment deleted successfully"
    }

@patient_routes.route("/allergies")
def get_allergies():

    connection = sqlite3.connect("patients.db")
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM allergies")

    allergies = cursor.fetchall()

    connection.close()

    return [dict(allergy) for allergy in allergies]

@patient_routes.route("/allergies/<int:allergy_id>")
def get_allergy(allergy_id):

    connection = sqlite3.connect("patients.db")
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM allergies WHERE allergy_id = ?",
        (allergy_id,)
    )

    allergy = cursor.fetchone()

    connection.close()

    if allergy:
        return dict(allergy)

    return {"message": "Allergy not found"}, 404

@patient_routes.route("/allergies", methods=["POST"])
def create_allergy():

    data = request.get_json()

    connection = sqlite3.connect("patients.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO allergies
        (
            patient_id,
            allergy_name,
            severity
        )
        VALUES (?, ?, ?)
    """, (
        data["patient_id"],
        data["allergy_name"],
        data["severity"]
    ))

    connection.commit()
    connection.close()

    return {
        "message": "Allergy created successfully"
    }, 201

@patient_routes.route("/allergies/<int:allergy_id>", methods=["PUT"])
def update_allergy(allergy_id):

    data = request.get_json()

    connection = sqlite3.connect("patients.db")
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE allergies
        SET
            allergy_name = ?,
            severity = ?
        WHERE allergy_id = ?
    """, (
        data["allergy_name"],
        data["severity"],
        allergy_id
    ))

    connection.commit()
    connection.close()

    return {
        "message": "Allergy updated successfully"
    }

@patient_routes.route("/allergies/<int:allergy_id>", methods=["DELETE"])
def delete_allergy(allergy_id):

    connection = sqlite3.connect("patients.db")
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM allergies WHERE allergy_id = ?",
        (allergy_id,)
    )

    connection.commit()
    connection.close()

    return {
        "message": "Allergy deleted successfully"
    }

@patient_routes.route("/medications")
def get_medications():

    connection = sqlite3.connect("patients.db")
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM medications")

    medications = cursor.fetchall()

    connection.close()

    return [dict(medication) for medication in medications]

@patient_routes.route("/medications/<int:medication_id>")
def get_medication(medication_id):

    connection = sqlite3.connect("patients.db")
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM medications WHERE medication_id = ?",
        (medication_id,)
    )

    medication = cursor.fetchone()

    connection.close()

    if medication:
        return dict(medication)

    return {"message": "Medication not found"}, 404

@patient_routes.route("/medications", methods=["POST"])
def create_medication():

    data = request.get_json()

    connection = sqlite3.connect("patients.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO medications
        (
            patient_id,
            medication_name,
            dosage
        )
        VALUES (?, ?, ?)
    """, (
        data["patient_id"],
        data["medication_name"],
        data["dosage"]
    ))

    connection.commit()
    connection.close()

    return {
        "message": "Medication created successfully"
    }, 201

@patient_routes.route("/medications/<int:medication_id>", methods=["PUT"])
def update_medication(medication_id):

    data = request.get_json()

    connection = sqlite3.connect("patients.db")
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE medications
        SET
            medication_name = ?,
            dosage = ?
        WHERE medication_id = ?
    """, (
        data["medication_name"],
        data["dosage"],
        medication_id
    ))

    connection.commit()
    connection.close()

    return {
        "message": "Medication updated successfully"
    }

@patient_routes.route("/medications/<int:medication_id>", methods=["DELETE"])
def delete_medication(medication_id):

    connection = sqlite3.connect("patients.db")
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM medications WHERE medication_id = ?",
        (medication_id,)
    )

    connection.commit()
    connection.close()

    return {
        "message": "Medication deleted successfully"
    }

@patient_routes.route("/observations")
def get_observations():

    connection = sqlite3.connect("patients.db")
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM observations")

    observations = cursor.fetchall()

    connection.close()

    return [dict(observation) for observation in observations]

@patient_routes.route("/observations/<int:observation_id>")
def get_observation(observation_id):

    connection = sqlite3.connect("patients.db")
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM observations WHERE observation_id = ?",
        (observation_id,)
    )

    observation = cursor.fetchone()

    connection.close()

    if observation:
        return dict(observation)

    return {"message": "Observation not found"}, 404

@patient_routes.route("/observations", methods=["POST"])
def create_observation():

    data = request.get_json()

    connection = sqlite3.connect("patients.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO observations
        (
            patient_id,
            observation_type,
            result,
            observation_date
        )
        VALUES (?, ?, ?, ?)
    """, (
        data["patient_id"],
        data["observation_type"],
        data["result"],
        data["observation_date"]
    ))

    connection.commit()
    connection.close()

    return {
        "message": "Observation created successfully"
    }, 201

@patient_routes.route("/observations/<int:observation_id>", methods=["PUT"])
def update_observation(observation_id):

    data = request.get_json()

    connection = sqlite3.connect("patients.db")
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE observations
        SET
            observation_type = ?,
            result = ?,
            observation_date = ?
        WHERE observation_id = ?
    """, (
        data["observation_type"],
        data["result"],
        data["observation_date"],
        observation_id
    ))

    connection.commit()
    connection.close()

    return {
        "message": "Observation updated successfully"
    }

@patient_routes.route("/observations/<int:observation_id>", methods=["DELETE"])
def delete_observation(observation_id):

    connection = sqlite3.connect("patients.db")
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM observations WHERE observation_id = ?",
        (observation_id,)
    )

    connection.commit()
    connection.close()

    return {
        "message":"Observation deleted successfully"
    }



@patient_routes.route("/patients/search")
def search_patients():

    last_name = request.args.get("last_name")
    gender = request.args.get("gender")

    connection = sqlite3.connect("patients.db")
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    if last_name:
        cursor.execute(
            "SELECT * FROM patients WHERE last_name LIKE ?",
            ('%' + last_name + '%',)
        )

    elif gender:
        cursor.execute(
            "SELECT * FROM patients WHERE gender = ?",
            (gender,)
        )

    else:
        return {"message": "Please provide a search parameter"}, 400

    patients = cursor.fetchall()

    connection.close()

    return [dict(patient) for patient in patients]



@patient_routes.route("/hl7", methods=["POST"])
def hl7_to_json():

    hl7_message = request.data.decode("utf-8")

    segments = hl7_message.split("\n")

    patient = {}

    for segment in segments:

        fields = segment.split("|")

        if fields[0] == "PID":

            patient["patient_id"] = fields[3]

            name = fields[5].split("^")

            patient["last_name"] = name[0]
            patient["first_name"] = name[1]

            patient["dob"] = fields[7]
            patient["gender"] = fields[8]

    return patient

@patient_routes.route("/patients/<patient_id>/summary")
def get_patient_summary(patient_id):

    connection = sqlite3.connect("patients.db")
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute(
    "SELECT * FROM patients WHERE patient_id = ?",
    (patient_id,)
)

    patient = cursor.fetchone()

    if not patient:
     connection.close()
     return {"message": "patient not found"}, 404

    cursor.execute(
    "SELECT * FROM appointments WHERE patient_id = ?",
     (patient_id,)
)

    appointments = cursor.fetchall()

    cursor.execute(
    "SELECT * FROM allergies WHERE patient_id = ?",
     (patient_id,)
)

    allergies = cursor.fetchall()

    cursor.execute(
    "SELECT * FROM medications WHERE patient_id = ?",
     (patient_id,)
)

    medications = cursor.fetchall()

    cursor.execute(
    "SELECT * FROM observations WHERE patient_id = ?",
     (patient_id,)
)

    observations = cursor.fetchall()

    connection.close()

    return {
        "patient": dict(patient),
        "appointments": [dict(a) for a in appointments],
        "allergies": [dict(a) for a in allergies],
        "medications": [dict(m) for m in medications],
        "observations": [dict(o) for o in observations]
}

@patient_routes.route("/patients/age/<int:age>")
def get_patients_by_age(age):

    connection = sqlite3.connect("patients.db")
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM patients
        WHERE (CAST(strftime('%Y', 'now') AS INTEGER) -
               CAST(strftime('%Y', dob) AS INTEGER)) >= ?
    """, (age,))

    patients = cursor.fetchall()

    connection.close()

    return [dict(patient) for patient in patients]