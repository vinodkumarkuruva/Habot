from .models import Employee,User
from flask import request, jsonify
from habot import app, db,jwt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import datetime

# User Registration
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 400
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

# User Login
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid username or password"}), 401
    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200

# Protect Employee routes with JWT
@app.route('/api/employees/', methods=['POST'])
@jwt_required()
def create_employee():
    current_user = get_jwt_identity()  # Fetch authenticated user ID
    data = request.get_json()
    if not data.get('name') or not data.get('email'):
        return jsonify({"error": "Name and email are required"}), 400
    if Employee.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email already exists"}), 400
    employee = Employee(
        name=data['name'],
        email=data['email'],
        department=data.get('department'),
        role=data.get('role')
    )
    db.session.add(employee)
    db.session.commit()
    return jsonify(employee.to_dict()), 201

# Filter by department and Role
@app.route('/api/employees/', methods=['GET'])
@jwt_required()
def list_employees():
    page = request.args.get('page', 1, type=int)
    department = request.args.get('department')
    role = request.args.get('role')
    query = Employee.query
    if department:
        query = query.filter(Employee.department == department)
    if role:
        query = query.filter(Employee.role == role)
    employees = query.paginate(page=page, per_page=10, error_out=False).items
    return jsonify([employee.to_dict() for employee in employees]), 200

# Retrieve by id
@app.route('/api/employees/<int:id>/', methods=['GET'])
@jwt_required()
def get_employee(id):
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404
    return jsonify(employee.to_dict()), 200

# Update by id
@app.route('/api/employees/<int:id>/', methods=['PUT'])
@jwt_required()
def update_employee(id):
    data = request.get_json()
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404
    employee.name = data.get('name', employee.name)
    employee.email = data.get('email', employee.email)
    employee.department = data.get('department', employee.department)
    employee.role = data.get('role', employee.role)
    db.session.commit()
    return jsonify(employee.to_dict()), 200

# Delete_by_id
@app.route('/api/employees/<int:id>/', methods=['DELETE'])
@jwt_required()
def delete_employee(id):
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404
    db.session.delete(employee)
    db.session.commit()
    return jsonify({'message':'Deleted Successfully'}), 204