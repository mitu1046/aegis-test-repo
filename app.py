import sqlite3
import os
import pickle
import base64
import subprocess

# Vulnerability 1: Hardcoded credentials
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
DB_PASSWORD = "super_secret_db_password_123"

def get_user(username):
    # Vulnerability 2: SQL Injection (f-string)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    result = cursor.fetchone()
    conn.close()
    return result

def search_users(search_term):
    # Vulnerability 3: SQL Injection (f-string)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE name LIKE '%{search_term}%'")
    results = cursor.fetchall()
    conn.close()
    return results

def ping_server(host):
    # Vulnerability 4: Command Injection
    # User input is passed directly to os.system
    command = f"ping -c 1 {host}"
    print(f"Executing: {command}")
    return os.system(command)

def read_file(filename):
    # Vulnerability 5: Path Traversal
    # Allows reading any file on the system if path contains ../
    filepath = os.path.join('/var/www/uploads', filename)
    with open(filepath, 'r') as f:
        return f.read()

def load_user_session(session_data):
    # Vulnerability 6: Insecure Deserialization
    # Unpickles untrusted data
    decoded_data = base64.b64decode(session_data)
    session = pickle.loads(decoded_data)
    return session

def execute_command(user_input):
    # Vulnerability 7: Command Injection via subprocess
    # Direct shell execution with user input
    result = subprocess.run(f"echo {user_input}", shell=True, capture_output=True, text=True)
    return result.stdout

def get_admin_users():
    # Vulnerability 8: Another SQL Injection variant
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    role = "admin"
    # This looks safe but is still vulnerable if role comes from user input
    query = f"SELECT * FROM users WHERE role = '{role}' AND active = 1"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

def unsafe_eval(expression):
    # Vulnerability 9: Code Injection via eval
    # Never use eval with user input!
    try:
        result = eval(expression)
        return result
    except:
        return "Error in expression"

def weak_crypto():
    # Vulnerability 10: Weak cryptographic practices
    import hashlib
    password = "user_password"
    # MD5 is cryptographically broken
    weak_hash = hashlib.md5(password.encode()).hexdigest()
    return weak_hash

if __name__ == "__main__":
    print("Test App Running")
    # print(get_user("admin"))
    # print(ping_server("8.8.8.8"))
    # print(execute_command("hello world"))
    # print(unsafe_eval("2 + 2"))