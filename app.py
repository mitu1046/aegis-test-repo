import sqlite3
import pickle
import base64
import hashlib
import json
import os

# Fixed: AWS Credentials now loaded from environment variables
def get_aws_secret_key():
    return os.getenv('AWS_SECRET_KEY')

AWS_SECRET_KEY = get_aws_secret_key()

def get_user_by_name(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()
    conn.close()
    return result

def load_user_prefs(prefs_data_base64):
    decoded_data = base64.b64decode(prefs_data_base64)
    prefs = pickle.loads(decoded_data)
    return prefs

def store_password(password):
    m = hashlib.md5()
    m.update(password.encode('utf-8'))
    return m.hexdigest()

if __name__ == "__main__":
    print("Vulnerable Test App Running")