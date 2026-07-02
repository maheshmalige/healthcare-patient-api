# Healthcare Patient API

A RESTful Healthcare Patient API built using Python, Flask, and SQLite.

This project demonstrates healthcare backend development concepts including CRUD operations, HL7 message parsing, REST APIs, and SQLite database integration.

---

## Features

- Patient CRUD (Create, Read, Update, Delete)
- Provider CRUD
- Appointment CRUD
- Allergy CRUD
- Medication CRUD
- Observation CRUD
- Patient Search
- HL7 v2 Message to JSON Transformation
- SQLite Database
- REST API using Flask

---

## Technologies Used

- Python 3
- Flask
- SQLite
- SQL
- REST API
- JSON
- HL7 v2
- Git
- GitHub

---

## Project Structure

```
patient-api/
│
├── app.py
├── routes.py
├── database.py
├── models.py
├── seed_database.py
├── patients.db
├── requests.http
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Database Tables

- Patients
- Providers
- Appointments
- Allergies
- Medications
- Observations

---

## API Endpoints

### Patients

| Method | Endpoint |
|---------|----------|
| GET | /patients |
| GET | /patients/<patient_id> |
| POST | /patients |
| PUT | /patients/<patient_id> |
| DELETE | /patients/<patient_id> |

### Providers

| Method | Endpoint |
|---------|----------|
| GET | /providers |
| GET | /providers/<provider_id> |
| POST | /providers |
| PUT | /providers/<provider_id> |
| DELETE | /providers/<provider_id> |

### Appointments

| Method | Endpoint |
|---------|----------|
| GET | /appointments |
| GET | /appointments/<appointment_id> |
| POST | /appointments |
| PUT | /appointments/<appointment_id> |
| DELETE | /appointments/<appointment_id> |

### Allergies

| Method | Endpoint |
|---------|----------|
| GET | /allergies |
| GET | /allergies/<allergy_id> |
| POST | /allergies |
| PUT | /allergies/<allergy_id> |
| DELETE | /allergies/<allergy_id> |

### Medications

| Method | Endpoint |
|---------|----------|
| GET | /medications |
| GET | /medications/<medication_id> |
| POST | /medications |
| PUT | /medications/<medication_id> |
| DELETE | /medications/<medication_id> |

### Observations

| Method | Endpoint |
|---------|----------|
| GET | /observations |
| GET | /observations/<observation_id> |
| POST | /observations |
| PUT | /observations/<observation_id> |
| DELETE | /observations/<observation_id> |

### Search

| Method | Endpoint |
|---------|----------|
| GET | /patients/search |

Example:

```
GET /patients/search?gender=Male
```

or

```
GET /patients/search?last_name=Smith
```

---

## HL7 Transformation

This project includes a simple HL7 v2 parser.

Endpoint:

```
POST /hl7
```

Example HL7 Message:

```
MSH|^~\&|EPIC|HOSPITAL|LAB|LAB|202607012200||ADT^A01|12345|P|2.5
PID|1||P1001||Smith^John||19900101|M
```

Returns:

```json
{
    "patient_id": "P1001",
    "first_name": "John",
    "last_name": "Smith",
    "dob": "19900101",
    "gender": "M"
}
```

---

## Installation

Clone the repository

```
git clone https://github.com/maheshmalige/healthcare-patient-api.git
```

Move into the project

```
cd healthcare-patient-api
```

Create a virtual environment

```
python -m venv venv
```

Activate virtual environment

Windows PowerShell

```
.\venv\Scripts\Activate.ps1
```

Install dependencies

```
pip install -r requirements.txt
```

Run the application

```
python app.py
```

The application runs at

```
http://127.0.0.1:5000
```

---

## Future Improvements

- HL7 ADT Message Processing
- FHIR Patient Resource
- JWT Authentication
- Swagger / OpenAPI Documentation
- Docker Support
- Unit Testing
- Logging
- Cloud Deployment

---

## Author

Mahesh Malige

Healthcare Integration Specialist

Dublin, Ireland