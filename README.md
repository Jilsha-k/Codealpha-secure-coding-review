# Secure Code Review of Python Authentication System (OWASP Top 10)

## 📌 Overview
This project focuses on identifying and fixing security vulnerabilities in a Python-based login application. The analysis follows OWASP Top 10 principles, highlighting common weaknesses in authentication and input handling.

---

## 🎯 Objective
- Identify insecure coding practices in a login system  
- Analyze authentication-related vulnerabilities  
- Implement secure coding techniques to mitigate risks  

---

## 🖥️ Application Description
The application is a simple login system built using Python and Flask. It initially contained insecure implementations, which were analyzed and improved to follow secure coding standards.

---

## ⚠️ Vulnerabilities Identified
- Hardcoded credentials in source code  
- Plaintext password storage  
- Lack of input validation  
- Weak authentication logic  

---

## 🔐 Security Improvements Implemented
- Removed hardcoded credentials  
- Implemented hashed password storage  
- Added proper input validation  
- Improved authentication mechanism  

---

## ⚖️ Before vs After

| Issue | Before | After |
|------|--------|------|
| Password Storage | Plaintext | Hashed |
| Input Validation | None | Implemented |
| Authentication | Weak | Secure |

---

## 🔒 Security Impact
These improvements help prevent:
- Unauthorized access  
- Credential theft  
- Injection attacks  
- Authentication bypass  

---

## 🛠️ Tools & Technologies Used
- Python  
- Flask  
- OWASP Top 10  

---

## 📁 Project Structure
app.py # Main application
login.py # Basic login (insecure version)
secure_login.py # Improved secure version


---

## 💡 Key Takeaway
This project demonstrates practical understanding of identifying and mitigating real-world security vulnerabilities in web applications.
