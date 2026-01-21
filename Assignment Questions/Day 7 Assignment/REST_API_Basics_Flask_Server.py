# app.py
# Simple User Management REST API using Flask

from flask import Flask, jsonify, request

# Create Flask application
app = Flask(__name__)

# In-memory user storage
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]


# GET /users → Return all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200


# GET /users/<id> → Return user details by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user), 200

    return jsonify({
        "error": "User not found"
    }), 404


# POST /users → Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    if not request.is_json:
        return jsonify({
            "error": "Invalid request",
            "message": "Request body must be JSON"
        }), 400

    data = request.get_json()

    if "name" not in data or not data["name"]:
        return jsonify({
            "error": "Invalid data",
            "message": "User 'name' is required"
        }), 400

    new_id = users[-1]["id"] + 1 if users else 1

    new_user = {
        "id": new_id,
        "name": data["name"]
    }

    users.append(new_user)

    return jsonify(new_user), 201


# Run the Flask application
if __name__ == "__main__":
    app.run(port=5000)
