import getpass
import hashlib
import logging

logging.basicConfig(filename="logs/login.log",level=logging.INFO,format="%(asctime)s - %(message)s")

stored_user = "admin"

stored_pass = hashlib.sha256("admin@123".encode()).hexdigest()

attempts = 3
while attempts > 0:
   username = input("Enter username:")
   password = getpass.getpass("Enter password: ")
   hashed_input = hashlib.sha256(password.encode()).hexdigest()
   if username == stored_user and hashed_input  == stored_pass:
       print("Login SuccessFull")
       break
   else:
       attempts -= 1
       logging.info("Failed login attempt for user: " + username)
       print("Invalid Credentials")
if attempts == 0:
   print("Account Locked")
