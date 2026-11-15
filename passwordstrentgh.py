
#type "quit" to quit the program.

COMMON_PASSWORDS = {"123456", "password", "qwerty", "12345678",
                    "111111", "abc123", "letmein", "iloveyou", "admin"}


while True:
   password = input("enter your password: ")
   if password == "quit":
     break


   if password.lower() in COMMON_PASSWORDS:
    print("this is a very common password. Pick another one.")
   else:
    if len(password) <=8:
     print("your password is too short. use at least 9 characters.")
    else:
      if not any(x.isdigit() for x in password):
       print("add at least one number.")
      else:
        if not any(x.isupper() for x in password):
         print("add at least one uppercase letter.")
        else:
         if not any(not x.isalnum() for x in password):
          print("add at least one symbol like '!' or '@'.")
         else:
          print("your password is strong and secure.")
              