from flask import Flask
from routes import patient_routes
from database import create_database

app = Flask(__name__)

app.register_blueprint(patient_routes)

create_database()

@app.route("/")
def home():
    return "Healthcare Patient API"

if __name__ == "__main__":
    app.run(debug=True)

   