from flask import Flask, request, jsonify
import json
import pymysql

# a simple rest api capable of crud operations on a "person" Resource
# interfacing with MySQL database

app = Flask(__name__)

def db_connect():
    conn = None
    try:
        conn = pymysql.connect(
            host='sql10.freesqldatabase.com',
            database='sql10646166',
            user='sql10646166',
            password='mgmaMA1dSl',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
            )
    except pymysql.Error as e:
        print(e)
    return conn

# CREATE Operation
@app.route('/api/', methods=['POST'])
def create_user():
    conn = db_connect()
    cursor = conn.cursor()

    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({'error': 'Please provide name'}), 400

    # Insert the new user into the database
    cursor.execute('INSERT INTO user (name) VALUES (%s)', (name,))

    conn.commit()
    conn.close()

    return jsonify({'message': 'User created Successfully: /api/user_id/{}'.format(cursor.lastrowid)}), 201

# READ Operation
@app.route('/api/<int:user_id>', methods=['GET'])
def read_user(user_id):
    conn = db_connect()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM user WHERE id=%s', (user_id,))
    person = cursor.fetchone()

    conn.close()

    if not person:
        return jsonify({'error': 'User not found'}), 404


    return jsonify(person), 200

# UPDATE Operation (PUT or PATCH)
@app.route('/api/<int:user_id>', methods=['PUT', 'PATCH'])
def update_user(user_id):
    conn = db_connect()
    cursor = conn.cursor()

    data = request.get_json()
    name = data.get('name')

    cursor.execute('SELECT * FROM user WHERE id=%s', (user_id,))
    person = cursor.fetchone()

    if not person:
        return jsonify({'error': 'User not found'}), 404

    if not name:
        name = person['name']

    cursor.execute('UPDATE user SET name=%s WHERE id=%s', (name, user_id))
    conn.commit()
    conn.close()

    return jsonify({'message': 'User updated Successfully: /api/user_id/{}'.format(user_id)}), 200

# DELETE Operation (DELETE)
@app.route('/api/<int:user_id>', methods=['DELETE'])
def delete_person(user_id):
    conn = db_connect()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM user WHERE id=%s', (user_id,))
    person = cursor.fetchone()

    if not person:
        return jsonify({'error': 'User not found'}), 404

    cursor.execute('DELETE FROM user WHERE id=%s', (user_id,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'User deleted Successfully: /api/user_id/{}'.format(user_id)}), 200

if __name__ == '__main__':
    app.run(debug=True)
