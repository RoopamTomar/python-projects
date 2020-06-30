"""Write a password generator in Python. Be creative with how you generate passwords
- strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a new password.
Include your run-time code in a main method.
Extra:
Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list."""
import random
pool = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
pool1 = ['A','B','C','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','(',')','<','>']
def password(pool,len):
    y =','.join(random.sample(pool,len))
    return y.replace(",","")

def strong_password(pool1,len):
    z = ','.join(random.sample(pool1,len))
    return z.replace(",","")

length = int(input("enter whether you want strong password or weak password by entering the length : "))
if length < 5:
    print(password(pool,length))
elif length >= 5:
    print(strong_password(pool1,length))
else:
    print("cant create password for this length")