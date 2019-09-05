import random
import string
t=1;
def password_generator(password_length):
    password_characters=string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation
    return "".join(random.choice(password_characters)for i in range(password_length))

while t:
    print("Do u want to generate password:\n")
    print("1.PRESS 1 TO GENERATE\n")
    print("2.PRESS 0 TO EXIT\n")
    t=int(input())
    if t==1:
          n=int(input("Enter the length of password to be generated:"))
          if n<7:
             print("The password length should be of atleast 8 characters\n")
          else:
             str1=password_generator(n)
             print("Your password is:",str1)
    else:
        exit(0);
    
        
        
