from flask import Flask, request, jsonify, render_template , redirect, url_for
from dotenv import load_dotenv
import pymongo
from pymongo.server_api import ServerApi
import os

load_dotenv()
MONGO_URI=os.getenv("MONGO_URI")
client = pymongo.MongoClient(MONGO_URI, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("Successfully connected to MongoDB!")
except Exception as e:
    print(f"Connection failed: {e}")
db = client["Docker_assignment"]

app = Flask(__name__)

@app.route('/')
def hello_world():

    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        if request.is_json:
            form_data = request.get_json()
            print("Received form data:", form_data)
        else:
            form_data = request.form.to_dict()

        result = db["design_info"].insert_one(form_data)
        print("Inserted document ID:", result.inserted_id)
        return jsonify({"status": "success", "message": "Data saved."}), 200
    
    else:
        return jsonify({"error": "Method not allowed"}), 405
if __name__ == '__main__':

    app.run(port=3000,host='0.0.0.0', debug=True)