from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql10646166:mgmaMA1dSl@sql10.freesqldatabase.com/sql10646166'

db = SQLAlchemy(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

# CREATE Operation (POST)
@app.route('/api/', methods=['POST'])
def create_user():
    name = request.form.get('name')
    """
    data = request.get_json()
    name = data.get('name')
    """

    if not name:
        return jsonify({'error': 'Please provide a name'}), 400

    # Validate that the "name" is a string
    if not isinstance(name, str):
        return jsonify({'error': 'Name must be a string'}), 400

    new_user = User(name=name)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

# READ Operation (GET)
@app.route('/api/<int:user_id>', methods=['GET'])
def read_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({'id': user.id, 'name': user.name}), 200

# UPDATE Operation (PUT or PATCH)
@app.route('/api/<int:user_id>', methods=['PUT', 'PATCH'])
def update_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()
    name = data.get('name')

    if name is not None:
        user.name = name

    db.session.commit()

    return jsonify({'message': 'User updated successfully'}), 200

# DELETE Operation (DELETE)
@app.route('/api/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({'error': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'User deleted successfully'}), 200

# READ Operation for Listing All Users (GET)
@app.route('/api/users', methods=['GET'])
def list_users():
    users = User.query.all()
    user_list = [{'id': user.id, 'name': user.name} for user in users]

    return jsonify(user_list), 200

if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    app.run(debug=True)
