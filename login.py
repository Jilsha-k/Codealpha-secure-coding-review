username=input("Enter username:")
password=input("Enter password:")

stored_user="admin"
stored_pass="admin@123"
if username == stored_user and password == stored_pass:
  print("Login SuccessFull")
else:
  print("Invalid Credentials")
