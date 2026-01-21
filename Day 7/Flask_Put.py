from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
users = [
    {"id": 1, "name": "Raja"},
    {"id": 2, "name": "Rama"}
]

# Home route
@app.route("/", methods=["GET"])
def home():
    return "Welcome to User API"

# Get all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# Get user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)
    return jsonify({"message": "user not found"}), 404

# Add new user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "Name field is required"}), 400

    new_user = {
        "id": len(users) + 1,
        "name": data["name"]
    }

    users.append(new_user)
    return jsonify(new_user), 201


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "Name field is required"}), 400

    for user in users:
        if user["id"] == user_id:
            user["name"] = data["name"]
            return jsonify(user), 200

    return jsonify({"message": "user not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
