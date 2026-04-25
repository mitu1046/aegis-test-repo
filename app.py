import sqlite3
import pickle
import base64
import hashlib
import json
import os

# Vulnerability 1: Hardcoded AWS Credentials
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def get_user_by_name(username):
    # Vulnerability 2: SQL Injection
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    result = cursor.fetchone()
    conn.close()
    return result

def load_user_prefs(prefs_data_base64):
    # Vulnerability 3: Insecure Deserialization
    decoded_data = base64.b64decode(prefs_data_base64)
    prefs = pickle.loads(decoded_data)
    return prefs

def store_password(password):
    # Vulnerability 4: Weak Cryptographic Hashing
    m = hashlib.md5()
    m.update(password.encode('utf-8'))
    return m.hexdigest()

if __name__ == "__main__":
    print("Vulnerable Test App Running")