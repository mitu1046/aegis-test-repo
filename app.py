import sqlite3
import os
import pickle
import base64
import subprocess
import hashlib

# Vulnerability 1: Hardcoded AWS Credentials
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# Vulnerability 2: Hardcoded Database Password
DB_PASSWORD = "super_secret_db_password_123"

def get_user(username):
    # Vulnerability 3: SQL Injection (f-string)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    result = cursor.fetchone()
    conn.close()
    return result

def search_users(search_term):
    # Vulnerability 4: SQL Injection (string concatenation)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name LIKE '%" + search_term + "%'")
    results = cursor.fetchall()
    conn.close()
    return results

def ping_server(host):
    # Vulnerability 5: Command Injection (os.system with user input)
    command = f"ping -c 1 {host}"
    print(f"Executing: {command}")
    return os.system(command)

def execute_system_command(cmd):
    # Vulnerability 6: Command Injection (subprocess with shell=True)
    return subprocess.check_output(cmd, shell=True)

def read_file(filename):
    # Vulnerability 7: Path Traversal
    filepath = os.path.join('/var/www/uploads', filename)
    with open(filepath, 'r') as f:
        return f.read()

def load_user_session(session_data):
    # Vulnerability 8: Insecure Deserialization (pickle)
    decoded_data = base64.b64decode(session_data)
    session = pickle.loads(decoded_data)
    return session

def hash_password(password):
    # Vulnerability 9: Weak Cryptographic Hashing (MD5)
    m = hashlib.md5()
    m.update(password.encode('utf-8'))
    return m.hexdigest()

if __name__ == "__main__":
    print("Vulnerable Test App Running")