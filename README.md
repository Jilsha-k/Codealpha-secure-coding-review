# Secure Code Review – Python Login System (OWASP Based)

## Overview
This project focuses on identifying and fixing security vulnerabilities in a Python-based login application. The analysis is based on OWASP Top 10 principles, highlighting common weaknesses in authentication and input handling.

---

## Objective
- Identify insecure coding practices in a login system  
- Analyze vulnerabilities related to authentication  
- Implement secure coding techniques to mitigate risks  

---

## Application Description
The application is a simple login system built using Python and Flask. It initially contained insecure implementations, which were analyzed and improved to follow secure coding standards.

---

## Vulnerabilities Identified
- Hardcoded credentials in source code  
- Plaintext password storage  
- Lack of input validation  
- Weak authentication logic  

---

## Security Improvements Implemented
- Removed hardcoded credentials  
- Implemented hashed password storage  
- Added proper input validation  
- Improved authentication mechanism  

---

## Tools & Technologies Used
- Python  
- Flask  
- OWASP Top 10  

---

## Project Structure
```bash
app.py              # Main application
login.py            # Basic login (insecure version)
secure_login.py     # Improved secure version
