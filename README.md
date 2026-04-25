# Aegis Test Repository

This repository contains intentionally vulnerable code for testing the Aegis security system.

## Vulnerabilities Included

### app.py
- SQL Injection (multiple variants)
- Command Injection 
- Path Traversal
- Insecure Deserialization
- Code Injection (eval)
- Weak Cryptography
- Hardcoded Credentials

### web_app.py
- Flask web application with 16 different vulnerabilities
- XSS, CSRF, Authentication bypass
- Information disclosure
- Debug mode in production

### config.py
- Hardcoded API keys and secrets
- Weak configuration settings
- Insecure defaults
- Credential exposure

## Usage

This code is intentionally vulnerable and should only be used for testing security tools like Aegis.

**DO NOT USE IN PRODUCTION!**
