import os
from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
mongo_uri = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/flask_app')
client = MongoClient(mongo_uri)
db = client.get_default_database()
collection = db['users']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        # Insert data into MongoDB
        collection.insert_one({'username': username, 'email': email})
        return render_template('confirmation.html', username=username, email=email)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
