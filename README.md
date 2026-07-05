# Healthcare Patient API

A RESTful Healthcare Patient API built using **Python**, **Flask**, and **SQLite** to simulate real-world healthcare interoperability workflows.

This project demonstrates the design and development of REST APIs, SQL-based data access, CRUD operations, HL7 v2 message parsing, and healthcare data management. It is designed as a hands-on learning project to strengthen practical skills in healthcare integration, API development, debugging, and interoperability.

---

# Objectives

- Build RESTful APIs using Flask
- Practice CRUD operations with SQLite
- Improve SQL querying and data retrieval skills
- Implement healthcare workflows using REST APIs
- Parse HL7 v2 messages into structured JSON
- Practice API debugging and troubleshooting
- Strengthen healthcare interoperability knowledge
- Prepare for Healthcare Integration and Interoperability interviews

---

# Technologies Used

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

# Features

### Patient Management
- Create Patient
- Retrieve All Patients
- Retrieve Patient by ID
- Update Patient
- Delete Patient

### Provider Management
- Create Provider
- Retrieve All Providers
- Retrieve Provider by ID
- Update Provider
- Delete Provider

### Appointment Management
- Create Appointment
- Retrieve All Appointments
- Retrieve Appointment by ID
- Update Appointment
- Delete Appointment

### Allergy Management
- Create Allergy
- Retrieve All Allergies
- Update Allergy
- Delete Allergy

### Medication Management
- Create Medication
- Retrieve All Medications
- Update Medication
- Delete Medication

### Observation Management
- Create Observation
- Retrieve All Observations
- Update Observation
- Delete Observation

### Additional Features

- Patient Search API
- HL7 v2 Message Parsing
- SQLite Database Integration
- RESTful API Design
- JSON Responses
- Parameterized SQL Queries

---

# Project Structure

```
healthcare-patient-api/
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

# Database Tables

- Patients
- Providers
- Appointments
- Allergies
- Medications
- Observations

---

# API Endpoints

## Patients

| Method | Endpoint |
|--------|----------|
| GET | /patients |
| GET | /patients/<patient_id> |
| POST | /patients |
| PUT | /patients/<patient_id> |
| DELETE | /patients/<patient_id> |

---

## Providers

| Method | Endpoint |
|--------|----------|
| GET | /providers |
| GET | /providers/<provider_id> |
| POST | /providers |
| PUT | /providers/<provider_id> |
| DELETE | /providers/<provider_id> |

---

## Appointments

| Method | Endpoint |
|--------|----------|
| GET | /appointments |
| GET | /appointments/<appointment_id> |
| POST | /appointments |
| PUT | /appointments/<appointment_id> |
| DELETE | /appointments/<appointment_id> |

---

## Allergies

| Method | Endpoint |
|--------|----------|
| GET | /allergies |
| GET | /allergies/<allergy_id> |
| POST | /allergies |
| PUT | /allergies/<allergy_id> |
| DELETE | /allergies/<allergy_id> |

---

## Medications

| Method | Endpoint |
|--------|----------|
| GET | /medications |
| GET | /medications/<medication_id> |
| POST | /medications |
| PUT | /medications/<medication_id> |
| DELETE | /medications/<medication_id> |

---

## Observations

| Method | Endpoint |
|--------|----------|
| GET | /observations |
| GET | /observations/<observation_id> |
| POST | /observations |
| PUT | /observations/<observation_id> |
| DELETE | /observations/<observation_id> |

---

## Search

| Method | Endpoint |
|--------|----------|
| GET | /patients/search |

### Example

```
GET /patients/search?gender=Male
```

or

```
GET /patients/search?last_name=Smith
```

---

# HL7 Message Parser

This project includes a basic HL7 v2 parser that extracts patient demographic information from a PID segment and converts it into JSON.

### Endpoint

```
POST /hl7
```

### Sample HL7 Message

```
MSH|^~\&|EPIC|HOSPITAL|LAB|LAB|202607012200||ADT^A01|12345|P|2.5
PID|1||P1001||Smith^John||19900101|M
```

### Sample Response

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

# HTTP Status Codes

| Status Code | Description |
|-------------|-------------|
| 200 | Request Successful |
| 201 | Resource Created |
| 400 | Bad Request |
| 404 | Resource Not Found |
| 500 | Internal Server Error |

---

# Installation

Clone the repository

```bash
git clone https://github.com/maheshmalige/healthcare-patient-api.git
```

Navigate to the project

```bash
cd healthcare-patient-api
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

The API will be available at

```
http://127.0.0.1:5000
```

---

# Testing

The APIs can be tested using:

- Postman
- VS Code REST Client (`requests.http`)
- Web Browser (GET requests)

---

# Learning Progress

This repository is continuously updated while practicing:

- Flask REST API Development
- SQLite Database Integration
- SQL Queries
- CRUD Operations
- Healthcare Interoperability
- HL7 v2 Message Processing
- API Debugging
- Healthcare Data Modelling

---

# Future Improvements

- Patient Summary Endpoint
- Appointment Details Endpoint using SQL JOIN
- FHIR Patient Resource
- HL7 ADT Message Persistence
- JWT Authentication
- Pagination
- Filtering and Sorting
- Swagger / OpenAPI Documentation
- Docker Support
- Unit Testing
- Logging
- CI/CD Pipeline
- Cloud Deployment

---

# Author

**Mahesh Malige**

Healthcare Integration Specialist | HL7 | REST APIs | Flask | Python | SQL

Dublin, Ireland

GitHub: https://github.com/maheshmalige

---

## License

This project is licensed under the MIT License.
