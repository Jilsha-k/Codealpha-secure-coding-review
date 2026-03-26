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
```

---

## Results
- Successfully identified critical security flaws  
- Improved application security using secure coding practices  
- Demonstrated difference between insecure and secure implementations  
- Demonstrated practical mitigation of OWASP Top 10 vulnerabilities in a real-world login scenario  

---

## Screenshots
(Add screenshots of login page, error handling, and secure login output here)

---

## Learning Outcome
- Strong understanding of secure coding principles  
- Practical knowledge of authentication vulnerabilities  
- Ability to analyze and fix insecure applications  

---

## 🔐 Security Mapping (OWASP Top 10)
- A2: Broken Authentication  
- A3: Sensitive Data Exposure  

---

## Future Improvements
- Implement multi-factor authentication (MFA)  
- Add database integration with secure storage  
- Implement session management and protection  

---

## Conclusion
This project demonstrates how insecure coding practices can lead to vulnerabilities and how they can be mitigated using industry-standard security practices.
