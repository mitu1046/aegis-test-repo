#!/usr/bin/env python3
"""
Vulnerable Web Application for Testing Aegis
Contains multiple security vulnerabilities for detection and remediation
"""

from flask import Flask, request, render_template_string, session, redirect
import sqlite3
import os
import subprocess
import hashlib
import jwt
import pickle
import base64

app = Flask(__name__)

# Vulnerability 1: Hardcoded secret key
app.secret_key = "hardcoded_secret_key_123"

# Vulnerability 2: Hardcoded JWT secret
JWT_SECRET = "super_secret_jwt_key"

# Vulnerability 3: Hardcoded database credentials
DATABASE_URL = "postgresql://admin:password123@localhost/mydb"

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Vulnerability 4: SQL Injection in login
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    
    if user:
        session['user_id'] = user[0]
        return "Login successful"
    return "Login failed"

@app.route('/search')
def search():
    query = request.args.get('q', '')
    
    # Vulnerability 5: SQL Injection in search
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    sql = f"SELECT * FROM products WHERE name LIKE '%{query}%'"
    cursor.execute(sql)
    results = cursor.fetchall()
    conn.close()
    
    # Vulnerability 6: XSS via template injection
    template = f"<h1>Search Results for: {query}</h1>"
    return render_template_string(template)

@app.route('/ping')
def ping():
    host = request.args.get('host', 'localhost')
    
    # Vulnerability 7: Command Injection
    command = f"ping -c 1 {host}"
    result = os.system(command)
    return f"Ping result: {result}"

@app.route('/file')
def read_file():
    filename = request.args.get('file', 'default.txt')
    
    # Vulnerability 8: Path Traversal
    filepath = os.path.join('/var/www/files', filename)
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        return content
    except:
        return "File not found"

@app.route('/exec')
def execute():
    cmd = request.args.get('cmd', 'ls')
    
    # Vulnerability 9: Command Injection via subprocess
    try:
        result = subprocess.check_output(cmd, shell=True, text=True)
        return f"<pre>{result}</pre>"
    except:
        return "Command failed"

@app.route('/eval')
def evaluate():
    expr = request.args.get('expr', '1+1')
    
    # Vulnerability 10: Code Injection via eval
    try:
        result = eval(expr)
        return f"Result: {result}"
    except:
        return "Invalid expression"

@app.route('/session')
def load_session():
    session_data = request.args.get('data', '')
    
    # Vulnerability 11: Insecure Deserialization
    try:
        decoded = base64.b64decode(session_data)
        session_obj = pickle.loads(decoded)
        return f"Session loaded: {session_obj}"
    except:
        return "Invalid session data"

@app.route('/hash')
def hash_password():
    password = request.args.get('password', 'default')
    
    # Vulnerability 12: Weak cryptographic hash (MD5)
    weak_hash = hashlib.md5(password.encode()).hexdigest()
    return f"Hash: {weak_hash}"

@app.route('/jwt')
def create_jwt():
    user_id = request.args.get('user_id', '1')
    
    # Vulnerability 13: JWT with weak secret
    token = jwt.encode({'user_id': user_id}, JWT_SECRET, algorithm='HS256')
    return f"Token: {token}"

@app.route('/admin')
def admin_panel():
    # Vulnerability 14: Missing authentication check
    # Should verify if user is admin before showing sensitive data
    return "Welcome to admin panel - sensitive data here!"

@app.route('/debug')
def debug_info():
    # Vulnerability 15: Information disclosure
    debug_data = {
        'database_url': DATABASE_URL,
        'secret_key': app.secret_key,
        'jwt_secret': JWT_SECRET,
        'environment': dict(os.environ)
    }
    return str(debug_data)

if __name__ == '__main__':
    # Vulnerability 16: Debug mode in production
    app.run(debug=True, host='0.0.0.0', port=5000)