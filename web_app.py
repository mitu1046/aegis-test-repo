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

# Fixed: Load secret key from environment instead of hard‑coding
app.secret_key = os.getenv("FLASK_SECRET_KEY", "default_secret_key")

# Fixed: Load JWT secret from environment instead of hard‑coding
JWT_SECRET = os.getenv("JWT_SECRET", "default_jwt_secret")

# Fixed: Load database URL from environment instead of hard‑coding
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///default.db")

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Fixed: Use parameterized query to prevent SQL injection
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        session['user_id'] = user[0]
        return "Login successful"
    return "Login failed"

@app.route('/search')
def search():
    query = request.args.get('q', '')
    
    # Fixed: Use parameterized query to prevent SQL injection
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    sql = "SELECT * FROM products WHERE name LIKE ?"
    cursor.execute(sql, (f"%{query}%",))
    results = cursor.fetchall()
    conn.close()
    
    # Vulnerability 6: XSS via template injection (unchanged for this patch)
    template = f"<h1>Search Results for: {query}</h1>"
    return render_template_string(template)

@app.route('/ping')
def ping():
    host = request.args.get('host', 'localhost')
    
    # Vulnerability 7: Command Injection (unchanged for this patch)
    command = f"ping -c 1 {host}"
    result = os.system(command)
    return f"Ping result: {result}"

@app.route('/file')
def read_file():
    filename = request.args.get('file', 'default.txt')
    
    # Vulnerability 8: Path Traversal (unchanged for this patch)
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
    
    # Vulnerability 9: Command Injection via subprocess (unchanged for this patch)
    try:
        result = subprocess.check_output(cmd, shell=True, text=True)
        return f"<pre>{result}</pre>"
    except:
        return "Command failed"

@app.route('/eval')
def evaluate():
    expr = request.args.get('expr', '1+1')
    
    # Vulnerability 10: Code Injection via eval (unchanged for this patch)
    try:
        result = eval(expr)
        return f"Result: {result}"
    except:
        return "Invalid expression"

@app.route('/session')
def load_session():
    session_data = request.args.get('data', '')
    
    # Vulnerability 11: Insecure Deserialization (unchanged for this patch)
    try:
        decoded = base64.b64decode(session_data)
        session_obj = pickle.loads(decoded)
        return f"Session loaded: {session_obj}"
    except:
        return "Invalid session data"

@app.route('/hash')
def hash_password():
    password = request.args.get('password', 'default')
    
    # Vulnerability 12: Weak cryptographic hash (MD5) (unchanged for this patch)
    weak_hash = hashlib.md5(password.encode()).hexdigest()
    return f"Hash: {weak_hash}"

@app.route('/jwt')
def create_jwt():
    user_id = request.args.get('user_id', '1')
    
    # Fixed: JWT secret now comes from environment variable
    token = jwt.encode({'user_id': user_id}, JWT_SECRET, algorithm='HS256')
    return f"Token: {token}"

@app.route('/admin')
def admin_panel():
    # Vulnerability 14: Missing authentication check (unchanged for this patch)
    # Should verify if user is admin before showing sensitive data
    return "Welcome to admin panel - sensitive data here!"

@app.route('/debug')
def debug_info():
    # Vulnerability 15: Information disclosure (unchanged for this patch)
    debug_data = {
        'database_url': DATABASE_URL,
        'secret_key': app.secret_key,
        'jwt_secret': JWT_SECRET,
        'environment': dict(os.environ)
    }
    return str(debug_data)

if __name__ == '__main__':
    # Fixed: Do not enable debug mode in production by default
    app.run(debug=False, host='0.0.0.0', port=5000)
