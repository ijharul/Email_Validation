import re
email_condition=r"^[a-z]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("Enter a you Email Id:")

if re.search(email_condition,user_email):
  print("Correct Email!")
else:
  print("Invalid Email!")