#!/usr/bin/env python3
"""
Configuration file with security vulnerabilities
"""

import os

# Vulnerability 1: Hardcoded API keys
API_KEY = "sk-1234567890abcdef"
STRIPE_SECRET_KEY = "sk_test_1234567890abcdef"
TWILIO_AUTH_TOKEN = "your_auth_token_here"

# Vulnerability 2: Hardcoded database credentials
DB_CONFIG = {
    'host': 'localhost',
    'user': 'admin',
    'password': 'admin123',  # Weak password
    'database': 'production_db'
}

# Vulnerability 3: Hardcoded encryption keys
ENCRYPTION_KEY = b'sixteen byte key'  # Too short for AES
SECRET_SALT = "hardcoded_salt_123"

# Vulnerability 4: Insecure default settings
DEBUG_MODE = True  # Should be False in production
ALLOW_ALL_ORIGINS = True
DISABLE_SSL_VERIFICATION = True

# Vulnerability 5: Weak JWT configuration
JWT_CONFIG = {
    'secret': 'weak_secret',
    'algorithm': 'none',  # No signature verification
    'expiration': 31536000  # 1 year - too long
}

# Vulnerability 6: Insecure file permissions
def create_temp_file(content):
    temp_file = '/tmp/sensitive_data.txt'
    with open(temp_file, 'w') as f:
        f.write(content)
    # Vulnerability: File created with default permissions (readable by all)
    return temp_file

# Vulnerability 7: Logging sensitive data
def log_user_activity(username, password, credit_card):
    log_message = f"User {username} logged in with password {password} and card {credit_card}"
    print(log_message)  # Logs sensitive data
    return log_message

# Vulnerability 8: Insecure random number generation
import random
def generate_session_token():
    # Using weak random number generator for security-critical token
    return str(random.randint(100000, 999999))

# Vulnerability 9: SQL connection string with credentials
DATABASE_URL = "mysql://root:password@localhost:3306/sensitive_db"

# Vulnerability 10: Hardcoded admin credentials
ADMIN_USERS = {
    'admin': 'admin',
    'root': 'toor',
    'administrator': '123456'
}

class DatabaseConnection:
    def __init__(self):
        # Vulnerability 11: Hardcoded connection details
        self.host = "prod-db-server.company.com"
        self.username = "db_admin"
        self.password = "Sup3rS3cr3t!"
        self.port = 3306
    
    def connect(self):
        # Vulnerability 12: No SSL/TLS for database connection
        connection_string = f"mysql://{self.username}:{self.password}@{self.host}:{self.port}/production"
        return connection_string

# Vulnerability 13: Exposed internal URLs
INTERNAL_SERVICES = {
    'admin_panel': 'http://internal-admin.company.com/admin',
    'database_admin': 'http://db-admin.internal:8080',
    'monitoring': 'http://monitoring.internal/dashboard'
}

# Vulnerability 14: Weak CORS configuration
CORS_CONFIG = {
    'origins': ['*'],  # Allows all origins
    'methods': ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
    'allow_credentials': True
}

if __name__ == "__main__":
    print("Configuration loaded")
    print(f"API Key: {API_KEY}")
    print(f"Database: {DATABASE_URL}")
    print(f"Admin users: {ADMIN_USERS}")