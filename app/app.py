from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://nosql-db:27017/")


db = client["some_test"]
collection = db["some_test"]


@app.route('/api', methods=['GET', 'POST', 'PUT'])
def manage_key():
    """
       Handle key-value management for a MongoDB collection.

       This function supports three HTTP methods:
       - GET: Retrieve the value associated with a given key.
       - POST: Insert a new key-value pair into the collection.
       - PUT: Update the value associated with an existing key.

       Request Parameters:
       - key: The key to identify the data.
       - value: The value associated with the key.
       - new_value: The new value to update an existing key's value.

       Returns:
       - If the request is successful, it returns a response with appropriate HTTP status and a message.
       - If the request fails, it returns an error message and the appropriate HTTP status.

       HTTP Status Codes:
       - 200: Successful operation.
       - 400: Invalid data in the request.
       - 404: The requested key was not found in the collection.
       """
    if request.method == 'GET':
        key = request.json.get('key')
        value = request.json.get('value')
        data = collection.find_one({key: value})
        if data:
            return jsonify({key: data[key]})
        return "Key not found", 404
    elif request.method == 'POST':
        key = request.json.get('key')
        value = request.json.get('value')
        if value is not None:
            collection.insert_one({key: value})
            return "Key updated", 200
        return "Invalid data", 400
    elif request.method == 'PUT':
        key = request.json.get('key')
        value = request.json.get('value')
        new_value = request.json.get('new_value')
        if value is not None:
            collection.update_one({key: value}, {"$set": {key: new_value}}, upsert=True)
            return "Key updated", 200
        return "Invalid data", 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
